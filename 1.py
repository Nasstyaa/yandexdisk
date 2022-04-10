import requests
import pathlib

class YaUploader:
    token = ''
    def __init__(self, file_path):
        self.file_path = file_path
    def upload(self):
        url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)}
        params = {'path': 'disk',
                  'overwrite': 'true'}
        upload_link = requests.get(url, headers=headers, params=params).json()['href']
        res = requests.put(upload_link, data=open(self.file_path, 'rb'))


if __name__ == "__main__":
    uploader = YaUploader('C:\\yandexdisk\1.txt')
