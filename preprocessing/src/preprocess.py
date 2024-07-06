import sys
import os
import json
import pandas as pd
import ffmpeg
import asyncio
from ffmpeg import Progress
from ffmpeg.asyncio import FFmpeg
from argparse import ArgumentParser

def parse_srt_file(filename):
    w = []
    t = 0
    t_old =0
    f = open(str(filename))
    for i, x in enumerate(f):
        if(len(x)<3): 
            continue
        if(x[2]==':'):
            y = x.split(':')
            y= y[0:3]
            y[2]= y[2][:-11]
            if len(y) <= 1:
                continue
            t_old = t
            t = int(y[0])*60*60 + int(y[1]) * 60 + int(y[2])
            w.append([t_old, t-t_old, str(str(filename[:-4]) + str(i//2))])
    f.close()
    return w


if __name__ == "__main__":
    parse_srt_file(os.path.join(os.getcwd(), "srt_files", "data", "Agent_Vinod.srt"))
    
    
    
    
    
    # parser = ArgumentParser()
    # parser.add_argument("--file", type=str, required=True, help="Movie file to preprocess")
    # parser.add_argument("-s", "--short-name", type=str, required=True, help="Shortname of the movie")
    # parser.add_argument("-j", "--json", type=str, required=True, help="path to json dataset file")
    # parser.add_argument("-d", "--dir", type=str, required=False, help="path to directory to save the preprocessed files")
    # parser.add_argument("-c", "--config", type=str, required=False, help="path to yml config file")
    # args = parser.parse_args()
    
    # CWD = os.getcwd()
    
    # #hyperparameters
    # utterances_in_context= 12
    # start_buffer= 0.5
    # end_buffer= 0.5
    
    # if args.dir is None:
    #     args.dir = os.path.join(os.getcwd(), args.short_name)
    
    