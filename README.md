<h1 align="center">👨‍💻 AI_Web_Scrapper</h1>
<h3 align="center">A Streamlit-powered smart web scraper that extracts specific data using natural language and Ollama LLM</h3>

---

- 💡 **What it does**: Scrapes any webpage, cleans the DOM, and extracts exactly what you ask using AI  
- 🔧 **Built with**: Python, Streamlit, Selenium, BeautifulSoup, LangChain, Ollama  
- 🧠 **Powered by**: Local LLM via Ollama & LangChain for intelligent content parsing  
- 📦 **Handles large pages** by chunking content for efficient processing  

---

<h3 align="left">🛠️ Tech Stack:</h3>

- 🐍 Python  
- 🌐 Streamlit  
- 🤖 Selenium + Edge WebDriver  
- 🧹 BeautifulSoup (for DOM cleaning)  
- 🧠 LangChain + Ollama LLM  

---

<h3 align="left">🚀 How to Use:</h3>

```bash
# Clone the repo
git clone https://github.com/yourusername/AI_Web_Scrapper.git
cd AI_Web_Scrapper

# Install dependencies
pip install -r requirements.txt

# Download Edge WebDriver (msedgedriver.exe) and ensure driver and brower have same version

# Run the app
streamlit run main.py
