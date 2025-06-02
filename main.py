import streamlit as st
from scrape import scrape_website
from scrape import extract_body_content, clean_body_content, split_dom_content
from parse import parse_with_ollama

st.title("Web Scraper")
url = st.text_input("Enter the URL to scrape:")

if st.button("Scrape"):
    print("Button clicked, starting scrape...")
    st.write("Scraping the website...")

    result = scrape_website(url)
    body_content = extract_body_content(result)
    cleaned_content = clean_body_content(body_content)

    st.session_state.dom_content = cleaned_content

    with st.expander("View DOM Content"):
        st.text_area("DOM Content", value=cleaned_content, height=300)

# Step 2: Ask Questions About the DOM Content
if "dom_content" in st.session_state:
    parse_description = st.text_area("Describe what you want to parse")

    if st.button("Parse Content"):
        if parse_description:
            st.write("Parsing the content...")

            # Parse the content with Ollama
            dom_chunks = split_dom_content(st.session_state.dom_content)
            parsed_result = parse_with_ollama(dom_chunks, parse_description)
            st.write(parsed_result)