"""
Example: Using AGEonT-st utilities programmatically
This script demonstrates how to use the analysis modules directly
"""

# Example article text
SAMPLE_TEXT = """
Artificial Intelligence has transformed the landscape of technology in recent years. 
Machine learning algorithms are now capable of performing tasks that were once thought 
to be exclusively human. From natural language processing to computer vision, AI systems 
are achieving remarkable results. However, challenges remain in areas such as 
interpretability, bias, and ethical considerations. Researchers are working to address 
these issues while pushing the boundaries of what AI can achieve. The future of AI 
promises exciting developments in healthcare, education, and scientific discovery.
"""


def example_sentiment_analysis():
    """Example: Sentiment Analysis"""
    print("\n" + "="*60)
    print("SENTIMENT ANALYSIS EXAMPLE")
    print("="*60)
    
    from utils import ContentAnalyzer
    
    analyzer = ContentAnalyzer()
    result = analyzer.analyze_sentiment(SAMPLE_TEXT)
    
    if result['success']:
        print(f"\nSentiment: {result['sentiment']}")
        print(f"Polarity: {result['polarity']:.3f}")
        print(f"Subjectivity: {result['subjectivity']:.3f}")
    else:
        print(f"Error: {result['error']}")


def example_summarization():
    """Example: Text Summarization"""
    print("\n" + "="*60)
    print("SUMMARIZATION EXAMPLE")
    print("="*60)
    
    from utils import TextSummarizer
    
    summarizer = TextSummarizer()
    result = summarizer.extractive_summarize(SAMPLE_TEXT, num_sentences=2)
    
    if result['success']:
        print(f"\nOriginal sentences: {result['original_sentences']}")
        print(f"Summary sentences: {result['summary_sentences']}")
        print(f"\nSummary:\n{result['summary']}")
    else:
        print(f"Error: {result['error']}")


def example_keywords():
    """Example: Keyword Extraction"""
    print("\n" + "="*60)
    print("KEYWORD EXTRACTION EXAMPLE")
    print("="*60)
    
    from utils import ContentAnalyzer
    
    analyzer = ContentAnalyzer()
    keywords = analyzer.extract_keywords(SAMPLE_TEXT, top_n=5)
    
    print("\nTop Keywords:")
    for word, freq in keywords:
        print(f"  - {word}: {freq}")


def example_statistics():
    """Example: Text Statistics"""
    print("\n" + "="*60)
    print("TEXT STATISTICS EXAMPLE")
    print("="*60)
    
    from utils import ContentAnalyzer
    
    analyzer = ContentAnalyzer()
    stats = analyzer.get_text_statistics(SAMPLE_TEXT)
    
    if stats['success']:
        print(f"\nWord Count: {stats['word_count']}")
        print(f"Sentence Count: {stats['sentence_count']}")
        print(f"Average Sentence Length: {stats['avg_sentence_length']}")
        print(f"Reading Time: {stats['reading_time_minutes']} minutes")
    else:
        print(f"Error: {stats['error']}")


def example_translation():
    """Example: Translation"""
    print("\n" + "="*60)
    print("TRANSLATION EXAMPLE")
    print("="*60)
    
    from utils import Translator
    
    translator = Translator()
    
    # Detect language
    detection = translator.detect_language(SAMPLE_TEXT)
    if detection['success']:
        print(f"\nDetected Language: {detection['language_name']}")
    
    # Translate to Spanish
    result = translator.translate_text(
        "Hello, this is a test.", 
        target_language='es'
    )
    
    if result['success']:
        print(f"\nOriginal: {result['original_text']}")
        print(f"Translated: {result['translated_text']}")
        print(f"Target Language: {result['target_language']}")


def example_article_fetching():
    """Example: Fetching Article from URL"""
    print("\n" + "="*60)
    print("ARTICLE FETCHING EXAMPLE")
    print("="*60)
    
    from utils import ArticleFetcher
    
    fetcher = ArticleFetcher()
    
    # Example with a sample URL (may not work without actual URL)
    print("\nNote: This requires a valid article URL")
    print("Example usage:")
    print("  result = fetcher.fetch_from_url('https://example.com/article')")
    print("  if result['success']:")
    print("      print(result['title'])")
    print("      print(result['text'][:200])")


def example_full_analysis():
    """Example: Complete Analysis Pipeline"""
    print("\n" + "="*60)
    print("FULL ANALYSIS PIPELINE")
    print("="*60)
    
    from utils import ContentAnalyzer, TextSummarizer
    
    analyzer = ContentAnalyzer()
    summarizer = TextSummarizer()
    
    print("\n1. Getting Statistics...")
    stats = analyzer.get_text_statistics(SAMPLE_TEXT)
    
    print("\n2. Analyzing Sentiment...")
    sentiment = analyzer.analyze_sentiment(SAMPLE_TEXT)
    
    print("\n3. Extracting Keywords...")
    keywords = analyzer.extract_keywords(SAMPLE_TEXT, top_n=5)
    
    print("\n4. Generating Summary...")
    summary = summarizer.extractive_summarize(SAMPLE_TEXT, num_sentences=2)
    
    # Display results
    print("\n" + "-"*60)
    print("ANALYSIS RESULTS")
    print("-"*60)
    
    if stats['success']:
        print(f"\n📊 Statistics:")
        print(f"  Words: {stats['word_count']}")
        print(f"  Sentences: {stats['sentence_count']}")
        print(f"  Reading Time: {stats['reading_time_minutes']} min")
    
    if sentiment['success']:
        print(f"\n😊 Sentiment:")
        print(f"  Overall: {sentiment['sentiment']}")
        print(f"  Polarity: {sentiment['polarity']:.3f}")
    
    if keywords:
        print(f"\n🔑 Top Keywords:")
        for word, freq in keywords[:3]:
            print(f"  - {word}")
    
    if summary['success']:
        print(f"\n📝 Summary:")
        print(f"  {summary['summary']}")


def main():
    """Run all examples"""
    print("\n" + "="*60)
    print("AGEonT-st: Programmatic Usage Examples")
    print("="*60)
    
    try:
        example_sentiment_analysis()
        example_summarization()
        example_keywords()
        example_statistics()
        example_translation()
        example_article_fetching()
        example_full_analysis()
        
        print("\n" + "="*60)
        print("✅ All examples completed successfully!")
        print("="*60)
        
    except Exception as e:
        print(f"\n❌ Error running examples: {e}")
        print("Make sure all dependencies are installed:")
        print("  pip install -r requirements.txt")


if __name__ == "__main__":
    main()
