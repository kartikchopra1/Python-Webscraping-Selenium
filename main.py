from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import datetime
import os
import sys

application_path = os.path.dirname(sys.executable)

# Print name on specific date
now = datetime.now()
month_day_year = now.strftime("%m%d%Y")  # MMDDYY

# apth of website
website = "https://www.thesun.co.uk/sport/football/"
# path of webdriver
path = "/Users/karti/Downloads/chromedriver"

# headless-mode
options = Options()
options.headless = True

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

contain = driver.find_elements(by="xpath",
                               value='//div[@class="teaser__copy-container"]')
# heading of cv file
titles = []
subtitles = []
links = []

# for loop to fetch title, subtiltes and links in webiste with xpath
for container in contain:
    title = container.find_element(by="xpath", value='./a/h3').text
    subtitle = container.find_element(by="xpath", value='./a/p').text
    lin = container.find_element(by="xpath", value='./a').get_attribute("href")
    titles.append(title)
    subtitles.append(subtitle)
    links.append(lin)

# dictonry for printing in csv
my_dict = {'title': titles, 'subtitle': subtitles, 'link': links}
df_headlines = pd.DataFrame(my_dict)
file_name = f'headline-{month_day_year}.csv'

# join methond to remane file to avoide confilt of /
final_path = os.path.join(application_path, file_name)

df_headlines.to_csv()

driver.quit()
