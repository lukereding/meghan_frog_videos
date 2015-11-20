from  numpy import *
import os, sys, cv2

# code based on: http://stackoverflow.com/questions/12926349/python-image-shuffle-failure-where-have-i-gone-wrong

def shuffle(ary):
    a=len(ary)
    b=a-1
    for d in range(b,0,-1):
         np.random.seed(11); e=random.randint(0,d)
        ary[[d,e]] = ary[[e,d]]
    return ary

script, path = sys.argv

for file in os.listdir(path):
    if file.endswith(".jpg"):

        print "processing " + str(file)
        frame = cv2.imread(file)
        shape = frame.shape

        # collapse the 2d photo into a 1d array
        frame = frame.reshape((shape[0]*shape[1],shape[2]))

        # randomize using Fisher-Yates algorithm
        frame = shuffle(frame)

        # go from 1d array to 2d photo
        frame = frame.reshape(shape)

        cv2.imwrite(file,frame)

print "done"
