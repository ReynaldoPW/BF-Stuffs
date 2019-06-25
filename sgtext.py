import urllib.request, urllib.parse, urllib.error
import glob, os
from threading import Thread
from time import sleep


threadList = []
fileList = []

foundFilesCount = 0

def gatherNaviChara(filename):    
    
    try:
        f = urllib.request.urlopen("http://dlc.bfglobal.gumi.sg/content/sgtext/" + filename)
        fetched = f.read()
        f.close()

        print(filename, "found")
        f = open ("resultSgtext/" + filename, "wb")
        f.write(fetched)
        f.close()

        global foundFilesCount
        foundFilesCount += 1

        write_to_log("BFGL sgtext", "Found " + filename + "\n")
        
    except urllib.error.URLError:    
        print("File not found : ", filename)


    
if __name__ == "__main__":

    alreadyExistFiles = []

    for filename in glob.glob("resultSgtext/" + "*.zip"):    
        alreadyExistFiles.append(filename[9:])
    
    for i in range(278, 280):

        s = "sgtext_en_%03d.zip" % (i)
        
        if not s in alreadyExistFiles:        
            fileList.append(s)

        for j in range(506, 510):

            s = "sgtext_SkillDescription_%03d.zip" % (j)

            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for k in range(390, 395):

            s = "sgtext_leaderSkillDescription_%03d.zip" % (k)

            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for l in range(406, 410):

            s = "sgtext_extraPassiveSkill_DESC_%03d.zip" % (l)

            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for m in range(241, 245):

            s = "sgtext_spheresShortDescription_%03d.zip" % (m)

            if not s in alreadyExistFiles:
                fileList.append(s)
        
    for i, filename in enumerate(fileList):        
        threadList.append(Thread(target = gatherNaviChara, args = (filename,)))

    for threadIndividual in threadList:
        sleep(0.02)
        threadIndividual.start()
    
    for threadIndividual in threadList:
        threadIndividual.join()

    write_to_log("BFGL Navi Chara", "Found " + str(foundFilesCount) + " new files, " + str(len(alreadyExistFiles)) + " already exist files\n")    
