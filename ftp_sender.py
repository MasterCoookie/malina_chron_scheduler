import ftplib
from secret import get_credentials

host, user, passwd = get_credentials()
session = ftplib.FTP(host, user, passwd)
file = open('jajo.png', 'rb')
session.storbinary('STOR jajo.png', file)
file.close()
session.quit()
