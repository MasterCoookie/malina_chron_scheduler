import time
from argparse import ArgumentParser
parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
parser.add_argument("-e", "--exposure", dest="exposure",
                    help="exposure", metavar="EXPOSURE")
args = parser.parse_args()
from libcamera import controls
from picamera2 import Picamera2, Preview

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)
controls = {"AnalogueGain": 1.0, "ExposureTime": int(args.exposure)}
preview_config = picam2.create_still_configuration(controls=controls)
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

picam2.capture_file(args.filename, wait=True)
