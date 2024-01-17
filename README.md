**Program Description:**

The provided Python program consists of three files: `DataAnalyzer.py`, `main.py`, and `WebScraper.py`. These files work together to perform sentiment analysis and word analysis on a movie or TV show script fetched from a given URL.

**DataAnalyzer.py:**
- `DataAnalyzer` is a class designed for analyzing script data.
- The `basic_clean` method removes unnecessary elements like scene descriptions, character names, and formatting.
- `prepare_for_nlp` and `prepare_for_word_analysis` methods further process the script for Natural Language Processing (NLP) tasks.
- `get_overall_sentiment` calculates and returns the overall sentiment of the script using TextBlob.
- `plot_sentiment_over_time` visualizes the sentiment polarity of the script over time in 20 parts.
- `word_count` returns the total number of words in the processed script.
- `count_word` method counts the occurrences of a specific word in the script.

**main.py:**
- `main` function serves as the entry point for the program.
- It calls functions from `WebScraper` to fetch the script from a specified URL.
- An instance of `DataAnalyzer` is created, allowing the user to run any of its documented functions.

**WebScraper.py:**
- `ScriptScraper` is a class responsible for scraping the script from a given URL using Selenium.
- The constructor initializes a WebDriver based on the specified web browser (Chrome or Firefox).
- `returnRawScript` method fetches the script either from a local file or by navigating to the URL and extracts the script from the page source.

**Readme File Text:**

# Script Analyzer

## Overview
The Script Analyzer is a Python program designed for analyzing movie or TV show scripts. It provides functionalities for sentiment analysis and word analysis, allowing users to gain insights into the emotional tone and lexical composition of a given script.

## Usage
1. Ensure you have the necessary dependencies installed:
   ```
   pip install textblob nltk matplotlib selenium
   ```

2. Run the `main.py` file, providing the URL of the script you want to analyze.

3. The program will fetch the script, perform analysis, and present the results.

## Features
- **Sentiment Analysis:** Understand the overall sentiment of the script using the `get_overall_sentiment` method.
- **Sentiment Over Time Plot:** Visualize the sentiment polarity of the script over time with the `plot_sentiment_over_time` method.
- **Word Analysis:** Explore word count and frequency with the `word_count` and `count_word` methods.

## Example
```python
from WebScraper import ScriptScraper
from DataAnalyzer import DataAnalyzer

def main():
    # Specify the URL of the script
    url = 'insert_url_here'
    
    # Fetch the script
    script, file_name = scrape_script(url)
    
    # Analyze the script using DataAnalyzer
    my_analyzer = DataAnalyzer(script, file_name)
    
    # Run any of the functions documented in DataAnalyzer
    my_analyzer.plot_sentiment_over_time()

if __name__ == "__main__":
    main()
```

## Note
- Ensure you have the appropriate web driver (ChromeDriver or GeckoDriver) installed and available in your system's PATH for web scraping functionality.
