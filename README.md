# AGEonT-st: AI-Powered Multilingual Research Article and News Insight System

An advanced AI-powered system for analyzing research articles and news from multiple sources with multilingual support, sentiment analysis, and automated insights generation.

## Features

- **Multilingual Support**: Analyze articles in multiple languages with automatic translation
- **AI-Powered Analysis**: Leverage state-of-the-art NLP models for deep content understanding
- **Sentiment Analysis**: Understand the emotional tone and sentiment of articles
- **Automated Summarization**: Generate concise summaries of lengthy articles
- **Research Insights**: Extract key findings, trends, and patterns from articles
- **Interactive Dashboard**: User-friendly Streamlit interface for easy interaction
- **Multiple Input Methods**: Support for URL fetching and direct text input

## Installation

1. Clone the repository:
```bash
git clone https://github.com/paildeep01/AGEonT-st.git
cd AGEonT-st
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Download required NLTK data:
```python
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

## Usage

Run the Streamlit application:
```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`.

## Application Features

### 1. Article Input
- **URL Input**: Fetch articles directly from web URLs
- **Text Input**: Paste article text directly
- **Language Detection**: Automatic language detection

### 2. Analysis Options
- **Translation**: Translate articles to your preferred language
- **Sentiment Analysis**: Analyze the emotional tone
- **Summarization**: Generate concise summaries
- **Key Insights**: Extract important points and themes

### 3. Visualization
- **Sentiment Charts**: Visual representation of sentiment analysis
- **Word Clouds**: Most frequent terms and topics
- **Timeline Analysis**: Track sentiment over article sections

## Project Structure

```
AGEonT-st/
├── app.py                 # Main Streamlit application
├── utils/
│   ├── article_fetcher.py # Article fetching and parsing
│   ├── translator.py      # Multilingual translation
│   ├── analyzer.py        # Sentiment and content analysis
│   └── summarizer.py      # Text summarization
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## Technologies Used

- **Streamlit**: Interactive web application framework
- **Transformers**: State-of-the-art NLP models (BART, BERT)
- **BeautifulSoup4**: Web scraping and HTML parsing
- **Newspaper3k**: Article extraction and parsing
- **TextBlob**: Natural language processing
- **NLTK**: Natural language toolkit
- **Plotly**: Interactive visualizations

## Configuration

Create a `.env` file in the root directory for custom configurations:
```
DEFAULT_LANGUAGE=en
MAX_SUMMARY_LENGTH=150
MIN_SUMMARY_LENGTH=50
```

## Examples

### Analyzing a News Article
1. Paste the article URL in the input field
2. Select target language for translation (if needed)
3. Click "Analyze Article"
4. View sentiment analysis, summary, and key insights

### Analyzing Research Papers
1. Copy and paste the research paper text
2. Select analysis options
3. Get automated insights and summaries
4. Export results for further use

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.

## Support

For issues, questions, or contributions, please open an issue on GitHub.

## Roadmap

- [ ] Add support for PDF document parsing
- [ ] Implement citation extraction
- [ ] Add batch processing for multiple articles
- [ ] Create API endpoints for programmatic access
- [ ] Add support for more languages
- [ ] Implement advanced topic modeling
- [ ] Add user authentication and saved analyses

## Acknowledgments

This project uses various open-source libraries and pre-trained models from the NLP community.