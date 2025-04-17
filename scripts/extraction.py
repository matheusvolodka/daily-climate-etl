import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import json
from urllib.parse import quote

load_dotenv('credentials.env')


class ClimateExtractor:
    def __init__(self, city_name):
        self.city_name = city_name
        self.city_url = quote(city_name)
        self.date = datetime.today().strftime('%Y-%m-%d')
        self.api_key = os.getenv('API_KEY')
        self.data = None
        self.directory = None

    def ext_data(self):
        base_url = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'
        endpoint = f'{base_url}{self.city_url}/today?unitGroup=metric&key={self.api_key}'

        try:
            response = requests.get(endpoint)
            response.raise_for_status()
            self.data = response.json()
            print("Dados extraídos com sucesso.")
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
            self.data = None

    def create_directory(self):
        self.directory = f'../data/daily_climate_{self.date}/{self.city_name}'
        os.makedirs(self.directory, exist_ok=True)
        print(f"Diretório criado: {self.directory}")

    def save_data(self):
        if self.data:
            filename = f'{self.directory}/daily_data_{self.city_name}_{self.date}.json'
            with open(filename, 'w') as file:
                json.dump(self.data, file, indent=4)
            print(f"Dados salvos com sucesso em: {filename}")
        else:
            print("Nenhum dado para salvar.")

    def run(self):
        self.ext_data()
        self.create_directory()
        self.save_data()


if __name__ == '__main__':
    extractor = ClimateExtractor("London")
    extractor.run()
