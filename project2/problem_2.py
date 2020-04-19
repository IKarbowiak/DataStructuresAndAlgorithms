import os


def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    if os.path.isfile(path):
        if path.endswith(suffix):
            return [path]
        else:
            return []

    if not os.path.isdir(path):
        return None

    result = []
    paths = os.listdir(path)
    first_path = paths[0]
    for p in paths:
        base_path = os.path.join(path, p)
        rest_path = find_files(suffix, base_path)
        if rest_path:
            result += rest_path

    return result


print(find_files(".c", "./testdir"))
# if we include testdir in current directory result should be:
#  ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']

print(find_files(".c", "./testdir/subdir5"))
# result should be ['./testdir/subdir5/a.c']

print(find_files(".c", "./testdir/subdir4"))
# result should be []

print(find_files(".c", "./ABC"))
# when directory does not exists, return None

print(find_files("A", "./testdir"))
# result should be [], any file ends with "A"

print(find_files("", "."))
# should return all files in current directory

print(find_files(".c", ""))
# should return None because "" is not a directory
