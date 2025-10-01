# Quick Start Guide

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/paildeep01/AGEonT-st.git
   cd AGEonT-st
   ```

2. **Set up Python virtual environment (recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Run the setup script:**
   ```bash
   python setup.py
   ```
   
   Or manually install:
   ```bash
   pip install -r requirements.txt
   python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
   ```

## Running the Application

Start the Streamlit application:
```bash
streamlit run app.py
```

The application will automatically open in your browser at `http://localhost:8501`.

## Basic Usage

### Analyzing a News Article from URL

1. Select **URL** as input method in the sidebar
2. Paste the article URL (e.g., `https://www.bbc.com/news/article-example`)
3. Click **Fetch Article**
4. Choose your analysis options in the sidebar:
   - Translation (if needed)
   - Sentiment Analysis
   - Summarization
   - Keywords
   - Statistics
5. Click **Analyze Article**
6. View results in different tabs

### Analyzing Text Directly

1. Select **Text** as input method
2. Paste or type your article text
3. Optionally add a title
4. Configure analysis options
5. Click **Analyze Article**

## Features Walkthrough

### 1. Language Detection & Translation
- Automatically detects the source language
- Translate to 12+ languages including English, Spanish, French, German, Chinese, etc.

### 2. Sentiment Analysis
- Overall sentiment (Positive/Neutral/Negative)
- Polarity score (-1 to +1)
- Subjectivity score (0 to 1)
- Sentence-level sentiment tracking

### 3. Summarization
- Extractive summarization
- Adjustable summary length (1-10 sentences)
- Bullet point format for key points

### 4. Keyword Extraction
- Top 15 keywords by frequency
- Visual representation with bar charts
- Filtered to remove common stop words

### 5. Text Statistics
- Word count, sentence count
- Average sentence length
- Estimated reading time
- Character count

## Example Workflows

### Academic Research Analysis
```
Input: Research paper abstract or full text
Options: 
  - Summarization (5 sentences)
  - Keywords
  - Statistics
Output: Quick overview, key terms, and metrics
```

### News Sentiment Tracking
```
Input: News article URL
Options:
  - Sentiment Analysis
  - Summarization
Output: Sentiment gauge, summary, emotional tone
```

### Multilingual Content Review
```
Input: Article in Spanish/French/etc.
Options:
  - Translation to English
  - Sentiment Analysis
  - Keywords
Output: Translated text with analysis
```

## Tips

- For best results, use complete articles (not just headlines)
- Longer texts (500+ words) provide better insights
- Try different summary lengths to find the right detail level
- Use translation for articles in foreign languages before analysis
- Keywords work best with domain-specific content

## Troubleshooting

**Issue: Article fetch fails**
- Check URL is accessible
- Try pasting text directly instead
- Some websites may block automated fetching

**Issue: Translation errors**
- Service may have rate limits
- Try smaller text chunks
- Check internet connectivity

**Issue: Slow analysis**
- First run may be slower (downloading models)
- Longer texts take more time
- Close other applications to free resources

## Advanced Usage

### Custom Configuration
Create a `.env` file:
```
DEFAULT_LANGUAGE=en
MAX_SUMMARY_LENGTH=200
MIN_SUMMARY_LENGTH=75
```

### Batch Processing
For analyzing multiple articles, run the utilities directly:
```python
from utils import ArticleFetcher, ContentAnalyzer

fetcher = ArticleFetcher()
analyzer = ContentAnalyzer()

urls = ['url1', 'url2', 'url3']
for url in urls:
    article = fetcher.fetch_from_url(url)
    sentiment = analyzer.analyze_sentiment(article['text'])
    print(f"{article['title']}: {sentiment['sentiment']}")
```

## Next Steps

- Explore all analysis options
- Try different languages
- Experiment with summary lengths
- Export results for reports
- Integrate with your workflow

For more information, see the main [README.md](README.md).
