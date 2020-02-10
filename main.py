# -*- coding: utf-8 -*-
from FFMPEG import FFMPEG
import os

if __name__ == '__main__':
    # CMD : ffmpeg -ss 00:00:00 -t 00:50:00 -i largefile.mp4 -acodec copy -vcodec copy smallfile.mp4
    # Extract just one frame from a video   : ffmpeg -i video.webm -ss 00:00:07.000 -vframes 1 thumb.jpg
    # Extract all frames from a video       : ffmpeg -i Sample.mkv ./test_images/thumb%04d.jpg -hide_banner

    ff = FFMPEG(del_temp_folder=True) 
    
    ff.start_time = '00:00:00'
    ff.finish_time = '00:00:06'
    
    ff.getAllVideos('.mp4')
    

    #info = ff.splitByTime('testvideo')
    #print(info)

    

    ff.info()
    ff.select()
    ff.runPool()
    ff.concatProcessingVideos()
    ff.open(
