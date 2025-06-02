# AI_Web_Scrapper
Web Scraper & Content Parser
This project is a Streamlit-based web application that allows users to scrape the content of any website, view the cleaned DOM content, and extract specific information using natural language instructions powered by an Ollama LLM.

Features
  Web Scraping: Enter any URL and retrieve the full HTML content using Selenium and Edge WebDriver.
  Content Cleaning: Automatically extracts and cleans the <body> content, removing scripts and styles for easier parsing.
  Interactive UI: View and inspect the cleaned DOM content directly in the app.
  Natural Language Parsing: Describe what you want to extract, and the app uses an LLM (via LangChain and Ollama) to parse and return only the requested data.
  Chunked Processing: Handles large DOMs by splitting content into manageable chunks for efficient parsing.

Tech Stack
  Python
  Streamlit
  Selenium
  BeautifulSoup
  LangChain & Ollama LLM

Usage
  Install dependencies from requirements.txt.
  Download the correct Edge WebDriver (msedgedriver.exe) for your system.
  Run the app with: streamlit run main.py
  Enter a URL, scrape the site, and describe what you want to extract!
