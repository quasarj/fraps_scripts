import os
import subprocess

ffmpeg = r"d:\ffmpeg\bin\ffmpeg.exe"
args = " -i \"{0}\" -strict -2 -vcodec libx264 -acodec aac -f mp4 -b 4000k \"{1}\""

avis = [f for f in os.listdir('.') if f.lower().endswith('avi')]
print(avis)

for filename in avis:
    shortname, ext = os.path.splitext(filename)
    dest_file = shortname + ".mp4"
    ret = subprocess.call(ffmpeg + args.format(filename, dest_file))
    if ret == 0: # ffmpeg returned successfully
        # check taht the destination file is there
        if os.path.isfile(dest_file):
            os.unlink(filename) # delete the original
    else:
        print("There was an error encoding! Not deleting original.")

print("Done")
