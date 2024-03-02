import ftplib
from secret import get_credentials

try:
    host, user, passwd = get_credentials()
    session = ftplib.FTP(host, user, passwd)
    file = open('jajo2.png', 'rb')
    code = session.storbinary('STOR jajo.png', file)
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
