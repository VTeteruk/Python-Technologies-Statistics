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


def parse_page_number(soup: BeautifulSoup):
    number = int(soup.select("li.page-item > a.page-link")[-2].text)
    return number if number else 0


def parse_vacancies_references(soup: BeautifulSoup) -> list:
    return [reference["href"] for reference in soup.select("a.profile")]


def parse_detailed_vacancy(soup: BeautifulSoup):
    return soup.select_one("div.mb-4")
