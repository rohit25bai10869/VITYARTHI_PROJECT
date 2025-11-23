import random
import time

# I made this booking system for railway tickets
# some parts might not be perfect but it works

def calculate_fare(km, age, coach_type):
    # base calculation per km
    price = km * 1.52
    
    # coach wise pricing (I checked online for rough idea)
    if coach_type == "SL":
        price = price * 1.4
    elif coach_type == "3AC":
        price = price * 2.2
    elif coach_type == "2AC":
        price = price * 3.0
    elif coach_type == "1AC":
        price = price * 4.5
    elif coach_type == "GEN":
        price = price * 1.0
    elif coach_type == "ECN":
        price = price * 1.2
    else:
        print("Coach type not found, using general coach price")
        price = price * 1.0
    
    # age discounts
    if age < 12:
        price = price * 0.5    # children get half price
    if age > 60:
        price = price * 0.7    # senior citizens discount
    
    return int(price)


def book_ticket():
    print("\n--- Railway Ticket Booking System ---\n")
    
    # taking passenger details
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    from_station = input("From Station: ")
    to_station = input("To Station: ")
    distance = int(input("Enter Distance (in km): "))
    
    # date input
    journey_date = input("Journey Date (DD-MM-YYYY): ")
    
    # coach selection
    print("\nAvailable Coach Types:")
    print("SL - Sleeper")
    print("3AC - AC 3 Tier")
    print("2AC - AC 2 Tier")
    print("1AC - AC 1 Tier")
    print("GEN - General")
    print("ECN - Economy")
    selected_coach = input("\nEnter Coach Type: ").upper()
    
    # random time generation (I thought it would be realistic)
    random_hour = random.randint(0, 23)
    random_minute = random.randint(0, 59)
    
    # format time properly
    if random_minute < 10:
        journey_time = str(random_hour) + ":0" + str(random_minute)
    else:
        journey_time = str(random_hour) + ":" + str(random_minute)
    
    # calculate total fare
    total_fare = calculate_fare(distance, age, selected_coach)
    
    # generate PNR number (10 digit random)
    pnr_no = random.randint(1000000000, 9999999999)
    
    print("\nProcessing your booking...")
    time.sleep(1)
    
    # display ticket
    print("\n****************************************")
    print("          RAILWAY TICKET")
    print("****************************************")
    print("PNR Number    :", pnr_no)
    print("Date          :", journey_date)
    print("Time          :", journey_time)
    print("Passenger Name:", name)
    print("Age           :", age)
    print("From          :", from_station)
    print("To            :", to_station)
    print("Distance      :", distance, "km")
    print("Coach Type    :", selected_coach)
    print("Total Fare    : Rs.", total_fare)
    print("****************************************\n")
    
    # save ticket in file
    ticket_file = open("railway_tickets.txt", "a")
    line = str(pnr_no) + "," + journey_date + "," + journey_time + "," + name + "," + str(age) + "," + from_station + "," + to_station + "," + str(distance) + "," + selected_coach + "," + str(total_fare) + "\n"
    ticket_file.write(line)
    ticket_file.close()
    
    print("Ticket saved successfully!\n")


# main program starts here
print("=" * 40)
print("  Welcome to Railway Booking System")
print("=" * 40)

while True:
    print("\nMenu:")
    print("1. Book a New Ticket")
    print("2. Exit")
    
    user_choice = input("\nEnter your choice: ")
    
    if user_choice == "1":
        book_ticket()
    elif user_choice == "2":
        print("\nThank you for using our system!")
        print("Have a safe journey :)")
        break
    else:
        print("Invalid choice! Please enter 1 or 2\n")