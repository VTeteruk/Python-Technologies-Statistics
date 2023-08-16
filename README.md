# Python Technologies Analysis from Djinni Job Vacancies

This project focuses on analyzing Python-related technologies in job vacancies listed on Djinni.co,
a popular job board. The script scrapes job vacancy data, counts the occurrences of various
technologies, and creates a CSV file for further analysis. The analysis is visualized using
matplotlib.
___

## Project Structure

* config.py: Configuration file containing URL constants and other settings.
* parser/parser.py: Script responsible for web scraping and data parsing.
* main.py: Main script that orchestrates the scraping, data processing, and visualization.
* py-technologies.csv: CSV file containing technology occurrence data.
* README.md: This documentation file.

## Requirements

`Python 3.x`
___

## Usage

1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Install the required libraries using `pip install -r requirements.txt`.
4. Run the `analysis.py` script to perform web scraping, data analysis, and visualization.
5. The script will create/update py-technologies.csv and display a bar chart showing the
   distribution of technologies.

___

## Configuration

`config.py`: Modify this file to update URLs, technologies, and other settings.

## Output

The script outputs a bar chart that visualizes the distribution of Python technologies based on job
vacancies from Djinni.co. Each technology is represented by a bar, with its height indicating the
number of occurrences in the job vacancies.
