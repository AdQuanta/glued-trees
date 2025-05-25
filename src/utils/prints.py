from ..utils.strings import StrEnum, SpecialChars, num_out_of_num, str_len_untill_first_newline
from ..utils import decorators, lists

from typing import Any, Literal, Optional, TextIO, List, Generic, TypeVar, Iterator, overload, Iterable, Sequence, cast, Collection, TypedDict
_T = TypeVar('_T')


import numpy as np

# For defining print std_out or other:
import sys
# For getting the terminal width:
import shutil

from numpy import inf


class StaticPrinter():

    def __init__(self, print_out:TextIO|Literal[False]=sys.stdout, in_place:bool=False) -> None:
        self.printed_lines_lengths : List[int] = []
        self.print_out : TextIO|Literal[False] = print_out
        self.in_place : bool = in_place

    @property
    def end_char(self)->str:
        if self.in_place:
            return ''
        else:
            return '\n'

    def _print(self, s:str, end:Optional[str]=None)->None:
        if end is None:
            end = self.end_char
        print_out = self.print_out
        if isinstance(print_out, bool) and print_out==False:
            return
        print(s, end=end, file=print_out)
    
    @decorators.ignore_first_method_call
    def clear(self) -> None:
        # Get info about what was printed until now:
        reversed_printed_lengths = self.printed_lines_lengths.copy()
        reversed_printed_lengths.reverse()

        # Act according to `in_place`:
        for is_first, is_last, line_width in lists.iterate_with_edge_indicators(reversed_printed_lengths):
            if self.in_place:
                if not is_first:
                    pass   #TODO: Here we have a small bug that causes stacked static printers to override one-another                    
                self._print(SpecialChars.BackSpace*line_width)
                self._print(" "*line_width)
                self._print(SpecialChars.BackSpace*line_width)
                if not is_last:
                    self._print(SpecialChars.LineUp)
            else:
                self._print(SpecialChars.LineUp, end=SpecialChars.LineClear)

        # Reset printed lengths:
        self.printed_lines_lengths = []
                
    def print(self, s:str) -> None:
        if self.print_out is None:
            return
        self.clear()
        print_lines = s.split(SpecialChars.NewLine)
        self.printed_lines_lengths = [len(line) for line in print_lines]
        self._print(s)
    



class StaticNumOutOfNum(Generic[_T]):
    def __init__(self, items:Iterable[_T]|int, print_prefix:str="", print_suffix:str="", print_out:TextIO|Literal[False]=sys.stdout, in_place:bool=False, _expected_length:int|None=None) -> None:    
        ## Fix different way of calling this object:
        if isinstance(items, int):
            items_ = range(items)
        else:
            items_ = items
        items_ = cast(Iterable[_T], items_,)

        ## Save basic data:
        self.static_printer : StaticPrinter = StaticPrinter(print_out=print_out, in_place=in_place)
        self.print_prefix :str = print_prefix
        self.print_suffix :str = print_suffix
        self.counter : int = -1
        self._is_iterated : bool = False
        self._items_iter : Iterator[_T] = iter(items_)

        # Get expected length:
        try: 
            _expected_length = len(items_)  #type: ignore   we're doing type ducking here
        except Exception:
            if _expected_length is None:
                _expected_length = int(inf)
        self.expected_length : int = _expected_length

        # First print:
        if self.expected_length>0:
            self._show()

    def __next__(self) -> _T:
        try:
            val = self.next()
        except StopIteration:
            self.clear()
            raise StopIteration
        return val

    def __iter__(self) -> "StaticNumOutOfNum":
        self._is_iterated = True
        return self

    def _check_end_iterations(self)->bool:
        return self._is_iterated and self.iteration_num > self.expected_length

    def next(self, increment:int=1, extra_str:Optional[str]=None, every:int=1) -> _T:
        self.counter += increment        
        self._show(extra_str)
        if self._check_end_iterations():
            raise StopIteration
        
        ## Chose return values:
        res = next(self._items_iter)
        return res

    def append_extra_str(self, extra_str:str)->None:
        self._show(extra_str)

    def clear(self):
        self.static_printer.clear()

    def _print(self, s:str):
        self.static_printer.print( s + self.print_suffix )

    @property
    def iteration_num(self) -> int:
        """Iteration-Number starting from 1"""
        return self.counter+1

    def _show(self, extra_str:Optional[str]=None):
        i = self.iteration_num
        expected_end = int( self.expected_length )
        s = num_out_of_num(i, expected_end)
        self._print( s )


class ProgressBar(Generic[_T]):

    def __new__(cls, items:int|Collection[_T]|Iterable[_T], **kwargs):
        if isinstance(items, int):
            assert "_expected_end" not in kwargs
            kwargs["_expected_end"] = items
            items = range(items)
        instance = super().__new__(cls)
        instance.__init__(items, **kwargs)
        return instance

    def __init__(self, 
        items:Collection[_T]|Iterable[_T]|int,
        /, *,
        _expected_end:int|Literal['infinity']|None=None,
        print_prefix: str = "", 
        print_suffix: str = "", 
        print_length: int | None = None,   # If None then resort to terminal width
        print_out: TextIO | Literal[False] = sys.stdout, 
        _bar_empty_char: str = '.',
        _bar_full_char: str = u'█'
    ) -> None:
        if hasattr(self, "_initialzied") and self._initialzied:
            return
        ## The main object to track what should be printed and deleted:
        self.static_printer : StaticPrinter = StaticPrinter(print_out=print_out)
        ## Save basic data:
        self.print_prefix :str = print_prefix
        self.print_suffix :str = print_suffix
        self.print_length :int|None = print_length
        ## Iteration variables:
        self._main_iter : Iterator[tuple[int, _T]] = enumerate(items)
        self._expected_end : int|Literal['unkonwn'] = _derive_expected_end(items, _expected_end)
        self._crnt_run_index : int = 0
        ## Printing characters:
        self._bar_empty_char : str = _bar_empty_char
        self._bar_full_char : str = _bar_full_char
        # Prevents double calling when using __new__
        self._initialzied : bool = True

    @classmethod
    def by_range(
        cls,
        num:int,
        *,
        print_prefix:str="", 
        print_suffix:str="", 
        print_length:int|None=None,   # If None then resort to terminal width
        print_out:TextIO|Literal[False]=sys.stdout, 
        _bar_empty_char:str='.',
        _bar_full_char:str=u'█',
    ) -> "ProgressBar[int]":
        prog_bar = cls(    #type: ignore
            range(num),
            _expected_end = num,
            print_prefix = print_prefix,
            print_suffix = print_suffix,
            print_length = print_length,
            print_out = print_out,
            _bar_empty_char = _bar_empty_char,
            _bar_full_char = _bar_full_char
        )
        prog_bar = cast(ProgressBar[int], prog_bar)
        return prog_bar  
      

    def __iter__(self) -> "_ProgressBarIterator[_T]":
        return _ProgressBarIterator(self)

    def next(self, skip:int=1, extra_str:str='') -> _T:
        assert skip>0, "Increment must be greater than 0"
        item : _T = None  #type: ignore
        for _ in range(skip):
            i, item = next(self._main_iter)
        self._crnt_run_index = i + 1
        self._show(extra_str=extra_str)
        return item

    def _derive_bar_str(self)->str:     
        """ Derives the full progress bar string + prefix and suffixes.
        """
        # Unpack properties:
        prefix_str = self.print_prefix
        suffix_str = self.print_suffix
        expected_end = self._expected_end
        e_c = self._bar_empty_char  #usually '.'
        f_c = self._bar_full_char  #usually  u'█'
        crnt_run_index = self._crnt_run_index

        ## Get the expected end: 
        print_length = self.print_length
        adjusted_terminal_width = get_crnt_terminal_width() - 5  # 5 for good measure
        if print_length is None:
            print_length = adjusted_terminal_width
        else:
            print_length = min(print_length, adjusted_terminal_width)

        if expected_end == 'unkonwn':
            expected_end = np.inf
            _num_out_of_num_str = f"{crnt_run_index:4}"
        elif isinstance(expected_end, int):
            _num_out_of_num_str = num_out_of_num(crnt_run_index, expected_end)
        else:
            raise TypeError(f"Expected end value of {expected_end} is not valid")

        ## Lengths of the full and empty bars:
        # Adding two for brackets and a few more for good measyre = -10:
        entire_bar_length = print_length - max(len(_num_out_of_num_str), 10) - len(prefix_str) - len(suffix_str) - 10
        if crnt_run_index > expected_end:
            full_bar_length = entire_bar_length
        else:
            full_bar_length = int(entire_bar_length*crnt_run_index/expected_end)
        empty_bar_length = entire_bar_length-full_bar_length
        
        ## The actual string:
        s = f"{prefix_str}[{f_c*full_bar_length}{(e_c*empty_bar_length)}] "+_num_out_of_num_str+suffix_str

        return s

    def _show(self, extra_str:str=''):
        s = self._derive_bar_str()
        s += " "+extra_str
        self.static_printer.print(s)

    def append_extra_str(self, s:str):
        self._show(extra_str=s)

    def clear(self) -> None:
        self.static_printer.clear()

    def __del__(self) -> None:
        self.clear()


class _ProgressBarIterator(Generic[_T]):

    def __init__(self, prog_bar_obj:ProgressBar[_T]) -> None:
        self.prog_bar_obj : ProgressBar[_T] = prog_bar_obj

    def __next__(self) -> _T:
        try:
            val = self.prog_bar_obj.next()
        except StopIteration:
            self.prog_bar_obj.static_printer.clear()
            raise StopIteration
        return val


def get_crnt_terminal_width()->int:
    terminal_size = shutil.get_terminal_size()
    width = terminal_size.columns
    return width


def _derive_expected_end(items:Collection[_T]|Iterable[_T], _expected_end:int|Literal['unkonwn']|None)->int|Literal['unkonwn']:
    try:
        items_len = len(items)  #type: ignore
    except Exception:
        items_len = 'unkonwn'
    
    if _expected_end is None:
        return items_len
    elif _expected_end == 'unkonwn':
        return items_len
    elif isinstance(_expected_end, int):
        if isinstance(items_len, int) and _expected_end != items_len:
            raise ValueError(f"Expected end value of {_expected_end} is not equal to the length of the items {items_len}")
        return _expected_end
    else:
        raise TypeError(f"Expected end value of {_expected_end} is not valid")

class PrintColors(StrEnum):
    DEFAULT = '\033[0m'
    # Styles:
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'
    UNDERLINE_THICK = '\033[21m'
    STRIKE_THROUGH = '\033[9m'
    ## Highlighted:
    HIGHLIGHTED = '\033[7m'
    HIGHLIGHTED_BLACK = '\033[40m'
    HIGHLIGHTED_RED = '\033[41m'
    HIGHLIGHTED_GREEN = '\033[42m'
    HIGHLIGHTED_YELLOW = '\033[43m'
    HIGHLIGHTED_BLUE = '\033[44m'
    HIGHLIGHTED_PURPLE = '\033[45m'
    HIGHLIGHTED_CYAN = '\033[46m'
    HIGHLIGHTED_GREY = '\033[47m'
    #
    HIGHLIGHTED_GREY_LIGHT = '\033[100m'
    HIGHLIGHTED_RED_LIGHT = '\033[101m'
    HIGHLIGHTED_GREEN_LIGHT = '\033[102m'
    HIGHLIGHTED_YELLOW_LIGHT = '\033[103m'
    HIGHLIGHTED_BLUE_LIGHT = '\033[104m'
    HIGHLIGHTED_PURPLE_LIGHT = '\033[105m'
    HIGHLIGHTED_CYAN_LIGHT = '\033[106m'
    HIGHLIGHTED_WHITE_LIGHT = '\033[107m'

    MARGIN_1 = '\033[51m'
    MARGIN_2 = '\033[52m' # seems equal to MARGIN_1
    
    ## colors
    BLACK = '\033[30m'
    RED_DARK = '\033[31m'
    GREEN_DARK = '\033[32m'
    YELLOW_DARK = '\033[33m'
    BLUE_DARK = '\033[34m'
    PURPLE_DARK = '\033[35m'
    CYAN_DARK = '\033[36m'
    GREY_DARK = '\033[37m'

    BLACK_LIGHT = '\033[90m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[96m'



def add_color(s:str, color:PrintColors, active:bool=True)->str:
    if not active:
        return s
    return color+s+PrintColors.DEFAULT

def print_warning(s:str)->None:
    warn1color = PrintColors.HIGHLIGHTED_YELLOW
    warn2color = PrintColors.YELLOW_DARK
    s = add_color("Warning: ", warn1color)+add_color(s, warn2color)
    print(s)


def fix_numpy_print_length(linewidth:int=10000, precision:int=2):
    np.set_printoptions(linewidth=linewidth)
    np.set_printoptions(precision=precision)


def numpy_array_shortened(arr:np.ndarray, precision:int=3)->None:
     with np.printoptions(precision=precision, suppress=True):
        print(arr)