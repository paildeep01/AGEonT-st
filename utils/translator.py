"""
Translator Module
Handles multilingual translation
"""
from googletrans import Translator as GoogleTranslator
import config


class Translator:
    """Translate text between languages"""
    
    def __init__(self):
        self.translator = GoogleTranslator()
    
    def translate_text(self, text, target_language='en', source_language='auto'):
        """
        Translate text to target language
        
        Args:
            text (str): Text to translate
            target_language (str): Target language code
            source_language (str): Source language code (auto-detect if 'auto')
            
        Returns:
            dict: Translation result with translated text and detected language
        """
        try:
            if not text or text.strip() == '':
                return {
                    'success': False,
                    'error': 'Empty text provided'
                }
            
            # Translate text
            result = self.translator.translate(
                text, 
                dest=target_language, 
                src=source_language
            )
            
            return {
                'success': True,
                'translated_text': result.text,
                'source_language': result.src,
                'target_language': target_language,
                'original_text': text
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'message': 'Translation failed. The text might be too long or the service is unavailable.'
            }
    
    def detect_language(self, text):
        """
        Detect the language of text
        
        Args:
            text (str): Text to analyze
            
        Returns:
            dict: Detected language info
        """
        try:
            detection = self.translator.detect(text)
            
            language_name = config.SUPPORTED_LANGUAGES.get(
                detection.lang, 
                detection.lang.upper()
            )
            
            return {
                'success': True,
                'language_code': detection.lang,
                'language_name': language_name,
                'confidence': detection.confidence
            }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
