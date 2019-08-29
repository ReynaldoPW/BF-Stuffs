import urllib.request, urllib.parse, urllib.error
import glob, os
from threading import Thread
from time import sleep


threadList = []
fileList = []

foundFilesCount = 0

def gatherNaviChara(filename):    
    
    try:
        f = urllib.request.urlopen("http://dv5bk1m8igv7v.cloudfront.net/asset/2400/content/sgtext/" + filename)
        #f = urllib.request.urlopen("http://cdn.android.brave.a-lim.jp/event/" + filename)
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

    for filename in glob.glob("resultSgtext/" + "*.png"):    
        alreadyExistFiles.append(filename[9:])
    
    for i in range(355, 400):

        s = "sgtext_units_%03d.zip" % (i)
        
        if not s in alreadyExistFiles:        
            fileList.append(s)

        for j in range(520, 560):

            s = "sgtext_SkillDescription_%03d.zip" % (j)

            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for k in range(285, 330):

            s = "sgtext_en_%03d.zip" % (k)
            
            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for l in range(415, 460):

            s = "sgtext_extraPassiveSkill_DESC_%03d.zip" % (l)
            
            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for m in range(245, 290):

            s = "sgtext_spheresShortDescription_%03d.zip" % (m)
            
            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for n in range(400, 450):

            s = "sgtext_leaderSkillDescription_%03d.zip" % (n)
            
            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for o in range(285, 330):
            s = "sgtext_FE_SKILL_NAME_%03d.zip" % (o)
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
