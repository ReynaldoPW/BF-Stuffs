import urllib.request, urllib.parse, urllib.error
import glob, os
from threading import Thread
from time import sleep


threadList = []
fileList = []

foundFilesCount = 0

def gatherNaviChara(filename):    
    
    try:
        f = urllib.request.urlopen("http://dv5bk1m8igv7v.cloudfront.net/asset/21900/content/dungeon/" + filename)
        fetched = f.read()
        f.close()

        print(filename, "found")
        f = open ("resultDungeon/" + filename, "wb")
        f.write(fetched)
        f.close()

        global foundFilesCount
        foundFilesCount += 1

        write_to_log("BFGL Navi Chara", "Found " + filename + "\n")
        
    except urllib.error.URLError:    
        print("File not found : ", filename)


    
if __name__ == "__main__":

    alreadyExistFiles = []

    for filename in glob.glob("resultDungeon/" + "*.png"):    
        alreadyExistFiles.append(filename[7:])
    
    for i in range(0, 7):
        for j in range(0, 150):
            for k in range(0, 10):
                    s = "sp_quest_banner_8%d%03d%d.png" % (i, j, k)
                    if not (s in alreadyExistFiles):
                        fileList.append(s)

                    for l in range(0, 6):
                        s = "sp_quest_banner_8%d%03d%d_%d.png" % (i, j, k, l)
                        if not s in alreadyExistFiles:
                            fileList.append(s) 

    for i, filename in enumerate(fileList):        
        threadList.append(Thread(target = gatherNaviChara, args = (filename,)))

    for threadIndividual in threadList:
        sleep(0.1)
        threadIndividual.start()
    
    for threadIndividual in threadList:
        threadIndividual.join()

    write_to_log("BFGL Navi Chara", "Found " + str(foundFilesCount) + " new files, " + str(len(alreadyExistFiles)) + " already exist files\n")    
