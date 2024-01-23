import fnmatch
import os


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


for i in find("*.py", "D:\\VARUN\\PROGRAMMING 3.9\\"):
    print(i)