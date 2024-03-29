import urllib.request, urllib.parse, urllib.error
import glob, os
from threading import Thread
from time import sleep


threadList = []
fileList = []

foundFilesCount = 0

def gatherNaviChara(filename):    
    
    try:
        f = urllib.request.urlopen("http://dv5bk1m8igv7v.cloudfront.net/asset/21900/content/sgtext/" + filename)
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

    for filename in glob.glob("resultSgtext/" + ""):    
        alreadyExistFiles.append(filename[9:])
    
    for i in range(404, 450):

        s = "sgtext_units_%03d.zip" % (i)
        
        if not s in alreadyExistFiles:        
            fileList.append(s)

        for j in range(631, 660):

            s = "sgtext_SkillDescription_%03d.zip" % (j)

            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for k in range(339, 380):

            s = "sgtext_en_%03d.zip" % (k)
            
            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for l in range(520, 550):

            s = "sgtext_extraPassiveSkill_DESC_%03d.zip" % (l)
            
            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for m in range(300, 340):

            s = "sgtext_spheresShortDescription_%03d.zip" % (m)
            
            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for n in range(491, 520):

            s = "sgtext_leaderSkillDescription_%03d.zip" % (n)
            
            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for o in range(392, 410):
		
            s = "sgtext_FE_SKILL_NAME_%03d.zip" % (o)
			
            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for p in range(432, 450):
            
            s = "sgtext_extraPassiveSkill_Name_%03d.zip" % (p)
            
            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for q in range(481, 500):
            
            s = "sgtext_skillName_%03d.zip" % (q)
            
            if not s in alreadyExistFiles:
                fileList.append(s)
                
        for r in range(408, 440):
            
            s = "sgtext_leaderSkillName_%03d.zip" % (r)
            
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
