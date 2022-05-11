# Testing different sound bitrates and measure their quality
## Installation

FFMpeg needs to be installed:
### Debian based distros:
`sudo apt-get install ffmpeg`
### Windows:
Download and extract the latest ffmpeg build here: https://www.gyan.dev/ffmpeg/builds/ffmpeg-git-github

When extracted add to the PATH the /bin folder.

Then install ffmpeg-python:
`pip install ffmpeg-python`

Make sure the following dependecies are installed:
* matplotlib
* mosquito

or run `pip install mosqito matplotlib`

# Running the code
`python ./compresser.py`

It will create a list of 2 files for each configured bitrates, one .mp3 for the file size comparisson and one .wav for the computation of the sound quality metrics.
It will show one plot comparing the file size of the mp3 against the bitrate and another one comparing the bitrate against the "sharpness" metric using 4 different algorithms (din, aures, bismarck, fastl)
