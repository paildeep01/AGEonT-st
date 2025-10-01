# Usage Guide and Examples

## Table of Contents
1. [Getting Started](#getting-started)
2. [Using the Web Interface](#using-the-web-interface)
3. [Programmatic Usage](#programmatic-usage)
4. [Advanced Features](#advanced-features)
5. [Common Use Cases](#common-use-cases)
6. [Tips and Best Practices](#tips-and-best-practices)

## Getting Started

### First Time Setup

```bash
# Clone and navigate to the project
git clone https://github.com/paildeep01/AGEonT-st.git
cd AGEonT-st

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"

# Run the application
streamlit run app.py
```

## Using the Web Interface

### Example 1: Analyzing a News Article

**Scenario**: You want to quickly understand the sentiment and key points of a news article.

**Steps**:
1. Open the application at `http://localhost:8501`
2. In the sidebar, keep **URL** selected
3. Paste article URL: `https://www.example.com/news/ai-breakthrough`
4. Click **Fetch Article**
5. In sidebar, select analysis options:
   - ☑ Sentiment Analysis
   - ☑ Summarization
   - ☑ Keywords
6. Set Summary Sentences to **3**
7. Click **Analyze Article**
8. View results in tabs:
   - **Summary**: Read the 3-sentence condensed version
   - **Sentiment**: See if the article is positive/negative
   - **Keywords**: Identify main topics

### Example 2: Translating and Analyzing Foreign Content

**Scenario**: You have a Spanish article and want English analysis.

**Steps**:
1. Select **Text** as input method
2. Paste Spanish article text
3. In sidebar:
   - Target Language: **English**
   - Analysis Options: ☑ Translation, ☑ Sentiment, ☑ Summary
4. Click **Analyze Article**
5. View:
   - **Summary**: English summary
   - **Detailed**: Full translation

### Example 3: Research Paper Analysis

**Scenario**: Extracting key insights from an academic paper.

**Steps**:
1. Input method: **Text**
2. Paste abstract or full paper
3. Analysis options: All selected
4. Summary Sentences: **5** (for more detail)
5. Review:
   - **Keywords**: Research themes
   - **Statistics**: Paper length and complexity
   - **Summary**: Main contributions

## Programmatic Usage

### Example 1: Batch Sentiment Analysis

Analyze sentiment across multiple articles:

```python
from utils import ContentAnalyzer

analyzer = ContentAnalyzer()

articles = [
    "AI is revolutionizing healthcare with amazing results...",
    "Privacy concerns grow as technology advances...",
    "New breakthrough promises exciting possibilities..."
]

results = []
for i, article in enumerate(articles, 1):
    sentiment = analyzer.analyze_sentiment(article)
    if sentiment['success']:
        print(f"Article {i}: {sentiment['sentiment']}")
        print(f"  Polarity: {sentiment['polarity']:.2f}")
        print(f"  Subjectivity: {sentiment['subjectivity']:.2f}\n")
        results.append(sentiment)
```

**Output**:
```
Article 1: Positive
  Polarity: 0.35
  Subjectivity: 0.42

Article 2: Negative
  Polarity: -0.15
  Subjectivity: 0.38

Article 3: Positive
  Polarity: 0.42
  Subjectivity: 0.55
```

### Example 2: Automated Report Generation

Generate a complete analysis report:

```python
from utils import ArticleFetcher, ContentAnalyzer, TextSummarizer

# Initialize
fetcher = ArticleFetcher()
analyzer = ContentAnalyzer()
summarizer = TextSummarizer()

# Fetch article
url = "https://example.com/article"
article = fetcher.fetch_from_url(url)

if article['success']:
    text = article['text']
    
    # Analyze
    stats = analyzer.get_text_statistics(text)
    sentiment = analyzer.analyze_sentiment(text)
    keywords = analyzer.extract_keywords(text, 10)
    summary = summarizer.extractive_summarize(text, 3)
    
    # Generate report
    print(f"ANALYSIS REPORT: {article['title']}")
    print("=" * 60)
    print(f"\nURL: {url}")
    print(f"Author(s): {', '.join(article['authors'])}")
    print(f"Published: {article['publish_date']}")
    
    print(f"\n📊 STATISTICS")
    print(f"Words: {stats['word_count']}")
    print(f"Reading Time: {stats['reading_time_minutes']} minutes")
    
    print(f"\n😊 SENTIMENT")
    print(f"Overall: {sentiment['sentiment']}")
    print(f"Polarity: {sentiment['polarity']:.2f}")
    
    print(f"\n📝 SUMMARY")
    print(summary['summary'])
    
    print(f"\n🔑 TOP KEYWORDS")
    for word, freq in keywords[:5]:
        print(f"  - {word}: {freq}")
```

### Example 3: Multilingual Processing

Process articles in multiple languages:

```python
from utils import Translator, ContentAnalyzer

translator = Translator()
analyzer = ContentAnalyzer()

# Detect and translate
text = "Bonjour, ceci est un texte en français."

# Detect language
detection = translator.detect_language(text)
print(f"Detected: {detection['language_name']}")

# Translate to English
translation = translator.translate_text(text, 'en')
if translation['success']:
    english_text = translation['translated_text']
    print(f"Translated: {english_text}")
    
    # Analyze translated text
    sentiment = analyzer.analyze_sentiment(english_text)
    print(f"Sentiment: {sentiment['sentiment']}")
```

### Example 4: Keyword Trend Analysis

Compare keywords across multiple documents:

```python
from utils import ContentAnalyzer
from collections import Counter

analyzer = ContentAnalyzer()

documents = [
    "AI and machine learning are transforming industries...",
    "Deep learning neural networks achieve breakthroughs...",
    "Machine learning applications in healthcare..."
]

all_keywords = Counter()

for doc in documents:
    keywords = analyzer.extract_keywords(doc, 10)
    for word, freq in keywords:
        all_keywords[word] += freq

print("Overall top keywords:")
for word, freq in all_keywords.most_common(5):
    print(f"  {word}: {freq}")
```

## Advanced Features

### Custom Summary Length

Adjust based on your needs:

```python
from utils import TextSummarizer

summarizer = TextSummarizer()
text = "Your long article text..."

# Very brief (1 sentence)
brief = summarizer.extractive_summarize(text, 1)

# Moderate (3 sentences)
moderate = summarizer.extractive_summarize(text, 3)

# Detailed (7 sentences)
detailed = summarizer.extractive_summarize(text, 7)
```

### Sentence-Level Analysis

Track sentiment throughout the article:

```python
from utils import ContentAnalyzer

analyzer = ContentAnalyzer()
text = "Your article text..."

sentence_sentiments = analyzer.analyze_sentence_sentiments(text)

for i, sent_data in enumerate(sentence_sentiments, 1):
    polarity = sent_data['polarity']
    sentiment_type = 'Positive' if polarity > 0.1 else 'Negative' if polarity < -0.1 else 'Neutral'
    print(f"Sentence {i} ({sentiment_type}): {sent_data['sentence']}")
```

### Combining Multiple Analyses

Create a comprehensive analysis pipeline:

```python
def comprehensive_analysis(text):
    """Perform all available analyses"""
    from utils import ContentAnalyzer, TextSummarizer, Translator
    
    results = {}
    
    # Initialize
    analyzer = ContentAnalyzer()
    summarizer = TextSummarizer()
    translator = Translator()
    
    # Language detection
    lang = translator.detect_language(text)
    results['language'] = lang
    
    # Statistics
    stats = analyzer.get_text_statistics(text)
    results['statistics'] = stats
    
    # Sentiment
    sentiment = analyzer.analyze_sentiment(text)
    results['sentiment'] = sentiment
    
    # Keywords
    keywords = analyzer.extract_keywords(text, 15)
    results['keywords'] = keywords
    
    # Summary
    summary = summarizer.extractive_summarize(text, 3)
    results['summary'] = summary
    
    # Bullet points
    bullets = summarizer.bullet_point_summary(text, 5)
    results['bullets'] = bullets
    
    return results

# Use it
analysis = comprehensive_analysis("Your article text...")
print(f"Language: {analysis['language']['language_name']}")
print(f"Sentiment: {analysis['sentiment']['sentiment']}")
print(f"Summary: {analysis['summary']['summary']}")
```

## Common Use Cases

### 1. Daily News Digest

Create a daily summary of news articles:

```python
from utils import ArticleFetcher, TextSummarizer

fetcher = ArticleFetcher()
summarizer = TextSummarizer()

news_urls = [
    "https://news1.com/article1",
    "https://news2.com/article2",
    "https://news3.com/article3"
]

print("DAILY NEWS DIGEST")
print("=" * 60)

for url in news_urls:
    article = fetcher.fetch_from_url(url)
    if article['success']:
        summary = summarizer.extractive_summarize(article['text'], 2)
        print(f"\n{article['title']}")
        print(f"{summary['summary']}")
```

### 2. Academic Research Scanner

Scan research papers for relevance:

```python
def scan_research_paper(text, keywords_of_interest):
    """Check if paper is relevant based on keywords"""
    from utils import ContentAnalyzer
    
    analyzer = ContentAnalyzer()
    paper_keywords = analyzer.extract_keywords(text, 20)
    
    # Get just the words
    paper_words = [word for word, freq in paper_keywords]
    
    # Check overlap
    relevant_keywords = set(keywords_of_interest) & set(paper_words)
    
    if relevant_keywords:
        print(f"✓ Relevant! Found: {', '.join(relevant_keywords)}")
        return True
    else:
        print("✗ Not relevant")
        return False

# Usage
interest_keywords = ['machine learning', 'neural networks', 'deep learning']
paper_text = "Your paper abstract..."
scan_research_paper(paper_text, interest_keywords)
```

### 3. Content Quality Check

Evaluate article readability and depth:

```python
from utils import ContentAnalyzer

def evaluate_content_quality(text):
    """Evaluate content based on various metrics"""
    analyzer = ContentAnalyzer()
    
    stats = analyzer.get_text_statistics(text)
    keywords = analyzer.extract_keywords(text, 10)
    
    # Check word count
    word_count = stats['word_count']
    
    # Check average sentence length
    avg_length = stats['avg_sentence_length']
    
    # Check keyword diversity
    keyword_diversity = len(keywords)
    
    print("CONTENT QUALITY EVALUATION")
    print("=" * 40)
    
    # Evaluate depth
    if word_count < 300:
        print("Depth: ⚠️  Too short")
    elif word_count < 800:
        print("Depth: ✓ Adequate")
    else:
        print("Depth: ✓✓ Comprehensive")
    
    # Evaluate readability
    if avg_length < 15:
        print("Readability: ✓✓ Very readable")
    elif avg_length < 25:
        print("Readability: ✓ Good")
    else:
        print("Readability: ⚠️  Complex")
    
    # Evaluate topic coverage
    if keyword_diversity > 8:
        print("Topic Coverage: ✓✓ Excellent")
    elif keyword_diversity > 5:
        print("Topic Coverage: ✓ Good")
    else:
        print("Topic Coverage: ⚠️  Limited")

# Usage
evaluate_content_quality("Your article text...")
```

## Tips and Best Practices

### 1. Input Quality
- **Longer texts** (500+ words) provide better analysis
- **Clean text** without excessive formatting works best
- **Complete articles** give better context than snippets

### 2. Language Handling
- Auto-detect works well for most languages
- For mixed-language texts, translate first
- Some languages may have limited sentiment lexicons

### 3. Summary Optimization
- **News articles**: 2-3 sentences
- **Research papers**: 5-7 sentences
- **Long reports**: 7-10 sentences

### 4. Keyword Extraction
- Filter out domain-specific stop words if needed
- Increase top_n for longer documents
- Keywords work best with focused content

### 5. Performance
- First run may be slower (model loading)
- Cache results for repeated analyses
- Process in batches for multiple articles

### 6. Error Handling

Always check for success:

```python
from utils import ArticleFetcher

fetcher = ArticleFetcher()
result = fetcher.fetch_from_url(url)

if result['success']:
    # Process the article
    text = result['text']
else:
    # Handle error
    print(f"Error: {result.get('message', 'Unknown error')}")
```

### 7. Interpreting Sentiment

- **Polarity**: -1 (very negative) to +1 (very positive)
  - > 0.3: Strong positive
  - 0.1 to 0.3: Mild positive
  - -0.1 to 0.1: Neutral
  - -0.3 to -0.1: Mild negative
  - < -0.3: Strong negative

- **Subjectivity**: 0 (objective) to 1 (subjective)
  - > 0.6: Very subjective/opinionated
  - 0.3 to 0.6: Balanced
  - < 0.3: Very objective/factual

### 8. Memory Management

For very long texts:

```python
# Process in chunks
def analyze_long_text(text, chunk_size=5000):
    """Analyze very long texts in chunks"""
    from utils import ContentAnalyzer
    
    analyzer = ContentAnalyzer()
    chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
    
    sentiments = []
    for chunk in chunks:
        sentiment = analyzer.analyze_sentiment(chunk)
        if sentiment['success']:
            sentiments.append(sentiment['polarity'])
    
    # Average sentiment
    avg_polarity = sum(sentiments) / len(sentiments)
    return avg_polarity
```

## Troubleshooting

### Common Issues

1. **Import Errors**: Run `pip install -r requirements.txt`
2. **NLTK Data Missing**: Run `python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"`
3. **Translation Timeouts**: Reduce text size or retry
4. **URL Fetch Fails**: Some sites block automated access, use text input instead

## Next Steps

- Explore all analysis options
- Try different languages
- Experiment with summary lengths
- Build custom analysis pipelines
- Integrate into your workflow

For more information, see:
- [README.md](README.md) - Full documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick start guide
- [examples.py](examples.py) - Code examples
