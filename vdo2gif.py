#!bin/python3
import argparse
from moviepy.editor import *

argparser = argparse.ArgumentParser()

argparser.add_argument('inputdir',type=str, help='Input directory for video file')
argparser.add_argument('outputdir',type=str,help='Output directory for gif file')
argparser.add_argument('-r','--resize',type=float,action='store',dest='resize',default=1,help='scale the gif dimension relative to original video file.(0-1) default:1')
argparser.add_argument('-s','--speed',type=float,action='store',dest='speed',default=1,help='modify the speed of the gif relative to original video. default:1')
argparser.add_argument('-f','--fps',type=int, action='store',dest='framerate',default=25, help='framerate. default:25')
argparser.add_argument('-t', '--time',nargs=2, action='store', dest='time', metavar=('0:0:0','0:0:0'), help='the video within the timeline will be converted gif when specify.(Format: hr:min:sec)')

args = argparser.parse_args()

startTime = list()
endTime = list()
args.outputdir = args.outputdir.replace(".gif", "")
banner = """
scripted by -
     _   __                       ___  ___            _ _____ _           
    | | / /                       |  \/  |           | |_   _| |          
    | |/ /  __ _ _   _ _ __   __ _| .  . |_   _  __ _| |_| | | |__  _   _ 
    |    \ / _` | | | | '_ \ / _` | |\/| | | | |/ _` | __| | | '_ \| | | |
    | |\  \ (_| | |_| | | | | (_| | |  | | |_| | (_| | |_| | | | | | |_| |
    \_| \_/\__,_|\__,_|_| |_|\__, \_|  |_/\__, |\__,_|\__\_/ |_| |_|\__,_|
                              __/ |        __/ |                          
                             |___/        |___/                           

github: https://github.com/kmt29
"""
clip = None

if args.time != None:
    startTime = args.time[0].split(':',3)
    endTime = args.time[1].split(':',3)
    if len(startTime) > 3 or len(endTime) > 3:
        argparser.print_help()
        sys.exit()
    clip = (VideoFileClip(args.inputdir).subclip((float(startTime[0]),float(startTime[1]),float(startTime[2])),(float(endTime[0]),float(endTime[1]),float(endTime[2]))).resize(args.resize).speedx(args.speed))
    
if args.time == None:
    clip = VideoFileClip(args.inputdir).resize(args.resize).speedx(args.speed)

print(banner)

clip.write_gif(args.outputdir+'.gif',fps=args.framerate,program='ffmpeg')
  
