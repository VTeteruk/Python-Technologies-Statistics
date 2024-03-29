import logging
import os.path
from datetime import datetime

import pandas as pd
from matplotlib import pyplot as plt

import config
from parser.parser import main

logging.basicConfig(
    level=logging.INFO
)


def get_data_from_csv_file() -> pd.DataFrame:
    if not os.path.exists("py-technologies.csv"):
        logging.info("Creating a data file...")
        main(config.DJINNI_PYTHON_JOBS_URL)

    last_updated_time = datetime.fromtimestamp(os.stat("py-technologies.csv").st_mtime)
    if (datetime.now() - last_updated_time).total_seconds() > config.TIME_WHEN_UPDATE_FILE:
        logging.info("Data is outdated\nUpdating the data...")
        main(config.DJINNI_PYTHON_JOBS_URL)

    return pd.read_csv("py-technologies.csv").sort_values("Value", ascending=False)


def save_plot() -> None:
    plt.savefig(
        os.path.join("plots", f"output_plot_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png")
    )


def create_plot() -> None:
    df = get_data_from_csv_file()
    colors = ["red" if value > df["Value"].mean() else "blue" for value in df["Value"]]

    plt.figure(figsize=(12, 6))
    plt.bar(df["Technology"], df["Value"], color=colors, width=0.4)
    plt.xticks(rotation=90)
    plt.title("Python technologies according to djinni vacancies")
    plt.xlabel("Technologies")
    plt.ylabel("Value")
    plt.tight_layout()

    save_plot()

    plt.show()
    plt.close()


if __name__ == "__main__":
    create_plot()
