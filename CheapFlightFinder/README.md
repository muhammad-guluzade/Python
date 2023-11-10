# Cheap Flights Finder

## What is this program?
This program is designed to have an excel sheet of **users with their emails stored**, and another excel sheet, where **some airports in some cities are stored**. The program finds **cheapest flights** to the airports listed in excel sheet from a **certain airport (in this case, hardcoded GYD airport)**, and then alerts everyone who's in the excel sheet if the cheap flight was found. 

## How it works?

This program asks the user to enter his full name and email, and then uses sheety API to add this user to an excel sheet. After that, the program accesses another excel sheet using sheety API and finds the cheapest flights from particular city to some airports, which are listed in this excel sheet. The program finds the flights using tequila API. Next, when the cheapest flights are found, the program opens users excel sheet again and iterates through all emails in order to send the message about cheapest flights to certain airports.

## If you want to use it
- You need to register in tequila and receive a web token to access tequila API
- You need to use your own email and password to send emails
- You need to have your own excel sheet of users with their emails, or use your own email in the code to receive an alert
