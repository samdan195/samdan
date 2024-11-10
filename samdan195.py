import datetime

# List of valid stations (example list)
valid_stations = ["Central", "North", "South", "East", "West"]

# Function to validate the ticket type
def validate_ticket_type(ticket_type):
    valid_types = ['single', 'return', 'day pass']
    if ticket_type.lower() in valid_types:
        return True
    print("Invalid ticket type. Please choose 'single', 'return', or 'day pass'.")
    return False

# Function to validate station name
def validate_station(station_name):
    if station_name in valid_stations:
        return True
    print(f"Invalid station: {station_name}. Please enter a valid station name.")
    return False

# Function to validate date
def validate_date(date_text):
    try:
        date = datetime.datetime.strptime(date_text, '%Y-%m-%d')
        if date >= datetime.datetime.now():
            return True
        else:
            print("The date must be in the future.")
            return False
    except ValueError:
        print("Incorrect date format, should be YYYY-MM-DD.")
        return False

# Function to display a booking summary
def display_summary(ticket_type, start_station, destination_station, travel_date):
    print("\n--- Booking Summary ---")
    print(f"Ticket Type: {ticket_type.capitalize()}")
    print(f"From: {start_station}")
    print(f"To: {destination_station}")
    print(f"Date of Travel: {travel_date}")
    print("-----------------------")

# Main function to run the ticket booking process
def book_ticket():
    print("Welcome to Centrala Underground Ticketing System!\n")
    
    # Step 1: Select ticket type
    ticket_type = input("Select ticket type (single/return/day pass): ").strip().lower()
    if not validate_ticket_type(ticket_type):
        return
    
    # Step 2: Enter journey details
    start_station = input("Enter start station: ").strip().capitalize()
    if not validate_station(start_station):
        return

    destination_station = input("Enter destination station: ").strip().capitalize()
    if not validate_station(destination_station):
        return

    # Check that the start and destination stations are different
    if start_station == destination_station:
        print("Start and destination stations must be different.")
        return

    # Step 3: Enter and validate travel date
    travel_date = input("Enter travel date (YYYY-MM-DD): ").strip()
    if not validate_date(travel_date):
        return

    # Step 4: Confirm booking
    display_summary(ticket_type, start_station, destination_station, travel_date)
    confirmation = input("\nConfirm booking? (yes/no): ").strip().lower()
    if confirmation == 'yes':
        print("Booking confirmed! Thank you for using Centrala Underground.")
    else:
        print("Booking cancelled.")

# Run the booking system
if __name__ == "__main__":
    book_ticket()
