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

This script will take a long time to run on even reasonably long videos.

#### make_blocks.sh
`make_blocks.sh` is a bash script that will take out the frames of a video named `final_frog_video.avi`, save them in a subdirectory called `images`, overwrite the frames with the original frames subdividied into chunks, then make a new video called `final_frog_video_blocks.avi`.  To run it, first do `chmod +x make_blocks.sh` then do `bash -x make_blocks`.

#### make_blocks.py
`make_blocks.py` is called by `make_blocks.sh` . It is run like `python make_blocks.py /path/to/directory/containing/jpgs rotate block_length`. It looks for jpgs in the specified folder, cuts them into blocks (the size of the blocks is determined by the `block_length` parameter), then puts the pieces back in a random order. (The order was initially determined by randomization, but the order is the same for each frame.) The second argument tells the program whether each frame should be rotated 180 degress (i.e. flipped upside down). Pass anything other that `rotate` and it will not rotate the frames. Finally, the last argument is the block length used to determine the size of the blocks. It must be a multiple of both the width and the height of each frame in pixels or else you'll get a video back that is a slightly different size than the one you put in. Default is set to 80 in `make_blocks.sh`.
