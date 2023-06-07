from variables import *
from ftp_env  import *
import pysftp

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None  # Disable hostkey checking

def sftp(local_path, name_file) -> bool:
  print('Local:' , local_path)
  print('Remote:', remote_path + name_file)
  try:
    with pysftp.Connection(host=sftp_host, username=sftp_username, password=sftp_password, cnopts=cnopts) as sftp:
      print('Connect ok', sftp_host)
      sftp.put(local_path, remote_path + name_file)
      sftp.close()
    return True
  except Exception as e:
    print('Error', e)
    return False
