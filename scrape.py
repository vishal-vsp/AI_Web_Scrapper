import selenium.webdriver as webdriver
from selenium.webdriver.edge.service import Service
import time
from bs4 import BeautifulSoup

def scrape_website(website):
    print("Launching web scraper...")

    chrome_driver_path = "./msedgedriver.exe"  # Ensure this path is correct for your system
    opions = webdriver.EdgeOptions()
    driver = webdriver.Edge(service=Service(chrome_driver_path), options=opions)

    try:
        driver.get(website)
        print("Page Loaded...")
        html = driver.page_source
        time.sleep(10)  # Wait for the page to load completely

        return html
    finally:
        driver.quit()
        print("Web scraper closed.")

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    body_content = soup.find('body')
    if body_content: 
        return body_content.get_text(strip=True)
    return "No body content found."
    
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, 'html.parser')
    for script in soup(["script", "style"]):
        script.decompose()      # Remove script and style elements. Can also use .extract() to remove them

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())
    return cleaned_content
    
def split_dom_content(dom_content, max_length=6000):
    return [dom_content[i:i + max_length] for i in range(0, len(dom_content), max_length)]