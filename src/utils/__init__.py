def add_all_utils_to_path():
    import pathlib, sys
    utils_folder = pathlib.Path(__file__).parents[1].__str__()
    if utils_folder not in sys.path:
        sys.path.append(utils_folder)
    