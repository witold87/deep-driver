## Deep Driver Project Introduction
- Project date: 2019
- Project object: Design and run augmented RC car with replaced steering - from radio controlled car to autonomous car 
- Tech stack: python, pillow, open-cv, tensorflow (on Coral TPU, model inference), google cloud (model training)


## TL;DR

![deep-driver-success-gif.gif](deep-driver-success-gif.gif)

## Deep Driver Guide
This guide covers installation and using the scripts related to the code upload on this repository.

### Running the scripts
We have delivered some basic scripts in order to make the work easier at the beginning.  To make it also easy to read and develop, we have splitted the main logic into 4 different scripts:
- record data (gathering data)
- convert data (converting to more suitable format)
- extract frames (chopping raw data into separate images; even short movie produces many frames)
- classify - inferencing using our data, model and labels. 

#### Record (gather) data
For this job we have created a script which captures a footage from the camera and saves it to a file in a .h264 format.:

`python record_training_data.py --help`

will launch the quick help for running this script. To launch the minimum version of script, we need to add two parameters:

`python record_training_data.py --record <integer> --mode <string>`

where --record is the number of seconds you want to record, for example:

`python record_training_data.py --record 10` 

will record 10 seconds of footage. 
Second argument was "mode". Used for prelabeling activity. Any string value is acceptable, however, to be more clean, it is strongle recommended to use future label here, fo example:

`python record_training_data.py --record 10 --mode on_track`

will result in naming the files also as "on_track" so you will not get lost in the files later on.
By default, file will be saved in the /home/pi directory. If you wish to change it, use additional parameter: `--path` and write an absolute path to your destination folder.

#### Converting the data
Converting previously recorded file from .h264 format to .mp4 format. To do that type:

`python convert_training_data.py --input <file-location>`

Here, as an input, type the absolute path of the file recorded in the previous step, for example:

`python convert_training_data.py --input /home/pi/projects/deepdriver/recorderd_data/<filename>`

File will be converted and saved in the same location, so now in the destination folder you will have two file, named similary, but with two different formats.

#### Extracting frames
The last mandatory step for data preparation is to extract frames, our machine learning input, from our raw data.
To do that use script extract_frames.py :

`python extract_frames.py --path <file-location> --mode <string>`

whrere as file location you provide an absolute path to your training data file in .mp4 format, for example:

`python extract_frames.py --path /home/pi/projects/deepdriver/recorderd_data/<filename.mp4>`

And for the second parameter, `--mode`, stick to the labeling convention when recording was done, example:

`python extract_frames.py --path /home/pi/projects/deepdriver/recorderd_data/<filename.mp4> --mode on_track`

beacuse scripts will automatically create a subfolder called "extracted_frames" where it will put all files. Naming (`--mode`) is used to not mix all the files when recording multiple footages.

Gather all those file and use them as an input to the machine learning model. We have not manipulated those images at all - this is a task for you! Tweak the size, crop, adjust colors, contrast etc. to get acceptable form of input images. Train the model (Google Cloud Platform or write your own model compatible with Coral) and go to the next section.

#### Inferencing (predicting) the track
Having trained model and related labels, head towards the last script - classify image:

`python3 classify_image.py --model <path-to-model> --labels <path-to-labels>`

When the camera start you should be able to see how script makes real-time predictions.