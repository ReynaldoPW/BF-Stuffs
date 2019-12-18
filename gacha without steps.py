import urllib.request, urllib.parse, urllib.error
import glob, os
from threading import Thread
from time import sleep


threadList = []
fileList = []

foundFilesCount = 0

def gatherUnitIlls(filename):

	try:
		f = urllib.request.urlopen("http://dv5bk1m8igv7v.cloudfront.net/asset/2900/content/gacha/" + filename)
		#f = urllib.urlopen("http://v2.cdn.android.brave.a-lim.jp//unit/img/" + filename)
		fetched = f.read()
		f.close()
		
		print(filename, "found")
		f = open ("gacha/" + filename, "wb")
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

	for filename in glob.glob("gacha/" + "*.png"):    
		alreadyExistFiles.append(filename[6:])

	print("Already exist: ", len(alreadyExistFiles))

	
	for i in range(1, 32):
			s = "gacha_img_201912%02dA.png" % (i)

			if not (s in alreadyExistFiles):
					fileList.append(s)

					s = "gacha_img_201912%02dB.png" % (i)

					if not s in alreadyExistFiles:
						fileList.append(s)
						
					s = "gacha_img_201912%02dC.png" % (i)
				
					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dD.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dE.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dF.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dG.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dH.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dI.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dJ.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dK.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dL.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dM.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dN.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dO.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dP.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dQ.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dR.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dS.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dT.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dU.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dV.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dW.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dX.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dY.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dZ.png" % (i)
				
			if not (s in alreadyExistFiles):
				fileList.append(s)

			for j in range(0,13):
                                s = "Brave19%02d.png" % (j)
                                if not (s in alreadyExistFiles):
                                        fileList.append(s)

	for i, filename in enumerate(fileList):        
		threadList.append(Thread(target = gatherUnitIlls, args = (filename,)))        

	for threadIndividual in threadList:
		sleep(0.03)
		threadIndividual.start()
	
	for threadIndividual in threadList:
		threadIndividual.join()

	write_to_log("BFGL Unit Illustration", "Found " + str(foundFilesCount) + " new files, " + str(len(alreadyExistFiles)) + " already exist files\n")
