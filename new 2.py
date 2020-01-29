import urllib.request, urllib.parse, urllib.error
import glob, os
from threading import Thread
from time import sleep


threadList = []
fileList = []

foundFilesCount = 0

def gatherUnitIlls(filename):

    try:
        f = urllib.request.urlopen("http://news.gumi.sg/bravefrontier/news/files/html/2020-01/" + filename)
        #f = urllib.urlopen("http://v2.cdn.android.brave.a-lim.jp//unit/img/" + filename)
        fetched = f.read()
        f.close()
        
        print(filename, "found")
        f = open ("resultEX/" + filename, "wb")
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

    for filename in glob.glob("resultEX/" + "*.html"):    
        alreadyExistFiles.append(filename[9:])

    print("Already exist: ", len(alreadyExistFiles))

    for i in range(0, 10):
        for j in range(0, 99):
            for k in range(0, 999):
                s = "UnitDetailsMiriam_1580%d%02d%03d.html" % (i, j, k)                
                if not (s in alreadyExistFiles):
                    fileList.append(s)
                elif (s in alreadyExistFiles):
                    print(s, "already exist")

    for i, filename in enumerate(fileList):        
        threadList.append(Thread(target = gatherUnitIlls, args = (filename,)))        

    for threadIndividual in threadList:
        sleep(0.05)
        threadIndividual.start()
    
    for threadIndividual in threadList:
        threadIndividual.join()

    write_to_log("BFGL Unit Illustration", "Found " + str(foundFilesCount) + " new files, " + str(len(alreadyExistFiles)) + " already exist files\n")
