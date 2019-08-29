import urllib.request, urllib.parse, urllib.error
import glob, os
from threading import Thread
from time import sleep


threadList = []
fileList = []

foundFilesCount = 0

def gatherUnitIlls(filename):

	try:
		f = urllib.request.urlopen("http://dv5bk1m8igv7v.cloudfront.net/asset/2400/content/gacha/" + filename)
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

	
	for i in range(28, 32):
		for j in range(1,36):
		   
			s = "gacha_img_201908%02dA_S%d.png" % (i, j)

			if not (s in alreadyExistFiles):
					fileList.append(s)
					s = "gacha_img_201908%02dB_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
						fileList.append(s)
						
					s = "gacha_img_201908%02dC_S%d.png" % (i, j)
				
					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dD_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dE_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dF_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dG_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dH_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dI_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dJ_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dK_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dL_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dM_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dN_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dO_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dP_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dQ_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dR_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dS_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dT_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dU_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dV_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dW_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dX_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dY_S%d.png" % (i, j)

					if not s in alreadyExistFiles:
							fileList.append(s)
						
					s = "gacha_img_201908%02dZ_S%d.png" % (i, j)
				
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
