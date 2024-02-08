from ftplib import FTP

from loguru import logger


class FtpReceiver:
    server_ip = '192.168.1.2'
    username = 'esset'
    password = '0000'

    def __init__(self):
        self.ftp = FTP(self.server_ip)
        self.ftp.login(self.username, self.password)

    def receive_file_via_ftp(self, local_file_path, remote_file_path):
        try:
            with open(local_file_path, 'wb') as file:
                self.ftp.cwd('files')
                self.ftp.retrbinary(f'RETR {remote_file_path}', file.write)
            logger.success(f"File '{remote_file_path}' downloaded successfully to '{local_file_path}'.")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
        finally:
            self.ftp.quit()
