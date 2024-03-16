import time
import os
import json
import pathlib
from datetime import datetime
from argparse import ArgumentParser
from libcamera import controls
from picamera2 import Picamera2, Preview

from ftp_sender import upload_folder

script_folder = pathlib.Path(__file__).parent.resolve()

print("Starting...")

exposures = json.load(open(os.path.join(script_folder, 'exposures.json'))).get('exposures')
print(f"Taking {len(exposures)} pictures with exposures:", exposures)

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
args = parser.parse_args()

picam2 = Picamera2()
# picam2.start_preview(Preview.QTGL)


preview_config = picam2.create_still_configuration()
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

dirname = os.path.join(script_folder, f'{args.filename}_{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
os.mkdir(dirname)

for i, exposure in enumerate(exposures):
    print(f"Capturing image {i} with exposure {exposure}")
    controls = {"AnalogueGain": 1.0, "ExposureTime": exposure}
    picam2.set_controls(controls)
    time.sleep(2)
    picam2.capture_file(f'{dirname}/index{i}_exposure{exposure}.jpg', wait=True)

print("Done")
picam2.stop()
picam2.stop_preview()

print("Uploading to FTP...")
upload_folder(dirname)
