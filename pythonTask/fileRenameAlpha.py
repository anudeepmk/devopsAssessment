import itertools, os, glob, sys
if len(sys.argv) == 3:
    pathtoDir, suffix = sys.argv[1], sys.argv[2]
    if not os.path.isdir(pathtoDir):
        print("Entered directory " + pathtoDir + " does not exist")
        sys.exit()

else:
    print("Enter as follows: " + sys.argv[0] + " <DirectorytoCheck> <suffix>")
    sys.exit()


def multiple_file_types(*patterns):
    return itertools.chain.from_iterable(glob.iglob(pathtoDir + '/' + pattern, recursive=True) for pattern in patterns)

for filename in multiple_file_types("*." + suffix):
    os.chdir(pathtoDir)
    filename = filename.split('/')[-1]
    os.rename(filename, ''.join(sorted(filename.split('.')[-2], reverse = True) + list('.' + filename.split('.')[-1])))
