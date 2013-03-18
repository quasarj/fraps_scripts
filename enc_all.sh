echo Encoding all raw avis in the dir
for i in *.avi
do 
    sh encode.sh "$i"
done
