"""
Article Fetcher Module
Handles fetching and parsing articles from URLs
"""
import requests
from bs4 import BeautifulSoup
from newspaper import Article
import config


class ArticleFetcher:
    """Fetch and parse articles from URLs"""
    
    def __init__(self):
        self.headers = {
            'User-Agent': config.USER_AGENT
        }
    
    def fetch_from_url(self, url):
        """
        Fetch article content from URL
        
        Args:
            url (str): Article URL
            
        Returns:
            dict: Article data including title, text, authors, publish_date
        """
        try:
            article = Article(url)
            article.download()
            article.parse()
            
            return {
                'success': True,
                'title': article.title,
                'text': article.text,
                'authors': article.authors,
                'publish_date': article.publish_date,
                'top_image': article.top_image,
                'url': url
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': 'Failed to fetch article. Please check the URL or try pasting the text directly.'
            }
    
    def extract_text_from_html(self, html_content):
        """
        Extract text from HTML content
        
        Args:
            html_content (str): HTML content
            
        Returns:
            str: Extracted text
        """
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            # Remove script and style elements
            for script in soup(["script", "style"]):
                script.extract()
            
            # Get text
            text = soup.get_text()
            
            # Clean up whitespace
            lines = (line.strip() for line in text.splitlines())
            chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
            text = ' '.join(chunk for chunk in chunks if chunk)
            
            return text
        except Exception as e:
            raise Exception(f"Failed to extract text from HTML: {str(e)}")
