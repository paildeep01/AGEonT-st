"""
Configuration settings for the AI-Powered Multilingual Research Article and News Insight System
"""
import os
from dotenv import load_dotenv

load_dotenv()

# Application Settings
APP_TITLE = "AGEonT-st: AI-Powered Article & News Insights"
APP_ICON = "🔍"

# Language Settings
DEFAULT_LANGUAGE = os.getenv("DEFAULT_LANGUAGE", "en")
SUPPORTED_LANGUAGES = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "it": "Italian",
    "pt": "Portuguese",
    "zh-cn": "Chinese (Simplified)",
    "ja": "Japanese",
    "ko": "Korean",
    "ar": "Arabic",
    "hi": "Hindi",
    "ru": "Russian"
}

# Summarization Settings
MAX_SUMMARY_LENGTH = int(os.getenv("MAX_SUMMARY_LENGTH", "150"))
MIN_SUMMARY_LENGTH = int(os.getenv("MIN_SUMMARY_LENGTH", "50"))

# Analysis Settings
SENTIMENT_THRESHOLD_POSITIVE = 0.1
SENTIMENT_THRESHOLD_NEGATIVE = -0.1

# Article Fetching Settings
REQUEST_TIMEOUT = 30
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
