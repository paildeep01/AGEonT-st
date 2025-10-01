"""
AGEonT-st: AI-Powered Multilingual Research Article and News Insight System
Main Streamlit Application
"""
import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
from utils import ArticleFetcher, Translator, ContentAnalyzer, TextSummarizer
import config

# Page configuration
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon=config.APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state
if 'analysis_results' not in st.session_state:
    st.session_state.analysis_results = None

# Initialize utility classes
@st.cache_resource
def get_utilities():
    """Initialize and cache utility classes"""
    return {
        'fetcher': ArticleFetcher(),
        'translator': Translator(),
        'analyzer': ContentAnalyzer(),
        'summarizer': TextSummarizer()
    }

utils = get_utilities()


def main():
    """Main application function"""
    
    # Header
    st.title(f"{config.APP_ICON} {config.APP_TITLE}")
    st.markdown("---")
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        input_method = st.radio(
            "Input Method:",
            ["URL", "Text"],
            help="Choose how to input the article"
        )
        
        st.markdown("---")
        
        target_language = st.selectbox(
            "Target Language:",
            options=list(config.SUPPORTED_LANGUAGES.keys()),
            format_func=lambda x: config.SUPPORTED_LANGUAGES[x],
            index=0,
            help="Select language for translation"
        )
        
        st.markdown("---")
        
        analysis_options = st.multiselect(
            "Analysis Options:",
            ["Translation", "Sentiment Analysis", "Summarization", "Keywords", "Statistics"],
            default=["Sentiment Analysis", "Summarization", "Keywords"],
            help="Select analysis types to perform"
        )
        
        summary_sentences = st.slider(
            "Summary Sentences:",
            min_value=1,
            max_value=10,
            value=3,
            help="Number of sentences in summary"
        )
        
        st.markdown("---")
        st.markdown("### About")
        st.info(
            "This AI-powered system analyzes articles and news with multilingual support, "
            "sentiment analysis, and automated insights generation."
        )
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📝 Input")
        
        article_text = ""
        article_title = ""
        
        if input_method == "URL":
            url = st.text_input(
                "Enter Article URL:",
                placeholder="https://example.com/article",
                help="Paste the URL of the article to analyze"
            )
            
            if st.button("Fetch Article", type="primary"):
                if url:
                    with st.spinner("Fetching article..."):
                        result = utils['fetcher'].fetch_from_url(url)
                        
                        if result['success']:
                            article_text = result['text']
                            article_title = result['title']
                            st.success("✅ Article fetched successfully!")
                            st.session_state.article_text = article_text
                            st.session_state.article_title = article_title
                        else:
                            st.error(f"❌ {result.get('message', 'Failed to fetch article')}")
                else:
                    st.warning("Please enter a URL")
        else:
            article_title = st.text_input(
                "Article Title:",
                placeholder="Enter article title (optional)"
            )
            
            article_text = st.text_area(
                "Article Text:",
                height=300,
                placeholder="Paste the article text here...",
                help="Paste or type the article content"
            )
            
            if article_text:
                st.session_state.article_text = article_text
                st.session_state.article_title = article_title
        
        # Display input preview
        if 'article_text' in st.session_state and st.session_state.article_text:
            with st.expander("📄 Preview"):
                if st.session_state.get('article_title'):
                    st.subheader(st.session_state.article_title)
                st.write(st.session_state.article_text[:500] + "..." 
                        if len(st.session_state.article_text) > 500 
                        else st.session_state.article_text)
    
    with col2:
        st.header("🔍 Analysis")
        
        if st.button("Analyze Article", type="primary", use_container_width=True):
            if 'article_text' in st.session_state and st.session_state.article_text:
                analyze_article(
                    st.session_state.article_text,
                    st.session_state.get('article_title', ''),
                    target_language,
                    analysis_options,
                    summary_sentences
                )
            else:
                st.warning("Please provide article text first")
    
    # Display results
    if st.session_state.analysis_results:
        display_results(st.session_state.analysis_results)


def analyze_article(text, title, target_lang, options, num_sentences):
    """Perform comprehensive article analysis"""
    
    results = {
        'title': title,
        'original_text': text
    }
    
    with st.spinner("Analyzing article..."):
        # Language detection
        lang_result = utils['translator'].detect_language(text)
        if lang_result['success']:
            results['detected_language'] = lang_result
        
        # Translation
        if "Translation" in options and target_lang != 'en':
            trans_result = utils['translator'].translate_text(text, target_lang)
            if trans_result['success']:
                results['translation'] = trans_result
                analysis_text = trans_result['translated_text']
            else:
                analysis_text = text
        else:
            analysis_text = text
        
        # Sentiment Analysis
        if "Sentiment Analysis" in options:
            sentiment_result = utils['analyzer'].analyze_sentiment(analysis_text)
            if sentiment_result['success']:
                results['sentiment'] = sentiment_result
        
        # Summarization
        if "Summarization" in options:
            summary_result = utils['summarizer'].extractive_summarize(analysis_text, num_sentences)
            if summary_result['success']:
                results['summary'] = summary_result
                
                # Bullet points
                bullet_points = utils['summarizer'].bullet_point_summary(analysis_text, num_sentences)
                results['bullet_points'] = bullet_points
        
        # Keywords
        if "Keywords" in options:
            keywords = utils['analyzer'].extract_keywords(analysis_text, 15)
            results['keywords'] = keywords
        
        # Statistics
        if "Statistics" in options:
            stats = utils['analyzer'].get_text_statistics(analysis_text)
            if stats['success']:
                results['statistics'] = stats
        
        # Sentence-level sentiment
        if "Sentiment Analysis" in options:
            sentence_sentiments = utils['analyzer'].analyze_sentence_sentiments(analysis_text)
            results['sentence_sentiments'] = sentence_sentiments
    
    st.session_state.analysis_results = results
    st.success("✅ Analysis complete!")


def display_results(results):
    """Display analysis results"""
    
    st.markdown("---")
    st.header("📊 Results")
    
    # Language Detection
    if 'detected_language' in results:
        st.info(f"🌍 **Detected Language:** {results['detected_language']['language_name']}")
    
    # Create tabs for different results
    tabs = st.tabs(["Summary", "Sentiment", "Keywords", "Statistics", "Detailed"])
    
    # Summary Tab
    with tabs[0]:
        if 'summary' in results:
            st.subheader("📝 Summary")
            st.write(results['summary']['summary'])
            
            st.markdown("**Key Points:**")
            if 'bullet_points' in results:
                for point in results['bullet_points']:
                    st.markdown(point)
            
            st.caption(f"Condensed from {results['summary']['original_sentences']} to "
                      f"{results['summary']['summary_sentences']} sentences")
        else:
            st.info("Summary not generated. Enable in analysis options.")
    
    # Sentiment Tab
    with tabs[1]:
        if 'sentiment' in results:
            st.subheader("😊 Sentiment Analysis")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                sentiment = results['sentiment']['sentiment']
                emoji = "😊" if sentiment == "Positive" else "😐" if sentiment == "Neutral" else "😞"
                st.metric("Overall Sentiment", f"{emoji} {sentiment}")
            
            with col2:
                st.metric("Polarity", f"{results['sentiment']['polarity']:.2f}")
            
            with col3:
                st.metric("Subjectivity", f"{results['sentiment']['subjectivity']:.2f}")
            
            # Sentiment gauge
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=results['sentiment']['polarity_percentage'],
                domain={'x': [0, 1], 'y': [0, 1]},
                title={'text': "Sentiment Polarity"},
                gauge={
                    'axis': {'range': [0, 100]},
                    'bar': {'color': "darkblue"},
                    'steps': [
                        {'range': [0, 33], 'color': "lightcoral"},
                        {'range': [33, 66], 'color': "lightyellow"},
                        {'range': [66, 100], 'color': "lightgreen"}
                    ],
                    'threshold': {
                        'line': {'color': "red", 'width': 4},
                        'thickness': 0.75,
                        'value': 50
                    }
                }
            ))
            fig.update_layout(height=300)
            st.plotly_chart(fig, use_container_width=True)
            
            # Sentence-level sentiment
            if 'sentence_sentiments' in results and results['sentence_sentiments']:
                st.subheader("Sentiment Over Sentences")
                
                sentiment_data = pd.DataFrame(results['sentence_sentiments'])
                if not sentiment_data.empty:
                    fig = px.line(
                        sentiment_data,
                        y='polarity',
                        title='Sentiment Flow',
                        labels={'index': 'Sentence', 'polarity': 'Sentiment Polarity'}
                    )
                    fig.add_hline(y=0, line_dash="dash", line_color="gray")
                    st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Sentiment analysis not performed. Enable in analysis options.")
    
    # Keywords Tab
    with tabs[2]:
        if 'keywords' in results:
            st.subheader("🔑 Key Terms")
            
            if results['keywords']:
                keywords_df = pd.DataFrame(
                    results['keywords'],
                    columns=['Keyword', 'Frequency']
                )
                
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.dataframe(keywords_df, use_container_width=True)
                
                with col2:
                    fig = px.bar(
                        keywords_df.head(10),
                        x='Frequency',
                        y='Keyword',
                        orientation='h',
                        title='Top Keywords'
                    )
                    st.plotly_chart(fig, use_container_width=True)
            else:
                st.info("No keywords extracted")
        else:
            st.info("Keyword extraction not performed. Enable in analysis options.")
    
    # Statistics Tab
    with tabs[3]:
        if 'statistics' in results:
            st.subheader("📈 Text Statistics")
            
            stats = results['statistics']
            
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.metric("Words", f"{stats['word_count']:,}")
            
            with col2:
                st.metric("Sentences", f"{stats['sentence_count']:,}")
            
            with col3:
                st.metric("Avg Sentence Length", f"{stats['avg_sentence_length']}")
            
            with col4:
                st.metric("Reading Time", f"{stats['reading_time_minutes']} min")
            
            # Statistics chart
            stats_data = pd.DataFrame([
                {'Metric': 'Word Count', 'Value': stats['word_count']},
                {'Metric': 'Sentence Count', 'Value': stats['sentence_count']},
                {'Metric': 'Character Count', 'Value': stats['character_count']}
            ])
            
            fig = px.bar(
                stats_data,
                x='Metric',
                y='Value',
                title='Content Metrics'
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Statistics not generated. Enable in analysis options.")
    
    # Detailed Tab
    with tabs[4]:
        st.subheader("📋 Full Analysis Details")
        
        if 'translation' in results:
            with st.expander("🌐 Translation"):
                st.write(f"**Source Language:** {results['translation']['source_language']}")
                st.write(f"**Target Language:** {results['translation']['target_language']}")
                st.write(f"**Translated Text:**")
                st.write(results['translation']['translated_text'])
        
        with st.expander("📄 Original Text"):
            st.write(results['original_text'])


if __name__ == "__main__":
    main()
