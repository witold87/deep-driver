import subprocess
import os.path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument( '--input', help='Input file', required=True)
args = parser.parse_args()
command = 'MP4Box -add {} {}.mp4'.format(args.input, os.path.splitext(args.input)[0])

try:
    print('[+] Converting...')
    output = subprocess.check_output(command, stderr=subprocess.STDOUT, shell=True)
except subprocess.CalledProcessError as e:
    print('[-] FAIL:\ncmd:{}\noutput:{}'.format(e.cmd, e.output))

