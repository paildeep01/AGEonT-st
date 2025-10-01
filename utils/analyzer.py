"""
Analyzer Module
Handles sentiment analysis and content analysis
"""
from textblob import TextBlob
import nltk
from collections import Counter
import re
import config

# Ensure NLTK data is available
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt', quiet=True)

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords', quiet=True)

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


class ContentAnalyzer:
    """Analyze article content for sentiment and insights"""
    
    def __init__(self):
        try:
            self.stop_words = set(stopwords.words('english'))
        except:
            self.stop_words = set()
    
    def analyze_sentiment(self, text):
        """
        Analyze sentiment of text
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Sentiment analysis results
        """
        try:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            subjectivity = blob.sentiment.subjectivity
            
            # Determine sentiment category
            if polarity > config.SENTIMENT_THRESHOLD_POSITIVE:
                sentiment = "Positive"
            elif polarity < config.SENTIMENT_THRESHOLD_NEGATIVE:
                sentiment = "Negative"
            else:
                sentiment = "Neutral"
            
            return {
                'success': True,
                'sentiment': sentiment,
                'polarity': polarity,
                'subjectivity': subjectivity,
                'polarity_percentage': (polarity + 1) * 50,
                'subjectivity_percentage': subjectivity * 100
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def extract_keywords(self, text, top_n=10):
        """
        Extract top keywords from text
        
        Args:
            text (str): Text to analyze
            top_n (int): Number of top keywords to return
            
        Returns:
            list: Top keywords with frequencies
        """
        try:
            # Tokenize and clean
            words = word_tokenize(text.lower())
            
            # Filter words
            words = [
                word for word in words 
                if word.isalnum() 
                and len(word) > 3 
                and word not in self.stop_words
            ]
            
            # Count frequencies
            word_freq = Counter(words)
            
            return word_freq.most_common(top_n)
        except Exception as e:
            return []
    
    def get_text_statistics(self, text):
        """
        Get basic statistics about the text
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Text statistics
        """
        try:
            sentences = sent_tokenize(text)
            words = word_tokenize(text)
            
            # Count words (excluding punctuation)
            word_count = len([w for w in words if w.isalnum()])
            
            # Average sentence length
            avg_sentence_length = word_count / len(sentences) if sentences else 0
            
            # Reading time (assuming 200 words per minute)
            reading_time = word_count / 200
            
            return {
                'success': True,
                'word_count': word_count,
                'sentence_count': len(sentences),
                'character_count': len(text),
                'avg_sentence_length': round(avg_sentence_length, 1),
                'reading_time_minutes': round(reading_time, 1)
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def analyze_sentence_sentiments(self, text):
        """
        Analyze sentiment for each sentence
        
        Args:
            text (str): Text to analyze
            
        Returns:
            list: Sentiment scores for each sentence
        """
        try:
            sentences = sent_tokenize(text)
            sentiments = []
            
            for sentence in sentences:
                blob = TextBlob(sentence)
                sentiments.append({
                    'sentence': sentence[:100] + '...' if len(sentence) > 100 else sentence,
                    'polarity': blob.sentiment.polarity
                })
            
            return sentiments
        except Exception as e:
            return []
