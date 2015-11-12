# make a video with blocks of the video reshuffled

ffmpeg -version

# make a new folder
mkdir images
cd images

# get individual frames as jpgs
ffmpeg -i ../final_frog_video.avi -an -qscale 1 %05d.jpg

# run python script
python ../make_blocks.py .

# put the frames back together
ffmpeg -f image2 -i %05d.jpg -r 30 -vcodec libx264 ../final_frog_video_blocks.avi

cd ..
rm -r images/
