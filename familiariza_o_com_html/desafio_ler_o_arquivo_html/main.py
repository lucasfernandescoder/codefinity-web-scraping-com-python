# Importing the module
from urllib.request import urlopen

# Opening web page
url = "https://codefinity-content-media.s3.eu-west-1.amazonaws.com/18a4e428-1a0f-44c2-a8ad-244cd9c7985e/page.html"
page = urlopen(url)


# Reading and decoding
web_page = page.read().decode("utf-8")
print(web_page)