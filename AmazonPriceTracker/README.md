# Low Price Tracker

This is the code that uses **Requests** and **BeautifulSoup** in order to scrape the data from the amazon website. It takes the link to Amazon product and checks whether its price is lower than the threshold price that the user sets. If it is, the user will receive an email about low price alert with the link to that product and they will know that they can buy it. The email is sent using **SMTP** module.

## If you want to use it
You have to specify the following:
- **headers** (the code needs to send the headers in order to get a valid response from the website, your headers can be viewed here [your headers](https://myhttpheader.com/)) You have to specify at least the following : User-Agent, Accept-Language
- **sender email and password**
- **receiver email**

## Problems
Sometimes the code throws an exception because it cannot find the price element on the website. This happens when Amazon does not allow you to access their website with your code. You can try again or add some additional parameters to **_headers_** section.
