##################### Normal Starting Project ######################
import datetime as dt
import pandas as pd
import random
import smtplib
my_email = ""
password = ""

# ---------- Updating birthdays csv ----------#
new_birthday_input = []
def entries(name, email, year, month, day):
    new_entry = {
        "name": name,
        "email": email,
        "year": year,
        "month": month,
        "day": day,
    }

    return new_entry

angela = entries("Angela Yu", "angela@email.com", 1990, 7, 10)
new_birthday_input.append(angela)
hana = entries("Hana", "hana@email.com", 2008, 9, 8)
new_birthday_input.append(hana)
haru = entries("Haru", "haru@email.com", 2016, 3, 26)
new_birthday_input.append(haru)
mum = entries("Mum", "mum@email.com", 1980, 11, 30)
new_birthday_input.append(mum)
yasu = entries("Yasu", "ys.seki@nifty.com", 1965, 12, 6)
new_birthday_input.append(yasu)

data = pd.DataFrame(new_birthday_input)
data.to_csv("birthdays.csv", index=False)

# ---------- Obtaining today's date ---------- #
today = (dt.datetime.now().month, dt.datetime.now().day)

# ---------- Retrieving data from csv file and compare if conditions are matched ---------- #
data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace('[NAME]', birthday_person['name'])
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthday_person['email'],
                msg=f"Subject:Happy Birthday {birthday_person['name']}\n\n{contents}"
            )
else:
    print("Sorry, there are no friends to whom you should send a happy birthday message today!")

# ---------- Sending message via email ---------- #
         


