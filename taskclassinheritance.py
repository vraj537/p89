class train:
    # Corrected constructor name: __init__
    def __init__(self, tno, source, destination, tickets, price):
        self.tno = tno
        self.source = source
        self.destination = destination
        self.tickets = tickets
        self.price = price

class customer:
    # Corrected constructor name: __init__
    def __init__(self, no, name, contact, email):
        self.no = no
        self.name = name
        self.contact = contact
        self.email = email

# Correct class name for clarity in the instance call below
class Booking(train, customer):
    # Corrected constructor name: __init__
    def __init__(self, tno, source, destination, tickets, price, no, name, contact, email):
        # Correctly call parent class constructors with 'self'
        customer.__init__(self, no, name, contact, email)
        train.__init__(self, tno, source, destination, tickets, price)

    def menu(self):
        print("\nTRAIN MENU")
        print("1) View Train")
        print("2) Book Train")
        print("3) Confirm booking")
        print("4) To cancel procedure")
        
        # Use a more descriptive variable for the current booking instance
        current_booking = self
        
        try:
            opt = int(input("Enter choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            current_booking.menu() # Re-call menu if input is invalid
            return
            
        match opt:
            case 1:
                print("\n--- Train Details ---")
                print("Train Number:", current_booking.tno)
                print("From:", current_booking.source)
                print("Destination:", current_booking.destination)
                print("Available Tickets:", current_booking.tickets)
                print("Price:", current_booking.price)
                current_booking.menu()
            case 2:
                print("Press 3 to confirm ticket")
                current_booking.menu()
            case 3:
                print("Your Ticket is booked successfully!")
            case 4:
                print("Cancellation procedure started (Not fully implemented).")
            case _:
                print("Invalid choice. Please select 1, 2, 3, or 4.")
                current_booking.menu()

    def display(self):
        print(self.tno, self.source, self.destination, self.tickets, self.price)
        print(self.no, self.name, self.contact, self.email)

# --- Instantiation and Execution ---
# 1. Instantiate the 'Booking' class (renamed to Booking for convention)
# 2. Pass all 9 required arguments (5 for train, 4 for customer)
# 3. Call the 'menu' method on the booking object.
obj = Booking(tno=10, source='a', destination='b', tickets=123, price=100000,no=12345,name='ayush',contact='989998', email='ay@mail')
obj.menu()
