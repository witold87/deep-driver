import cv2
import argparse
import os
from datetime import datetime


def set_up_argparse():
    parser = argparse.ArgumentParser(formatter_class = argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--path', help='Path to video file', required=True)
    parser.add_argument('--mode', help='Mode: on_track / off_track_left / off_track_right', required=True)
    return parser


def add_timestamp():
    now = datetime.now()
    return now.strftime("%Y%m%d%H%M%S")


def create_dir_for_extracted_frames():
    p = './extracted_frames'
    if not os.path.isdir(p):
        try:
            os.mkdir(p)
        except OSError:
            print('[-] Creation of the directory {} failed.'.format(p))
        else:
            print('[+] Successfully created the directory {}.'.format(p))
    return p


def extract_frames(args):
    path = create_dir_for_extracted_frames()
    vidcap = cv2.VideoCapture(args.path)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(os.path.join(path, args.mode +'_frame{}_time{}.jpg'.format(count, add_timestamp())), image)
        success, image = vidcap.read()
        print('[+] Read frame #{}, status: {}.'.format(count, success))
        count += 1
    print('[+] Finished.')


def main():
    args = set_up_argparse()
    extract_frames(args.parse_args())




if __name__ == '__main__':
    main()
