# -*- coding: utf-8 -*-
import glob, os
from CPrint import CPrint as cp
from subprocess import Popen,PIPE
from copy import deepcopy
from multiprocessing import Pool
import sys

class FFMPEG:
    temp_video = 'temp_' 
    __processing_videos = []
    __processing_index_keeper = None
    __video_container = []
    __start_time = ''
    __finish_time = ''

    def __init__(self, del_temp_folder=False):
        if del_temp_folder:
            os.system('rm -rf temp_source') 
        
        try:
            os.mkdir('temp_source')
        except:
            cp.cprint(1,1, "Dir Make Error: temp_source cant be created")
            print(sys.exc_info())
    
    def info(self):
        info_template = '{:20}:{:.>20}'
        
        cp.cprint(3, 3, info_template.format('Start Time', self.__start_time))
        cp.cprint(3, 3, info_template.format('Finish Time', self.__finish_time))
        
        cp.cprint(3,3, 'video container')
        for _index, _video in enumerate(self.__video_container):
            print('{:<3} -> {}'.format(_index, _video))
             

    @property
    def start_time(self):
        return self.__start_time
    @start_time.setter
    def start_time(self, start_time):
        self.__start_time = start_time

    @property
    def finish_time(self):
        return self.__finish_time
    @finish_time.setter
    def finish_time(self, finish_time):
        self.__finish_time = finish_time
    
    def getAllVideos(self, filter):
        self.__video_container = glob.glob('*/*{}'.format(filter))

    def splitByTime(self, *args):
        if len(args) == 1:
            start_time = self.__start_time
            finish_time = self.__finish_time
            video = args[0]
        else:
            video, start_time, finish_time = args
        cmd = f'ffmpeg -y -ss {start_time} -t {finish_time} -i {video} -acodec copy -vcodec copy {self.temp_video}{video}'
        self.run(cmd)
        
        return str(video) + ' is completed!'
    
    def select(self):
        cp.cprint(3,1, 'Please enter the video index:', end='')
        index = input().split(',')
        
        if ':' in index:
            self.__processing_videos = deepcopy(self.__video_container)
        else:
            try:
                for i in index:
                    i = int(i)
                    self.__processing_videos.append(self.__video_container[i])
            except:
                print("Index Error")
        
        print(self.__processing_videos)
    
    def run(self, cmd):
        pipe = Popen(cmd, stdout=PIPE, shell=True) 
        stdout = pipe.stdout.read().decode("utf-8")
        
    def runPool(self):
        pool = Pool(processes=4)
        pool_result = pool.map(self.splitByTime, self.__processing_videos)
        cp.cprint(3,2, *pool_result, sep='\n')
         
    def prli(self, liste):
        for i,j in enumerate(liste):
            print('{:3}:{}'.format(i,''))

    def concatProcessingVideos(self):
        with open('concat.ffmpeg', 'w') as f:
            for _file in self.__processing_videos:
                f.write('file temp_{}\n'.format(_file))

        
        cmd = 'ffmpeg -y -f concat -i concat.ffmpeg -c copy final.mp4'
        self.run(cmd)
        

    def open(self):
        filename = 'final.mp4'
        self.run(f'cvlc {filename}')

# CMD : ffmpeg -ss 00:00:00 -t 00:50:00 -i largefile.mp4 -acodec copy -vcodec copy smallfile.mp4
# Extract just one frame from a video   : ffmpeg -i video.webm -ss 00:00:07.000 -vframes 1 thumb.jpg
# Extract all frames from a video       : ffmpeg -i Sample.mkv ./test_images/thumb%04d.jpg -hide_banner

