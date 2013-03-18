/f/Program\ Files\ \(x86\)/ffmpeg/ffmpeg.exe -i "$1" -strict -2 -vcodec libx264 -acodec aac -f mp4 -b 4000k "$1.mp4"
rm -f "$1"
