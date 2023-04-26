
import requests
from bs4 import BeautifulSoup

# Specify the URL of the website to scrape
url = 'https://www.glassdoor.co.in/Reviews/Wipro-Reviews-E9936.htm'

# Send a GET request to the URL
response = requests.get(https://www.glassdoor.co.in/Reviews/Wipro-Reviews-E9936.htm)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find elements on the page using their HTML tags and attributes
title = soup.find('title').text
links = [a['href'] for a in soup.find_all('a')]

# Print the scraped data
print('Title:', title)
print('Links:', links)
