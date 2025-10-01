"""
Summarizer Module
Handles text summarization using extractive methods
"""
from textblob import TextBlob
import nltk
from nltk.tokenize import sent_tokenize
from collections import defaultdict
import config


class TextSummarizer:
    """Summarize text using extractive summarization"""
    
    def __init__(self):
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('punkt', quiet=True)
    
    def extractive_summarize(self, text, num_sentences=3):
        """
        Create extractive summary by selecting most important sentences
        
        Args:
            text (str): Text to summarize
            num_sentences (int): Number of sentences in summary
            
        Returns:
            dict: Summary result
        """
        try:
            sentences = sent_tokenize(text)
            
            if len(sentences) <= num_sentences:
                return {
                    'success': True,
                    'summary': text,
                    'method': 'extractive',
                    'original_sentences': len(sentences),
                    'summary_sentences': len(sentences)
                }
            
            # Score sentences based on word frequency
            word_frequencies = self._calculate_word_frequencies(text)
            sentence_scores = self._score_sentences(sentences, word_frequencies)
            
            # Get top sentences
            top_sentences = sorted(
                sentence_scores.items(), 
                key=lambda x: x[1], 
                reverse=True
            )[:num_sentences]
            
            # Sort by original order
            top_sentences = sorted(top_sentences, key=lambda x: sentences.index(x[0]))
            
            summary = ' '.join([sentence for sentence, score in top_sentences])
            
            return {
                'success': True,
                'summary': summary,
                'method': 'extractive',
                'original_sentences': len(sentences),
                'summary_sentences': num_sentences
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': 'Summarization failed. Please try with different text.'
            }
    
    def _calculate_word_frequencies(self, text):
        """Calculate word frequencies for scoring"""
        blob = TextBlob(text.lower())
        words = [word for word in blob.words if word.isalnum() and len(word) > 2]
        
        word_freq = defaultdict(int)
        for word in words:
            word_freq[word] += 1
        
        # Normalize frequencies
        max_freq = max(word_freq.values()) if word_freq else 1
        for word in word_freq:
            word_freq[word] = word_freq[word] / max_freq
        
        return word_freq
    
    def _score_sentences(self, sentences, word_frequencies):
        """Score sentences based on word frequencies"""
        sentence_scores = {}
        
        for sentence in sentences:
            blob = TextBlob(sentence.lower())
            words = [word for word in blob.words if word.isalnum()]
            
            score = 0
            for word in words:
                if word in word_frequencies:
                    score += word_frequencies[word]
            
            # Normalize by sentence length to avoid bias toward longer sentences
            if len(words) > 0:
                sentence_scores[sentence] = score / len(words)
            else:
                sentence_scores[sentence] = 0
        
        return sentence_scores
    
    def bullet_point_summary(self, text, num_points=5):
        """
        Create bullet point summary
        
        Args:
            text (str): Text to summarize
            num_points (int): Number of bullet points
            
        Returns:
            list: Bullet points
        """
        result = self.extractive_summarize(text, num_points)
        
        if result['success']:
            sentences = sent_tokenize(result['summary'])
            return ['• ' + sentence.strip() for sentence in sentences]
        else:
            return []
