from bs4 import BeautifulSoup
import requests
import smtplib



# the code that HAS TO BE CHANGED -->



# ========================

# this is the link to the product on amazon page
PRODUCT_LINK = "https://www.amazon.com.au/HonHey-Handheld-Portable-Rechargeable-Personal/dp/B07Q2C1TNQ/ref=sr_1_1?crid=273GKEF69WDJL&keywords=ventilator%2Bportable&qid=1699647905&sprefix=ventilator%2Bportab%2Caps%2C274&sr=8-1&th=1"

# the header files you need to provide in order to get access to amazon web page contents
headers = {
    "User-Agent": "to_be_written",
    "Accept-Language": "to_be_written"
}

# email that will be used in order to send a low price alert
EMAIL = ""
PASSWORD = ""

# email that will be used to receive low price alert
RECEIVER_EMAIL = ""

# the price that will determine whether to send email about low price alert or no
PRICE_THRESHOLD = 100

# ========================



# the code that DOES NOT HAVE TO BE CHANGED -->



# making GET request to the page of the product
# ========================
response = requests.get(url=PRODUCT_LINK,
                        headers=headers)
# ========================

# creating a BeautifulSoup object in order to scrape the data
# and scraping the price of the product
# ========================
soup = BeautifulSoup(response.text, "html.parser")
price = float(soup.find(class_="a-price-whole").getText())
# ========================

# if the price is less than the specified amount, the code will send an email
# with an alert that you can buy this product, and the link to that product.
# ========================
if price < PRICE_THRESHOLD:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL=EMAIL, password=PASSWORD)
        message = f"Subject:Low price for a rice cooker!\n\n" \
                  f"Go to \n\n{PRODUCT_LINK}\n\n to buy the rice cooker" \
                  f"right now!\n\nPrice: {round(price, 2)}$"
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=RECEIVER_EMAIL,
                            msg=message)
# ========================
