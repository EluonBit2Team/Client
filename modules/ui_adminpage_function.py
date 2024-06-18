import sys
import requests
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class GrafanaAPI:
    def __init__(self, api_url, api_key):
        self.api_url = api_url
        self.api_key = api_key

    def get_data(self, query):
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }
        response = requests.get(f'{self.api_url}/api/datasources/proxy/1/query', headers=headers, params={'query': query})
        response.raise_for_status()
        return response.json()


class GrafanaDataWindow(QMainWindow):
    def __init__(self, main_window, api_url, api_key):
        super().__init__()

        self.main_window = main_window
        self.api = GrafanaAPI(api_url, api_key)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Grafana Data Viewer')
        self.setGeometry(100, 100, 800, 600)

        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.show_data()

    def show_data(self):
        try:
            data = self.api.get_data('your_query_here')
            self.text_edit.setText(str(data))
        except Exception as e:
            self.text_edit.setText(f'Error fetching data: {e}')


