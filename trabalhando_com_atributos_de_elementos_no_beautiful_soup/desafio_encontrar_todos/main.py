# Import libraries
from bs4 import BeautifulSoup
from urllib.request import urlopen

# Open the page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/mother.html"
page = urlopen(url)
html = page.read().decode("utf-8")

# Create the BeautifulSoup object
soup = BeautifulSoup(html, "html.parser")

# Print the first `<div>` tag
for div in soup.find("div"):
    print(soup.find("div"))
# Print the tag `<p>` with the correct id
print(soup.find_all("p", {"id": "id0"}))
