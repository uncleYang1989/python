from PIL import Image, ImageSequence
import sys, os
filename="9963253270.gif"
im = Image.open(filename)
original_duration = im.info['duration']
frames = [frame.copy() for frame in ImageSequence.Iterator(im)]    
frames.reverse()

from images2gif import writeGif
writeGif("reverse_" + os.path.basename(filename), frames, duration=original_duration/1000.0, dither=0)