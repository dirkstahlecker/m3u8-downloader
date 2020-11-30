 #! /usr/bin/env ksh

videoPath=$0
audioPath=$1
outputPath=$2

videoTempPath=video.mp4
audioTempPath=audio.ts

#if [[ -e $2 ]]
#then
#	outputPath=$2
#else
#	outputPath="output.mp4"
#fi

echo $videoPath
echo $audioPath
echo $outputPath

#get video
echo "getting video"
ffmpeg -i $videoPath -c copy video.mp4 > /dev/null 2>&1
wait
echo "got video"

#get audio
echo "getting audio"
ffmpeg -i $audioPath -c copy -map a audio.ts > /dev/null 2>&1
wait
echo "got audio"

#combine
echo "combining"
ffmpeg -i $videoTempPath -i $audioTempPath -c:v copy -c:a aac $outputPath > /dev/null 2>&1
wait
echo "finished}


#clean up
rm $videoOutputPath
rm $audioOutputPath

return 0