import pandas as pd
df = pd.read_csv('hotels.csv', dtype={'id': str})

class Hotel:
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df['id'] == self.hotel_id,'name'].squeeze()
        self.location = df.loc[df['id'] == self.hotel_id,'city'].squeeze()
        self.type = df.loc[df['id'] == self.hotel_id,'type'].squeeze()

    def available(self):
        """Check if the hotel is available"""
        availability = df.loc[df['id'] == self.hotel_id,'available'].squeeze()
        if availability == 'yes':
            return True
        else:
            return False
    
    def book_hotel(self):
        """Book a room by changing its availability"""
        df.loc[df['id'] == self.hotel_id,'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

class Reservation_Ticket:
    def __init__(self, customer_name, hotel_name, room_type):
        self.customer_name = customer_name
        self.hotel_name = hotel_name
        self.room_type = room_type

    def generate_ticket(self):
        content = f"""
        Dear {self.customer_name.capitalize()}.
        
        On behalf of {self.hotel_name}, we want to express our heartfelt appreciation for choosing to book your upcoming stay with us. We can not wait to welcome you to our luxurious property and provide you with an unforgettable experience.
        
        Your booking details are confirmed for April-28-2024 to May-3-2024 in our {self.room_type.title()}. If you have any special requests or preferences, please do not hesitate to let us know, and we will do our best to accommodate them.
        """
        return content

class Spa_Package(Reservation_Ticket):
    def generate_ticket(self):
        content = f"""
        Dear {self.customer_name.capitalize()}.
        
        On behalf of {self.hotel_name}, we want to express our heartfelt appreciation for choosing to book your upcoming stay with us, with a special spa package service. We can not wait to welcome you to our luxurious property and provide you with an unforgettable experience.
        
        Your booking details are confirmed for April-28-2024 to May-3-2024 in our {self.room_type.title()}, with the special spa and beauty care service. If you have any special requests or preferences, please do not hesitate to let us know, and we will do our best to accommodate them.
        """
        return content

df_cards = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')
class CreditCard:
    def __init__(self, card_number):
        self.card_number = card_number
        # self.holder_name = df.loc[df['card_number'] == self.card_number, 'holder_name']
        # self.card_expiration = df.loc[df['card_number'] == self.card_number, "expiration"].squeeze()
        # self.card_cvc = df.loc[df['card_number'] == self.card_number, "cvc"].squeeze()

    def validate(self, holder_name, card_expiration, card_cvc):
        card_data = {'number': self.card_number,
                     'holder': holder_name,
                     'expiration': card_expiration,
                     'cvc': card_cvc}
        if card_data in df_cards:
            return True
        else:
            return False

df_card_security = pd.read_csv('card_security.csv', dtype=str)        
class Secure_Credit_Cards(CreditCard):
    def authenticate(self, given_password):
        password = df_card_security.loc[df_card_security['number'] == self.card_number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False

print(df)
if __name__ == "__main__":
    hotel_ID = input("Please select id of hotels that you want to check for the availability '134', '188', or '655 ")
    hotel = Hotel(hotel_id=hotel_ID)
    hotel.available()
    if hotel.available():
        credit_card = Secure_Credit_Cards(card_number="4489")
        if credit_card.validate(holder_name="ANGELA YU", card_expiration="12/29",card_cvc="789"):
            if credit_card.authenticate(given_password="mypassword"):
                hotel.book_hotel()
                name = input("Please provide your name: ")
                reserve_hotel =Reservation_Ticket(customer_name=name, hotel_name=hotel.name, room_type=hotel.type)
                print(reserve_hotel.generate_ticket())
                spa_package = input("Do you want to include our special spa package to the booking? ")
                if spa_package == "yes":
                    spa_service = Spa_Package(customer_name=name, hotel_name=hotel.name, room_type=hotel.type)
                    print(spa_service.generate_ticket())
                else:
                    print(reserve_hotel.generate_ticket())
            else:
                print("Credit card authentication failed!")
        else:
            print("There was a problem with the information of your credit card that you provided!")
    else:
        print("Hotel is full!")