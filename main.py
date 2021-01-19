import pandas as pd
import csv 
import random
import datetime as dt
import smtplib


# import letters to use 
letters = ['letters/letter_1.txt', 'letters/letter_2.txt',
           'letters/letter_3.txt', 'letters/letter_4.txt']


# allow user to add birthdays via function call
def add_birthday(name, email, birthday):
    """Add new birthday in format: NAME, EMAIL, MM-DD"""
    new_birthday = [name, email, birthday]
    with open('birth_dates.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(new_birthday)


def edit_letter(data):
    # retrieve target name and email
    name = data.iloc[0]["NAME"]
    recipient = data.iloc[0]["EMAIL"]
    letter = random.choice(letters)
    letter_string = ""
    with open(letter, "r") as f:
        content = f.readlines()
        for line in content:
            letter_string += line
    final_letter = letter_string.replace("[NAME]", str(name))
    send_letter("email.com", "password", recipient, final_letter)


def send_letter(email, password, recipient, message):
    """Send an email birthday message """
    with smtplib.SMTP("smtp.gmail.com") as conn:
        conn.starttls()
        conn.login(user=email, password=password)
        conn.sendemail(from_addr=email, to_addrs=recipient,
                       msg=f"Subject:Happy Birthday!\n\n{message}")


# create a dataframe from birthday csv data
birthday_df = pd.read_csv('birthdays/birth_dates.csv')

# check if todays date is in df, if so, send birthday message 
now = dt.datetime.now()
today = f"0{now.month}-{now.day}"
if today in birthday_df['BIRTHDAY']:
    bd_data = birthday_df.loc[birthday_df['BIRTHDAY'] == str(today)]
    edit_letter(bd_data)
