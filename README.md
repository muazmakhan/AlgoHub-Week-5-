**Web Scraping & File Automation**

## Overview

This repository contains two Python projects developed as part of my **Python Internship at AlgoHub UET Mardan**. The projects focus on **web scraping** and **task automation**, demonstrating practical applications of Python for data collection and file management.

## Projects

### 1. GitHub Web Scraper

A Python script that scrapes information from GitHub using the `requests` and `BeautifulSoup` libraries. The script sends HTTP requests, parses HTML content, extracts useful data using CSS selectors, and stores the extracted information in a structured format.

#### Features

* Sends HTTP requests to GitHub
* Parses HTML using BeautifulSoup
* Extracts relevant information
* Saves scraped data to a file
* Includes basic exception handling

### 2. File Organizer

A Python automation script that organizes files into categorized folders based on their file extensions. It automatically creates folders when needed and moves files to their appropriate locations.

#### Features

* Organizes files by extension
* Creates folders automatically
* Supports Images, Documents, Videos, Audio, and more
* Uses Python's `os` and `shutil` modules
* Simple and beginner-friendly implementation

## Technologies Used

* Python 3
* Requests
* BeautifulSoup4
* OS Module
* Shutil Module

## Installation

1. Clone the repository:

```bash
git clone https://github.com/muazmakhan/Web-Scraping-and-File-Automation.git
```

2. Navigate to the project directory:

```bash
cd Web-Scraping-and-File-Automation
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

## Project Structure

```text
Week5-WebScraping-Automation/
│
├── github_scraper/
│   ├── scraper.py
│   ├── output.txt
│   ├── requirements.txt
│   └── README.md
│
├── file_organizer/
│   ├── organizer.py
│   └── sample_files/
│
└── README.md
```

## Learning Outcomes

Through these projects, I learned to:

* Perform web scraping using Requests and BeautifulSoup.
* Parse HTML and extract information using CSS selectors.
* Automate repetitive tasks with Python.
* Organize files programmatically.
* Write clean, modular, and reusable Python code.

## Future Improvements

* Export scraped data to CSV and JSON.
* Add support for scheduled execution.
* Enhance the file organizer with additional file categories.
* Build a graphical user interface (GUI).


## License

This project is developed for educational and learning purposes as part of the AlgoHub Python Internship.
