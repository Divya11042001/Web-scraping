from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

# Read the HTML file
with open('Amazon_02.html', 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# Initialize lists to store the extracted data
names = []
prices = []
reviews = []
ratings = []
authors=[]
image_urls=[]

# Find all the desired div elements
divs = soup.find_all('div', class_="puis-card-container s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis puis-v1nyb4igz33igf2j9heq96r9jtz s-latency-cf-section puis-card-border")

# Extract data from each div
for div in divs:
    # Extract name
    try:
        name = div.find('span', class_="a-size-medium a-color-base a-text-normal").get_text(strip=True)
    except AttributeError:
        name = ""
    names.append(name)
    
    # Extract price
    try:
        price = div.find('span', class_="a-price-whole").get_text(strip=True)
    except AttributeError:
        price = ""
    prices.append(price)
    
    # Extract reviews
    try:
        review = div.find('span', class_="a-size-base s-underline-text").get_text(strip=True)
    except AttributeError:
        review = ""
    reviews.append(review)

    # Extract ratings
    try:
        rating = div.find('span', class_="a-icon-alt").get_text(strip=True)
    except AttributeError:
        rating = ""
    ratings.append(rating)

    # Extract Author
    try:
        author = div.find('a', class_="a-size-base a-link-normal s-underline-text s-underline-link-text s-link-style").get_text(strip=True)
    except AttributeError:
        author = ""
    authors.append(author)

    # Extract Images
    try:
        image_div = div.find('div', class_="a-section aok-relative s-image-fixed-height")
        image_url = image_div.find('img', class_="s-image")['src']
    except AttributeError:
        image_url = ""
    image_urls.append(image_url)


    





# Create a DataFrame
data = {
    'Name': names,
    'Price': prices,
    'Reviews': reviews,
    'Ratings': ratings,
    'Authors':authors,
    'Images':image_urls
}
df = pd.DataFrame(data)

# Save the DataFrame to an Excel file
output_path = 'Bookdata03.xlsx'
df.to_excel(output_path, index=False)

print(f'Data has been written to {output_path}')