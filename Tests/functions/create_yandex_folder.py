import requests
import configparser


config = configparser.ConfigParser()
config.read('setting.ini')

token = config['YAN']['tokenYAN']


def create_directory(name_directory):
      # name_directory = input('Введите имя папки: ')
      headers = {
        'Content-Type': 'application/json',
        'Authorization': token
      }    
      params = {
        'path': name_directory
      }
      response = requests.put(url = 'https://cloud-api.yandex.net/v1/disk/resources', params=params, headers=headers)
      # result = response.get('href').split('%3A%2F')[1]    
      return response.status_code