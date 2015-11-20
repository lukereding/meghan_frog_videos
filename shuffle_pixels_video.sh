## script for decomposing a video into photos, shuffling the pixels in each frame, and reassembling

ffmpeg -version

# make a new folder
mkdir images
cd images

# get individual frames as jpgs
ffmpeg -i ../final_frog_video.avi -an -qscale 1 %05d.jpg

# run python script
python ../randomize_pixels.py .

# put the frames back together
ffmpeg -f image2 -i %05d.jpg -r 30 -vcodec libx264 ../final_frog_video_randomized.avi

cd ..
rm -r images/
