import urllib.request, urllib.parse, urllib.error
import glob, os
from threading import Thread
from time import sleep


threadList = []
fileList = []

foundFilesCount = 0

def gatherSphereIlls(filename):

    try:
        f = urllib.request.urlopen("http://dv5bk1m8igv7v.cloudfront.net/asset/21900/content/item/" + filename)
        fetched = f.read()
        f.close()
        
        print(filename, "found")
        f = open ("sphere/" + filename, "wb")
        f.write(fetched)
        f.close()

        global foundFilesCount
        foundFilesCount += 1

        write_to_log("BFGL Sphere Illustration", "Found " + filename + "\n")
        
    except urllib.error.URLError:    
        print("File not found : ", filename)
        

############################################################
#==========================================================#
############################################################


if __name__ == "__main__":

    alreadyExistFiles = []

    for filename in glob.glob("sphere/" + "*.png"):    
        alreadyExistFiles.append(filename[7:])

    print("Already exist: ", len(alreadyExistFiles))

    for i in range(1, 2):
        for j in range(900, 999):
            for k in range(0, 10):
                s = "sphere_thum_8%d%03d%d.png" % (i, j, k)                
                if not (s in alreadyExistFiles):
                    fileList.append(s)
                elif (s in alreadyExistFiles):
                    print(s, "already exist")

    for i, filename in enumerate(fileList):        
        threadList.append(Thread(target = gatherSphereIlls, args = (filename,)))        

    for threadIndividual in threadList:
        sleep(0.05)
        threadIndividual.start()
    
    for threadIndividual in threadList:
        threadIndividual.join()

    write_to_log("BFGL Sphere Illustration", "Found " + str(foundFilesCount) + " new files, " + str(len(alreadyExistFiles)) + " already exist files\n")
