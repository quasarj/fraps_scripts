import os
ffmpeg = "c:\\Program Files (x86)\\ffmpeg\\ffmpeg.exe"
args = "-i \"{0}\" -strict -2 -vcodec libx264 -acodec aac -f mp4 -b 4000k \"{1}.mp4\""

avis = [f for f in os.listdir('.') if f.lower().endswith('avi')]
print avis

for a in avis:
    print("\"{exe}\" {args}".format(
        exe=ffmpeg,
        args=args.format(a, a)
    ))
print "done"
