# Instance variables vs Class variables
import pandas as pd
df = pd.read_csv('hotels.csv', dtype={'id': str})

class Hotel:
    watermark = "Equitable Property Group Ltd"
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

    # Class methods
    @classmethod
    def get_num_of_hotels(cls, data):
        return len(data)
    
    # Magic methods
    def __eq__(self):
        if self.hotel_id == self.hotel_id:
            return True
        else:
            return False
        
class Ticket(ABC):
    def generate(self):
        pass

class Reservation_Ticket(Ticket):
    def __init__(self, customer_name, hotel_name, room_type):
        self.customer_name = customer_name
        self.hotel_name = hotel_name
        self.room_type = room_type

    def generate_ticket(self):
        content = f"""
        Dear {self.the_customer_name}.
        
        On behalf of {self.hotel_name}, we want to express our heartfelt appreciation for choosing to book your upcoming stay with us. We can not wait to welcome you to our luxurious property and provide you with an unforgettable experience.
        
        Your booking details are confirmed for April-28-2024 to May-3-2024 in our {self.room_type.title()}. If you have any special requests or preferences, please do not hesitate to let us know, and we will do our best to accommodate them.
        """
        return content
    
    @property
    def the_customer_name(self):
        name = self.customer_name.strip()
        name = name.title()
        return name
    
    @staticmethod
    def convert(amount):
        return amount * 1.2

class Digital_Ticket(Ticket):
    def generate(self):
        return "Here is your tokenized ticket"
    
    def download(self):
        pass
hotel = Hotel(hotel_id="134")
# Class variables
print(hotel.watermark)

# Instance variables
print(hotel.name)

# Instance methods
print(hotel.available())

# Class methods
print(Hotel.get_num_of_hotels(data=df))
ticket = Reservation_Ticket(customer_name="Angela", hotel_name=hotel.name, room_type=hotel.type)
print(ticket.the_customer_name)
print(ticket.generate_ticket())

print(Reservation_Ticket.convert(10))