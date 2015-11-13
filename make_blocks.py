import sys, random, cv2, os
import numpy as np

# based on http://stackoverflow.com/questions/14593441/how-to-reorder-pixels
print sys.argv
_, path, rot, block_length = sys.argv
block_length = int(block_length)

rotate = True
# if third argument is not 'rotate', set rotate = F
if rot != "rotate":
    rotate = False

print "path: " + path + " \trotate: " + str(rotate)

for file in os.listdir(path):
    if file.endswith(".jpg"):
        print "processing file " + file
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

        if block_length == 80:
            myorder=[32, 35, 23, 18,  9, 19,  7,  0,  8,  3, 37, 16, 11, 39, 17,  1, 13, 33, 44, 15, 46,  6, 10, 38, 2,  5, 21, 20, 22, 45, 26, 12, 24, 47, 28, 14,  4, 36, 27, 43, 34, 40, 29, 25, 42, 30, 31, 41]
        elif block_length == 160:
            myorder=[11,  8,  6,  4,  3,  2,  7, 10,  1,  9,  5,  0]
        else:
            print "block length of " + str(block_length) + " is not supported. Exiting."
            sys.exit(1)

        shuffle = [ shuffle[i] for i in myorder]
        # create a blank image
        mask = np.zeros((width, height, 3),np.uint8)
        # paste the boxes onto the new image
        for box, sbox in zip(blockmap, shuffle):
            mask[box[0]:box[2], box[1]:box[3]] = img[sbox[0]:sbox[2], sbox[1]:sbox[3]]

        if rotate == True:
            print "rotating frame"
            mask = np.rot90(mask, k=2)
        # write over each image
        cv2.imwrite(file,mask)
print "done"
