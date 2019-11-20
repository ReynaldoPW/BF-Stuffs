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

	for filename in glob.glob("gacha/" + "*.png"):    
		alreadyExistFiles.append(filename[6:])

	print("Already exist: ", len(alreadyExistFiles))

	
	for i in range(20, 32):
		for j in range(1,36):
		   
			s = "gacha_img_201911%02dA_s%d.png" % (i, j)

			if not (s in alreadyExistFiles):
					fileList.append(s)
					s = "gacha_img_201911%02dB_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
						fileList.append(s)
						
					s = "gacha_img_201911%02dC_s%d.png" % (i, j)
				
					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dD_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dE_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dF_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dG_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dH_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dI_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dJ_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dK_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dL_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dM_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dN_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dO_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dP_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dQ_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dR_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dS_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dT_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dU_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dV_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dW_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dX_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dY_s%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201911%02dZ_s%d.png" % (i, j)
				
			elif (s in alreadyExistFiles):
				print(s, "already exist")


	for i, filename in enumerate(fileList):        
		threadList.append(Thread(target = gatherUnitIlls, args = (filename,)))        

	for threadIndividual in threadList:
		sleep(0.01)
		threadIndividual.start()
	
	for threadIndividual in threadList:
		threadIndividual.join()

	write_to_log("BFGL Unit Illustration", "Found " + str(foundFilesCount) + " new files, " + str(len(alreadyExistFiles)) + " already exist files\n")
