from WebScraper import ScriptScraper
from DataAnalyzer import DataAnalyzer


def main():
    script, file_name = scrape_script("https://imsdb.com/scripts/Joker.html")
    my_analyzer = DataAnalyzer(script, file_name)

    # Start Conducting Analyses!


def scrape_script(url):
    my_scraper = ScriptScraper(url, 'Google Chrome')
    return my_scraper.returnRawScript()


main()
