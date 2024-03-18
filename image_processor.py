from PIL import Image, ImageEnhance
import argparse
import os

class ImageProcessor:

    def load_from_file(self, file_name):
        self.img = Image.open(file_name)

    def process(self, contrast):
        self.img = self.img.convert('LA').convert('RGB')
        self.img = ImageEnhance.Contrast(self.img).enhance(contrast)

    def save_to_file(self, file_name):
        self.img.save(file_name)

class App:

    def run(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--input', help='Input image file name', default='input.jpg')
        parser.add_argument('--output', help='Output image file name', default='output.jpg')
        parser.add_argument('--contrast', help='Contrast value', default=10)
        parser.add_argument('--dir', help='Input directory')
        parser.add_argument('--out', help='Output directory', default='out')
        args = parser.parse_args()

        if args.dir:
            self.process_directory(args.dir, args.out, args.contrast)
        else:
            self.process_file(args.input, args.output, args.contrast)

    def process_file(self, input_filename, output_filename, contrast):
        imgProcess = ImageProcessor()
        imgProcess.load_from_file(input_filename)
        imgProcess.process(contrast)
        imgProcess.save_to_file(output_filename)

    def process_directory(self, input_dir, output_dir, contrast):
        for filename in os.listdir(input_dir):
            input_filename = os.path.join(input_dir, filename)
            output_filename = os.path.join(output_dir, filename)
            self.process_file(input_filename, output_filename, contrast)

app = App()
app.run()