import sys, random, cv2, os
import numpy as np

# based on http://stackoverflow.com/questions/14593441/how-to-reorder-pixels

# this will determine the size of the blocks. must be a multiple of the number of pixels in the width and height
block_length = 160

_, path = sys.argv

for file in os.listdir(path):
    if file.endswith(".jpg"):
        print "processing file" + file
        # read in the image
        img = cv2.imread(file)
        # save dimensions
        width, height, _ = img.shape
        # define blocks
        xblock = width / block_length
        yblock = height / block_length
        blockmap = [(xb*block_length, yb*block_length, (xb+1)*block_length, (yb+1)*block_length)
                for xb in xrange(xblock) for yb in xrange(yblock)]
        # shuffle in a repeatable way
        shuffle = list(blockmap)
        #order was determined randomally then hard-coded to be the same for each video
        myorder=[11,  8,  6,  4,  3,  2,  7, 10,  1,  9,  5,  0]
        shuffle = [ shuffle[i] for i in myorder]
        # create a blank image
        mask = np.zeros((width, height, 3),np.uint8)
        # paste the boxes onto the new image
        for box, sbox in zip(blockmap, shuffle):
            mask[box[0]:box[2], box[1]:box[3]] = img[sbox[0]:sbox[2], sbox[1]:sbox[3]]

        # write over each image
        cv2.imwrite(file,mask)
print "done"
