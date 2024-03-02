import ftplib
from secret import get_credentials

try:
    host, user, passwd = get_credentials()
    session = ftplib.FTP(host, user, passwd)
    file = open('jajo2.png', 'rb')

    folder_creation_code = session.mkd('floder_na_cam')
    if folder_creation_code.startswith('257'):
        print(f'Folder created successfully. Response code: {folder_creation_code}')
    else:
        print(f'Folder creation failed. Response code: {folder_creation_code}')
        # raise exception here

    code = session.storbinary('STOR floder_na_cam/jajo.png', file)
    if code.startswith('226'):
        print(f'File uploaded successfully. Response code: {code}')
    else:
        print(f'File upload failed. Response code: {code}')
        # raise exception here
    file.close()
    session.quit()
except ftplib.error_perm as e:
    print(f'FTP error: {e}')
except Exception as e:
    print(f'Error: {e}')
