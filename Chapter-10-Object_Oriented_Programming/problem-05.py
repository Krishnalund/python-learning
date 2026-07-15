#  Write a Class ‘Trainʼ which has methods to book a ticket, get status (no of seats) and get
# fare information of train.

class Train:
    def __init__(self, name , seats , fare):
        self.name = name
        self.seats = seats
        self.fare = fare
        
    def get_status(self):
        print('Train name:', self.name)
        print('Available seats:', self.seats)

    def get_fare(self):
        print(f"Fare: Rs. {self.fare}")

    def book_ticket(self):
        if self.seats > 0:
            self.seats-=1
            print('Ticket booked successfully!')
        else:
            print('Sorry! No seats available')

train_obj = Train('Railways', 100 , 1500)
train_obj.get_status()
train_obj.get_fare()
train_obj.book_ticket()


