
import requests
from bs4 import BeautifulSoup

from app.models import Document, SessionLocal

def scrape_news():
    session = SessionLocal()
    url = "https://news.ycombinator.com/"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("span", class_="titleline")  # Updated class for articles

    if not articles:
        print("No articles found on the page.")
        return

    for article in articles:
        article_text = article.get_text()
        print(f"Scraped Article: {article_text}")  # Debug: Print the article text
        new_doc = Document(text=article_text)

        session.add(new_doc)
        print(f"Added to session: {article_text}")  # Debug: Confirm it's added to the session
    
    session.commit()
    print("All articles committed to the database.")  # Debug: Confirm the commit
