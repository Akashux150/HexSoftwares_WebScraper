import requests
from bs4 import BeautifulSoup
import pandas as pd

# Step 1: Define the website URL
url = "http://quotes.toscrape.com/"

# Step 2: Send request to the website
response = requests.get(url)

# Step 3: Check if request was successful
if response.status_code == 200:
    print("Website connected successfully")
else:
    print("Failed to connect")

# Step 4: Parse the HTML content
soup = BeautifulSoup(response.text, "html.parser")

# Step 5: Find all quotes and authors
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")

# Step 6: Store data in list
data = []

for quote, author in zip(quotes, authors):
    data.append({
        "Quote": quote.text,
        "Author": author.text
    })

# Step 7: Convert list into dataframe
df = pd.DataFrame(data)

# Step 8: Save data into CSV file
df.to_csv("quotes.csv", index=False)

# Step 9: Print success message
print("Web scraping completed successfully!")
print("Data saved into quotes.csv")