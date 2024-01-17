import os

from selenium import webdriver


class ScriptScraper:
    def __init__(self, url, webbrowser):
        self.url = url
        webbrowser = webbrowser.lower()
        if webbrowser == 'firefox':
            self.driver = webdriver.Firefox()
        elif webbrowser == 'google chrome':
            self.driver = webdriver.Chrome()
        else:
            raise ValueError("Unsupported web browser: {}".format(webbrowser))

    def returnRawScript(self):
        # Create a file name based on the URL (you might want to adjust this logic)
        file_name = os.path.join('/Users/asatpathy/PycharmProjects/DataScienceProject/Raw Scripts',
                                 f'{os.path.basename(self.url)}.txt')
        # Check if the file exists
        if os.path.exists(file_name):
            with open(file_name, 'r') as file:
                return file.read(), file_name
        else:
            # Fetch the script from the web if the file doesn't exist
            self.driver.get(self.url)  # Navigate to the provided URL
            script = self.driver.page_source
            index_until = script.find('Written by')
            index_end = script.find('</pre><br>')
            script = script[index_until:index_end:1]
            # Ensure the entire directory structure exists
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
            # Write the raw script to a new file
            with open(file_name, 'w') as file:
                file.write(script)
            return script, file_name
