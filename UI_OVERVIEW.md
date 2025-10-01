# AGEonT-st User Interface Overview

## Main Interface Layout

### Header
```
🔍 AGEonT-st: AI-Powered Article & News Insights
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Sidebar (Left Panel)

```
┌─────────────────────────────────┐
│ ⚙️ Settings                      │
├─────────────────────────────────┤
│                                 │
│ Input Method:                   │
│ ○ URL                           │
│ ● Text                          │
│                                 │
├─────────────────────────────────┤
│                                 │
│ Target Language:                │
│ [English ▼]                     │
│                                 │
├─────────────────────────────────┤
│                                 │
│ Analysis Options:               │
│ ☑ Translation                   │
│ ☑ Sentiment Analysis            │
│ ☑ Summarization                 │
│ ☑ Keywords                      │
│ ☑ Statistics                    │
│                                 │
├─────────────────────────────────┤
│                                 │
│ Summary Sentences:              │
│ ────●────── 3                   │
│ 1         5         10          │
│                                 │
├─────────────────────────────────┤
│                                 │
│ ### About                       │
│ ℹ️ This AI-powered system       │
│   analyzes articles and news    │
│   with multilingual support,    │
│   sentiment analysis, and       │
│   automated insights.           │
│                                 │
└─────────────────────────────────┘
```

### Main Content Area

#### Left Column - Input Section
```
┌─────────────────────────────────────────────────────┐
│ 📝 Input                                            │
├─────────────────────────────────────────────────────┤
│                                                     │
│ Article Title:                                      │
│ [Enter article title (optional)               ]    │
│                                                     │
│ Article Text:                                       │
│ ┌─────────────────────────────────────────────┐   │
│ │ Paste the article text here...              │   │
│ │                                             │   │
│ │                                             │   │
│ │                                             │   │
│ │                                             │   │
│ │                                             │   │
│ │                                             │   │
│ └─────────────────────────────────────────────┘   │
│                                                     │
│ ▼ 📄 Preview                                        │
│   ┌───────────────────────────────────────────┐   │
│   │ Artificial Intelligence has transformed...│   │
│   │ ...                                       │   │
│   └───────────────────────────────────────────┘   │
│                                                     │
└─────────────────────────────────────────────────────┘
```

#### Right Column - Analysis Section
```
┌─────────────────────────────────────────────────────┐
│ 🔍 Analysis                                         │
├─────────────────────────────────────────────────────┤
│                                                     │
│        [Analyze Article]                            │
│                                                     │
└─────────────────────────────────────────────────────┘
```

### Results Display (After Analysis)

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Results

ℹ️ 🌍 Detected Language: English
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

┌─────────┬──────────┬──────────┬──────────┬──────────┐
│ Summary │ Sentiment│ Keywords │Statistics│ Detailed │
└─────────┴──────────┴──────────┴──────────┴──────────┘

SUMMARY TAB:
┌────────────────────────────────────────────────────────────┐
│ 📝 Summary                                                 │
├────────────────────────────────────────────────────────────┤
│ Artificial Intelligence has transformed the landscape      │
│ of technology in recent years. Machine learning           │
│ algorithms are achieving remarkable results.              │
│                                                            │
│ Key Points:                                                │
│ • Artificial Intelligence has transformed technology       │
│ • Machine learning algorithms achieve remarkable results  │
│ • Future promises exciting developments in healthcare     │
│                                                            │
│ Condensed from 8 to 3 sentences                           │
└────────────────────────────────────────────────────────────┘

SENTIMENT TAB:
┌────────────────────────────────────────────────────────────┐
│ 😊 Sentiment Analysis                                      │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌──────────┐  ┌──────────┐  ┌──────────────┐           │
│  │ Overall  │  │ Polarity │  │ Subjectivity │           │
│  │ Sentiment│  │   0.25   │  │     0.43     │           │
│  │ 😊       │  │          │  │              │           │
│  │ Positive │  │          │  │              │           │
│  └──────────┘  └──────────┘  └──────────────┘           │
│                                                            │
│  Sentiment Polarity Gauge:                                 │
│  ┌────────────────────────────────────────────────┐       │
│  │         ╭────────────────●──────────╮          │       │
│  │    0    │    33    50    │    66   100         │       │
│  │  Negative│  Neutral  │  Positive              │       │
│  └────────────────────────────────────────────────┘       │
│                                                            │
│  Sentiment Over Sentences:                                 │
│  ┌────────────────────────────────────────────────┐       │
│  │  1.0 │               ╱╲                        │       │
│  │  0.5 │         ╱╲   ╱  ╲    ╱╲                │       │
│  │  0.0 │────────────────────────────────         │       │
│  │ -0.5 │                                         │       │
│  │      └───────────────────────────────►         │       │
│  │        Sentence Number                         │       │
│  └────────────────────────────────────────────────┘       │
└────────────────────────────────────────────────────────────┘

KEYWORDS TAB:
┌────────────────────────────────────────────────────────────┐
│ 🔑 Key Terms                                               │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  Keywords Table:            Top Keywords Chart:            │
│  ┌────────────┬────────┐   ┌──────────────────────┐      │
│  │ Keyword    │  Freq  │   │ intelligence ■■■■■■■ │      │
│  ├────────────┼────────┤   │ learning     ■■■■■   │      │
│  │intelligence│   8    │   │ systems      ■■■■    │      │
│  │learning    │   6    │   │ algorithms   ■■■     │      │
│  │systems     │   5    │   │ technology   ■■      │      │
│  │algorithms  │   4    │   │ future       ■■      │      │
│  │technology  │   3    │   └──────────────────────┘      │
│  │future      │   3    │                                  │
│  └────────────┴────────┘                                  │
└────────────────────────────────────────────────────────────┘

STATISTICS TAB:
┌────────────────────────────────────────────────────────────┐
│ 📈 Text Statistics                                         │
├────────────────────────────────────────────────────────────┤
│                                                            │
│  ┌────────┐  ┌───────────┐  ┌──────────┐  ┌────────────┐│
│  │ Words  │  │ Sentences │  │ Avg Sent │  │Reading Time││
│  │  156   │  │     8     │  │ Length   │  │   0.8 min  ││
│  │        │  │           │  │   19.5   │  │            ││
│  └────────┘  └───────────┘  └──────────┘  └────────────┘│
│                                                            │
│  Content Metrics:                                          │
│  ┌────────────────────────────────────────────────┐       │
│  │ 1000│                                           │       │
│  │  800│          ╔═════╗                         │       │
│  │  600│          ║     ║                         │       │
│  │  400│  ╔═══╗   ║     ║   ╔═══════╗            │       │
│  │  200│  ║   ║   ║     ║   ║       ║            │       │
│  │    0│  ║   ║   ║     ║   ║       ║            │       │
│  │     └──────────────────────────────►            │       │
│  │       Words  Sent.  Chars                      │       │
│  └────────────────────────────────────────────────┘       │
└────────────────────────────────────────────────────────────┘

DETAILED TAB:
┌────────────────────────────────────────────────────────────┐
│ 📋 Full Analysis Details                                   │
├────────────────────────────────────────────────────────────┤
│                                                            │
│ ▼ 🌐 Translation                                           │
│   Source Language: English                                 │
│   Target Language: English                                 │
│   Translated Text: [Content here]                         │
│                                                            │
│ ▼ 📄 Original Text                                         │
│   Artificial Intelligence has transformed the landscape... │
│   [Full article text]                                     │
└────────────────────────────────────────────────────────────┘
```

## Color Scheme

- **Primary Color**: #1f77b4 (Blue)
- **Background**: #ffffff (White)
- **Secondary Background**: #f0f2f6 (Light Gray)
- **Text**: #262730 (Dark Gray)
- **Success**: #28a745 (Green)
- **Warning**: #ffc107 (Amber)
- **Error**: #dc3545 (Red)

## Interactive Elements

1. **Input Toggle**: Switch between URL and Text input
2. **Language Selector**: Dropdown with 12+ language options
3. **Analysis Checkboxes**: Multi-select for analysis types
4. **Slider**: Adjust summary length (1-10 sentences)
5. **Analyze Button**: Primary action button
6. **Tabs**: Navigate between different result views
7. **Expandable Sections**: Collapsible details in various sections

## User Flow

1. User arrives at main page
2. Selects input method (URL or Text)
3. Enters article content
4. Configures analysis options in sidebar
5. Clicks "Analyze Article"
6. Views results in organized tabs
7. Can expand/collapse sections for more detail
8. All results displayed with visual charts and metrics

## Responsive Design

- Layout adapts to different screen sizes
- Sidebar collapsible on mobile devices
- Charts scale appropriately
- Touch-friendly controls

## Accessibility Features

- High contrast text
- Clear visual hierarchy
- Descriptive labels
- Keyboard navigation support
- Screen reader compatible
