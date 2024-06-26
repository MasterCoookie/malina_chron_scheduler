import os
import json
import pathlib
import logging
from datetime import datetime

from ftp_sender import upload_folder

logger = logging.getLogger(__name__)
logging.basicConfig(filename="timelapse.log", level=logging.INFO)

logger.info("Starting...")

try:
    script_folder = pathlib.Path(__file__).parent.resolve()

    exposures = json.load(open(os.path.join(script_folder, 'exposures.json'))).get('exposures')
    logger.info(f"Taking {len(exposures)} pictures with exposures: {exposures}")

    dirname = os.path.join("/home/pi/malina_chron_scheduler", f'testy_cron_{datetime.now().strftime("%Y-%m-%d_%H:%M:%S")}')
    os.mkdir(dirname)

    for i, exposure in enumerate(exposures):
        logger.info(f"Taking picture {i+1}/{len(exposures)} with exposure {exposure}...")
        file_path = os.path.join(dirname, f"dupa_text_{i}_{exposure}.jpg")
        os.system(f'libcamera-still -n -o {file_path} --gain 1.0 --shutter {exposure}')

    logger.info("Done taking pictures")
    logger.info("Uploading to FTP...")
    upload_folder(dirname)
except Exception as e:
    logger.error(f"Error: {e}")
    print(f"Error: {e}")
    exit(1)

logger.info("Finished")
