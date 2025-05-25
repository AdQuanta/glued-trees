import os
from os.path import isfile
from os.path import isdir as isfolder
from os.path import sep as foldersep
from pathlib import Path


# Define a set of common file extensions
COMMON_EXTENSIONS = {'.mp4', '.mp3', '.txt', '.pdf', '.jpg', '.jpeg', '.png', '.gif', '.csv', '.json', '.xml', '.html', '.zip', '.tar', '.gz', '.bz2', '.7z'}

def _parse_path(path:str|Path) -> str:
    if isinstance(path, Path):
        return path.absolute().__str__()
    else:
        assert isinstance(path, str), f"Path must be a string or Path object, not {type(path)!r}"
    return path

def force_folder_exists(folder_full_path:str|Path) -> None:
    folder_full_path = _parse_path(folder_full_path)
    if not os.path.exists(folder_full_path):
        os.makedirs(folder_full_path)


def remove_folder(folder_full_path:str|Path, delete_files_in_folder_if_not_empty:bool=True) -> None:
    folder_full_path = _parse_path(folder_full_path)
    ## Remove all files in the folder
    if delete_files_in_folder_if_not_empty: 
        inner_files = get_all_files_fullpath_in_folder(folder_full_path)
        if len(inner_files) > 0:
            for file in inner_files:
                if isfile(file):
                    os.remove(file)
    ## Remove the folder itself
    if os.path.exists(folder_full_path):
        os.rmdir(folder_full_path)
    else:
        raise FileNotFoundError(f"Folder {folder_full_path!r} does not exist.")

def get_all_files_fullpath_in_folder(folder_full_path:str|Path) -> list[str]:
    folder_full_path = _parse_path(folder_full_path)
    return [folder_full_path+foldersep+filename for filename in get_all_file_names_in_folder(folder_full_path=folder_full_path)]


def get_all_file_names_in_folder(folder_full_path:str|Path) -> list[str]:
    folder_full_path = _parse_path(folder_full_path)
    return [file for file in os.listdir(folder_full_path) if not isfolder(folder_full_path+foldersep+file)]


def get_last_file_in_folder(folder_full_path:str|Path, none_if_empty:bool=True)->str:
    folder_full_path = _parse_path(folder_full_path)
    file_names = get_all_file_names_in_folder(folder_full_path=folder_full_path)
    if none_if_empty and len(file_names)==0:
        return None  #type: ignore
    return file_names[-1]

def has_extension(filename: str | Path) -> bool:
    path_type = filename if isinstance(filename, Path) else Path(filename)
    return path_type.suffix in COMMON_EXTENSIONS