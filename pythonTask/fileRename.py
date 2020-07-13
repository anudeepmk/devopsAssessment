import itertools, os, glob, time, sys
if len(sys.argv) == 4:
    pathtoDir, prefix, suffix = sys.argv[1], sys.argv[2], sys.argv[3]
    if not os.path.isdir(pathtoDir):
        print("Entered directory " + pathtoDir + " does not exist")
        sys.exit()

else:
    print("Enter as follows: " + sys.argv[0] + " <DirectorytoCheck> <prefix> <suffix>")
    sys.exit()

##For 3 padded integer count which increments per file
count = 0

def multiple_file_types(*patterns):
    return itertools.chain.from_iterable(glob.iglob(pathtoDir + '/' + pattern, recursive=True) for pattern in patterns)

for filename in multiple_file_types("*." + suffix):
    dateYear = time.strftime('%Y-%m-%d', time.gmtime(os.stat(filename).st_birthtime))
    paddedNum = str(count).zfill(3)
    os.rename(filename, prefix + "_" + dateYear + "_" + paddedNum + "." + filename.split('.')[-1])
    count += 1