import urllib.request, urllib.parse, urllib.error
import glob, os
from threading import Thread
from time import sleep


threadList = []
fileList = []

foundFilesCount = 0

def gatherUnitIlls(filename):

	try:
		f = urllib.request.urlopen("http://dv5bk1m8igv7v.cloudfront.net/asset/2700/content/gacha/" + filename)
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

	for filename in glob.glob("gacha/" + "*_3G.png"):    
		alreadyExistFiles.append(filename[6:])

	print("Already exist: ", len(alreadyExistFiles))

	
	for i in range(1, 32):
			s = "gacha_img_201912%02dA_3G.png" % (i)

			if not (s in alreadyExistFiles):
					fileList.append(s)

					s = "gacha_img_201912%02dB_3G.png" % (i)

					if not s in alreadyExistFiles:
						fileList.append(s)
						
					s = "gacha_img_201912%02dC_3G.png" % (i)
				
					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dD_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dE_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dF_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dG_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dH_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dI_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dJ_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dK_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dL_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dM_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dN_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dO_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dP_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dQ_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dR_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dS_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dT_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dU_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dV_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dW_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dX_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dY_3G.png" % (i)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201912%02dZ_3G.png" % (i)
				
			if not (s in alreadyExistFiles):
				fileList.append(s)


	for i, filename in enumerate(fileList):        
		threadList.append(Thread(target = gatherUnitIlls, args = (filename,)))        

	for threadIndividual in threadList:
		sleep(0.1)
		threadIndividual.start()
	
	for threadIndividual in threadList:
		threadIndividual.join()

	write_to_log("BFGL Unit Illustration", "Found " + str(foundFilesCount) + " new files, " + str(len(alreadyExistFiles)) + " already exist files\n")
