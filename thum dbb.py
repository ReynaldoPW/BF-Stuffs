import urllib.request, urllib.parse, urllib.error
import glob, os
from threading import Thread
from time import sleep


threadList = []
fileList = []

foundFilesCount = 0

def gatherUnitIlls(filename):

    try:
        f = urllib.request.urlopen("http://dv5bk1m8igv7v.cloudfront.net/asset/2200/content/unit/img/" + filename)
        #f = urllib.urlopen("http://v2.cdn.android.brave.a-lim.jp//unit/img/" + filename)
        fetched = f.read()
        f.close()
        
        print(filename, "found")
        f = open ("thum/" + filename, "wb")
        f.write(fetched)
        f.close()

        global foundFilesCount
        foundFilesCount += 1

        write_to_log("BFGL Unit Illustration", "Found " + filename + "\n")
        
    except urllib.error.URLError:    
        print("File not found : ", filename)
        

############################################################
#==========================================================#
############################################################


if __name__ == "__main__":

    alreadyExistFiles = []

    for filename in glob.glob("thum/" + "*.png"):    
        alreadyExistFiles.append(filename[5:])

    print("Already exist: ", len(alreadyExistFiles))

    for i in range(1, 7):
        for j in range(0, 150):
            for k in range(7, 9):
                    s = "unit_ills_thum_8%d%03d%d_100.png" % (i, j, k)
                    if not (s in alreadyExistFiles):
                        fileList.append(s)

    for i, filename in enumerate(fileList):        
        threadList.append(Thread(target = gatherUnitIlls, args = (filename,)))        

    for threadIndividual in threadList:
        sleep(0.05)
        threadIndividual.start()
    
    for threadIndividual in threadList:
        threadIndividual.join()

    write_to_log("BFGL Unit Illustration", "Found " + str(foundFilesCount) + " new files, " + str(len(alreadyExistFiles)) + " already exist files\n")
