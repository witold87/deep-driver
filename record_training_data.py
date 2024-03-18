import picamera
import subprocess
import os.path
import time
import argparse
from datetime import datetime
from subprocess import CalledProcessError

training_video =''
filename = ''

def set_up_argparse():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--path', help='File path for saving video', required=False, default='/home/pi/')
    parser.add_argument(
        '--record', help='Number of seconds to be captured', type=int, required=True)
    parser.add_argument(
        '--mode', help='on_track / off_track_left / off_track_right', type=str, required=True)
    parser.add_argument(
        '--resX', help='Resolution X for image', required=False, type=int, default=640)
    parser.add_argument(
        '--resY', help='Resolution Y for image', required=False, type=int, default=480)

    return parser



def set_up_camera(args):
    camera = picamera.PiCamera()
    camera.resolution = (args.resX, args.resY)
    camera.rotation = 180
    return camera


'''
def set_up_file(args):
    filename = 'training_' + args.mode + '_' + datetime.now().strftime('%H-%M-%S.h264')
    save_path = args.path
    training_video = os.path.join(save_path, filename)
'''


def camera_recording(camera, args):
    filename = 'training_' + args.mode + '_' + datetime.now().strftime('%H-%M-%S.h264')
    save_path = args.path
    training_video = os.path.join(save_path, filename)
    camera.start_preview()
    time.sleep(2)
    camera.start_recording(training_video)
    seconds_to_record = args.record
    while seconds_to_record > 0:
        seconds_to_record -= 1
        print('[+] Recording seconds...{}'.format(seconds_to_record))
        time.sleep(1)
    camera.wait_recording(1)
    camera.stop_recording()

def main():
    args = set_up_argparse().parse_args()
    camera = set_up_camera(args)
    #set_up_file(args)
    camera_recording(camera, args)



if __name__ == '__main__':
    main()
    


