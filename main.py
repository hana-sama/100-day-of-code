import smtplib
import datetime as dt
from random import choice

my_email = ""
password = ""

now = dt.datetime.now()
week_of_day = now.weekday()

weekday = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def pick_quote():
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = choice(all_quotes)
    return quote

if week_of_day == 0:
     quote = pick_quote()
     with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="",
            msg=f"Subject:Welcome to {weekday[week_of_day]}\n\n{quote}"
        )
elif week_of_day == 2:
    quote = pick_quote()
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="ys.seki@nifty.com",
            msg=f"Subject:Welcome to {weekday[week_of_day]}\n\n{quote}"
            )

else:
    print("Sorry, there is no quote to send today!")
            

