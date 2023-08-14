import csv
import logging
import re
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup
import config

RESULTS = dict.fromkeys(config.TECHNOLOGIES, 0)

logging.basicConfig(
    level=logging.INFO
)


def create_soup(url: str) -> BeautifulSoup:
    page = requests.get(url).content
    return BeautifulSoup(page, "html.parser")
