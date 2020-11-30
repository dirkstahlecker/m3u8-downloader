import re
import os

outputFile = "output.mp4"

def getText():
	with open('input.txt', 'r') as file:
		data = file.read().replace('\n', '')
	return data

def findVideoUrl():
	rawStr = getText()

	m = re.search('RESOLUTION:\s*[\d|x]+,\s*URL:\s*([\S]+)', rawStr)
	videoURL = m.group(1)
	print(videoURL)

	# print (m.group(m.groups() - 1))

	# strForAudio = rawStr.substr(rawStr.indexOf(videoURL))

	# audioRe = re.compile( , re.S | re.M)
	audioMatches = re.findall('URL:\s*([\S]+)', rawStr)
	audioUrl = audioMatches[len(audioMatches) -1]
	print(audioUrl)

	runDownloader(videoURL, audioUrl)

def runDownloader(videoURL, audioURL):
	command = "./download_m3u8 "+ videoURL + " " + audioURL + " " + outputFile

	os.system(command)

findVideoUrl()
