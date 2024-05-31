import os
import json
import pathlib
from datetime import datetime

from ftp_sender import upload_folder

script_folder = pathlib.Path(__file__).parent.resolve()

print("Starting...")

exposures = json.load(open(os.path.join(script_folder, 'exposures.json'))).get('exposures')
print(f"Taking {len(exposures)} pictures with exposures:", exposures)

dirname = os.path.join(script_folder, f'testy_cmd_{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
os.mkdir(dirname)

for i, exposure in enumerate(exposures):
    print(f"Taking picture {i+1}/{len(exposures)} with exposure {exposure}...")
    os.system(f"libcamera-still -t 5000 -n -o dupa_text_{i}_{exposure}.jpg --gain 1.0 --shutter {exposure}")

print("Done")
print("Uploading to FTP...")
upload_folder(dirname)
