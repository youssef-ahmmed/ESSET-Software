from ftplib import FTP

from loguru import logger


class WifiSender:
    server_ip = '192.168.1.2'
    username = 'esset'
    password = '0000'

    def __init__(self):
        self.ftp = FTP(self.server_ip)
        self.ftp.login(self.username, self.password)

    def send_file_via_ftp(self, local_file_path, remote_file_path):
        try:
            with open(local_file_path, 'rb') as file:
                self.ftp.cwd('files')
                self.ftp.storbinary(f'STOR {remote_file_path}', file)
            logger.success(f"File '{local_file_path}' uploaded successfully to '{remote_file_path}' on the server.")
        except Exception as e:
            logger.error(f"An error occurred: {e}")
        finally:
            self.ftp.quit()
