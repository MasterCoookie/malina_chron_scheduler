import os
import ftplib
from secret import get_credentials

def upload_folder(folder_path: str):
    folder_name  = os.path.basename(folder_path)
    try:
        host, user, passwd = get_credentials()
        session = ftplib.FTP(host, user, passwd)
        folder_creation_code = session.mkd(folder_name)
        if folder_creation_code != folder_name:
            print(f'Folder created successfully. Response code: {folder_creation_code}')
        else:
            print(f'Folder creation failed. Response code: {folder_creation_code}')

        for file in os.listdir(folder_path):
            file_path = f'{folder_path}/{file}'
            if os.path.isfile(file_path):
                code = session.storbinary(f'STOR {folder_name}/{file}', open(file_path, 'rb'))
                if code.startswith('226'):
                    print(f'File uploaded successfully. Response code: {code}')
                else:
                    print(f'File upload failed. Response code: {code}')
    except ftplib.error_perm as e:
        print(f'FTP error: {e}')
    except Exception as e:
        print(f'Error: {e}')
