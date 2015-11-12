### meghan_frog_videos

#### reverse_meghan_frog_video
`reverse_meghan_frog_video` is a plain text document that contains that code to clip her frog video up to the point where the male starts calling, reverse that segment of the video, then concatenate the forward and backward versions. The commands should be executed in a unix terminal that has ffmpeg, preferably installed via homebrew.

#### final_frog_video
`final_frog_video` is the .avi video that results from following the instructions in `reverse_meghan_frog_video`

#### randomize_pixels.py
`randomize_pixels.py` is a python script that using the Fisher-Yates algorithm to randomize pixels in individual frames. It is run like `python randomize_pixels directory/containing/jpg/files`. It is called in the `shuffle_pixels_video.sh` bash script.

#### shuffle_pixels_video.sh
`shuffle_pixels_video.sh` is a bash script that can be used to take any video, decompose it into its individual frames, randomize the pixels in each frame, then stitch the video back together again. To do all of this at once, you must `chmod +x shuffle_pixels_video.sh` to make the script executable. Then I recommend running `bash -x shuffle_pixels_video.sh` to run the script in debugging mode.

As written now, the video you want to perform these actions on must be called `final_frog_video.avi`; the code could easily be changed have this not be the case.

The script will create a folder to hold the individual frames in; it deletes this folder before it exists.

This script will take a long time to run on even reasonally long videos.
