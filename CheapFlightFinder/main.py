import requests
import datetime as dt
from datetime import timedelta
import smtplib



# code that HAS TO BE CHANGED -->



# ==========================

# url of the google sheet, you can either use this one or use your own
sheety_url_to_create_rows_for_flights = "https://api.sheety.co/7a5ff8bcf6a27b16eef1db60f1915888/aeroports/prices"

# api key needed to be obtained from tequila website
flights_api_key = ""

# endpoint in tequila API to search for flights
flights_endpoint = "https://api.tequila.kiwi.com/v2/search"

# email and password to be able to send emails
USER = ""
PASSWORD = ""

# headers for flights API, which only consist of an API key
headers_for_flights = {
    "apikey": flights_api_key
}

# ==========================



# code that DOES NOT HAVE TO BE CHANGED -->



# headers for sheety
headers_for_sheety = {
    "Content-Type": "application/json"
}


# this is the main function that will search for the flights using tequila API
# it searches for flights with the relevant price and, if found, concatenates
# the flight details to message that's going to be sent
# ==========================
def get_flights():
    # getting rows from the table
    response = requests.get(url=sheety_url_to_create_rows_for_flights)
    messages_list = []

    for item in response.json()["prices"]:
        params_for_flights = {
            "fly_from": "GYD",
            "fly_to": item["iataCode"],
            "date_from": dt.datetime.today().strftime("%d/%m/%Y"),
            "date_to": (dt.datetime.today() + timedelta(days=(6 * 30))).strftime("%d/%m/%Y"),
            "curr": "USD",
            "price_to": item["price"],
            "max_stopovers": 3,
            "nights_in_dst_from": 2,
            "nights_in_dst_to": 4,
            "flight_type": "round",
            "one_for_city": 1
        }
        flights_response = requests.get(url=flights_endpoint,
                                        params=params_for_flights,
                                        headers=headers_for_flights)
        flights_response.raise_for_status()

        for flight in flights_response.json()["data"]:
            if flight["price"] <= item["price"]:
                message = f"Low price alert!\nOnly {flight['price']}$ to fly " \
                          f"from Baku (GYD) to {item['city']}({flight['flyTo']})\n" \
                          f"from {flight['route'][0]['local_departure'].split('T')[0]} " \
                          f"to {flight['route'][1]['local_departure'].split('T')[0]}\n" \
                          f"Link\n{flight['deep_link']}"
                messages_list.append(message)
    return messages_list
# ==========================

# The user registration
# User inputs their full name and email and gets added to another
# sheet in sheety consisting of users, their full names, and emails
# ==========================
print("Welcome to cheap flights finder!")
first_name = input("Enter your first name: ").title()
last_name = input("Enter your last name: ").title()
email = input("Plase enter your email: ").strip().lower()
# ==========================

# sheety API url to add a new user
# ==========================
sheety_url_to_create_rows_for_users = "https://api.sheety.co/7a5ff8bcf6a27b16eef1db60f1915888/aeroports/users"
# ==========================

# parameters to add new user
# ==========================
params_for_user = {
    "user": {
        "firstName": first_name,
        "lastName": last_name,
        "email": email
    }
}
# ==========================

# adding a new user using POST request
# ==========================
response = requests.post(url=sheety_url_to_create_rows_for_users,
                         json=params_for_user,
                         headers=headers_for_sheety)
response.raise_for_status()
# ==========================

print("You have successfully been added to the database, please wait for the email to come!")

# GET request to a sheet of users in order to obtain all emails
# ==========================
response = requests.get(url=sheety_url_to_create_rows_for_users)
# ==========================

# getting the flights and their details
# ==========================
msg_list = get_flights()
# ==========================

# for loop that sends email to each registered user
# ==========================
for user in response.json()["users"]:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        for message in msg_list:
            connection.sendmail(from_addr=USER, to_addrs=user['email'],
                                msg=f"Subject:Low price alert!\n\n{message}")
# ==========================
