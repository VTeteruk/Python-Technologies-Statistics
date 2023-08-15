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


def parse_page_number(soup: BeautifulSoup) -> int:
    number = int(soup.select("li.page-item > a.page-link")[-2].text)
    return number if number else 0


def parse_vacancies_references(soup: BeautifulSoup) -> list:
    return [reference["href"] for reference in soup.select("a.profile")]


def parse_detailed_vacancy(soup: BeautifulSoup) -> BeautifulSoup:
    return soup.select_one("div.mb-4")


def calculate_technologies(soup: BeautifulSoup) -> None:
    for technology in config.TECHNOLOGIES:
        if re.findall(f" +{technology.lower()}", soup.get_text().lower()):
            RESULTS[technology] += 1
            continue


def combine_data() -> None:
    RESULTS["JavaScript"] += RESULTS["JS"]
    del RESULTS["JS"]


def write_to_csv(data: dict) -> None:
    with open("py-technologies.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(("Technology", "Value"))
        for technology, value in data.items():
            writer.writerow((technology, value))


def main(url: str) -> None:
    for number in range(1, parse_page_number(create_soup(url)) + 1):
        logging.info(f"Parsing page #{number}")
        vacancies_references = parse_vacancies_references(create_soup(url + f"&page={number}"))
        for reference in vacancies_references:
            logging.info(reference)
            parsed_soup = parse_detailed_vacancy(
                create_soup(urljoin(config.DJINNI_HOME_URL, reference))
            )
            calculate_technologies(parsed_soup)

    combine_data()
    write_to_csv(RESULTS)


if __name__ == "__main__":
    main(config.DJINNI_PYTHON_JOBS_URL)
