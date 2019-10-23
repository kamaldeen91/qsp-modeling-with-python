def files_in_dir(dir, filters=None):
    """
    Discovers and returns all files in the provided directory matching the provided glob filters. Returned
    paths are relative to the provided directory.
    :param dir: Find files relative to here
    :return: All files discovered as paths relative to dir
    """
    import fnmatch
    import os

    filters = filters or ['*']
    discovered_files = []
    for root, dirnames, filenames in os.walk(dir):
        for filter in filters:
            for filename in fnmatch.filter(filenames, filter):
                trimmed = os.path.join(root, filename).replace("{}{}".format(dir, os.sep), "")
                discovered_files.append(trimmed)
    return discovered_files
