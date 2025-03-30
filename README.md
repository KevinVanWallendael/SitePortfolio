# Streamlit Portfolio Website

This repository contains the code for my personal portfolio website, built using Streamlit. It showcases my projects, skills, and provides a way for visitors to learn more about my work.

## Table of Contents

* [Introduction](#introduction)
* [Features](#features)
* [Project Structure](#project-structure)
* [Setup and Installation](#setup-and-installation)
* [Usage](#usage)
* [Contact](#contact)

## Introduction

This website serves as my online portfolio, highlighting my experience and skills as a Business Intelligence Engineer. It includes information about my background, skills, and showcases some of my projects. The site is built with Streamlit, a Python library that makes it easy to create interactive web applications for data science.

## Features

The portfolio website includes the following key features:

* **About Me:** A detailed overview of my professional background, skills, and interests.
* **Portfolio Analysis:** An interactive tool for analyzing stock portfolios, including performance metrics, visualizations, and buy/sell recommendations.
* **Chatbot Assistant:** (Description to be added)
* **Housing Project:** A tool to predict housing prices in Warsaw based on various features.
* **Blog:** Articles discussing my projects, technologies, and insights.

## Project Structure

The project is organized as follows:

```
├── README.md         # This file
├── app.py            # Main Streamlit application
├── pages/            # Directory containing individual page scripts
│   ├── about_me.py   # About Me page
│   ├── assistant.py  # Chatbot Assistant page
│   ├── blog.py       # Blog page
│   ├── housing_project.py # Housing Project page
│   └── portfolio_analysis.py # Portfolio Analysis page
├── assets/           # Directory for images and other static assets
│   ├── profile-pic.png
│   ├── StockPortfolio.jpg
│   ├── OtoDom.jpg
│   ├── PredictionModel.jpg
│   ├── StockFlow.png
└── models/           # Directory for machine learning models (Housing Project)
├── housing_price_predictor_model.pkl
└── preprocessor.pkl
```

## Setup and Installation

1.  **Clone the repository:**

    ```bash
    git clone 
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **ChromeDriver (If needed for web scraping):**

    * If your project uses web scraping (like the Housing Project), you may need to install ChromeDriver. Download the correct version for your Chrome browser from the [ChromeDriver website](https://chromedriver.chromium.org/downloads) and place it in a directory accessible to your system's PATH.

## Usage

To run the Streamlit application:

```bash
streamlit run app.py
```

This will start the Streamlit server, and you can view the website in your browser at http://localhost:8501.

Contact
Name: Kevin Van Wallendael
[LinkedIn](https://www.linkedin.com/in/kevin-van-wallendael/)
[GitHub](https://github.com/KevinVanWallendael)