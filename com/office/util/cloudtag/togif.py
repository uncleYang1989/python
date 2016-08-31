from PIL import Image
import os
filelist = []
files = os.listdir("gifdir")
for f in files:
    f = "gifdir" + '/' + f
    if(os.path.isfile(f)):
        if (os.path.splitext(f)[1].upper() == ".BMP"):
            filelist.append(f)
        if (os.path.splitext(f)[1].upper() == ".JPG"):
            filelist.append(f)
        if (os.path.splitext(f)[1].upper() == ".PNG"):
            filelist.append(f)
        if (os.path.splitext(f)[1].upper() == ".TIF"):
            filelist.append(f)
outfile = "gif.gif"
for infile in filelist:
#         try:
            Image.open(infile).save(outfile)
            print "Covert to GIF successfully!"
#         except IOError:
            
            print "This format can not support!", infile
