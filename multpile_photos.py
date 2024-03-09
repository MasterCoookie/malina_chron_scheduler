import time
from datetime import datetime
from argparse import ArgumentParser
from libcamera import controls
from picamera2 import Picamera2, Preview

print("Starting...")

# exposures = [1000, 5000, 10000, 20000, 50000, 100000, 200000, 500000, 1000000]
exposures = [1000000, 250000, 62500, 16000, 4000, 1000, 250, 80]

parser = ArgumentParser()
parser.add_argument("-f", "--file", dest="filename",
                    help="write report to FILE", metavar="FILE")
parser.add_argument("-e", "--exposure", dest="exposure",
                    help="exposure", metavar="EXPOSURE")
args = parser.parse_args()

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)


preview_config = picam2.create_still_configuration()
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

for i, exposure in enumerate(exposures):
    print(f"Capturing image {i} with exposure {exposure}")
    controls = {"AnalogueGain": 1.0, "ExposureTime": exposure}
    picam2.set_controls(controls)
    time.sleep(2)
    picam2.capture_file(f'{args.filename}_{datetime.now()}_index{i}_exposure{exposure}.jpg', wait=True)

print("Done")
picam2.stop()
picam2.stop_preview()
