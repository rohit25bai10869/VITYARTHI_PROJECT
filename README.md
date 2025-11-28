# VITYARTHI_PROJECT
Railway Ticket Booking System (Python)
This is a simple console-based Railway Ticket Booking System written in Python. It allows a user to book railway tickets, calculate fare based on distance, age, and coach type, and save each ticket into a text file as a basic record system.

Project Details
-> Project Title: Railway Ticket Booking System (Console Based)

-> Student Name: Rohit Choudhary

-> Registration Number: 25BAI10869

-> Guide: Prof. Shahana Gazala Qureshi

Features
-> Menu-driven console interface (Book Ticket / Exit).

-> Fare calculation using:

   -> Distance in kilometers.

   -> Age-based discounts (child and senior citizen).

   -> Coach type multipliers (SL, 3AC, 2AC, 1AC, GEN, ECN).

-> Random generation of:

   -> Journey time (HH:MM format).

   -> 10-digit PNR-like number.

-> Nicely formatted ticket display on the console.

-> Ticket details saved to “railway_tickets.txt” in CSV-like format.

-> Technologies Used
   -> Language: Python 3.x

-> Libraries:

   -> random (for time and PNR generation)

   -> time (for processing delay)

-> Platform: Any OS with Python 3 installed

-> How to Run
1. Install Python 3.x on your system.

2. Save the code into a file, for example: railway_booking_system.py.

3. Open terminal/command prompt in the folder where the file is saved.

4. Run the script:

   -> python railway_booking_system.py

5. Use the menu:

   -> Press 1 to book a new ticket.

   -> Press 2 to exit the program.

-> Project Workflow (High Level)
   -> User sees welcome message and menu.

   -> User chooses “Book Ticket”.

   -> User enters personal and journey details.

   -> System:
     -> Generates random journey time.
     -> Calculates fare using distance, age, and coach.
     -> Generates a 10-digit PNR.
     -> Prints a formatted ticket.
     -> Appends ticket data to railway_tickets.txt.

   -> User returns to the menu and can either book again or exit.

Pseudocode (Short Version)
-> Main Menu:

  -> Loop:

   -> Show options (1: Book Ticket, 2: Exit).

   -> If 1 → call book_ticket().

   -> If 2 → thank the user and break.

   -> Else → show “Invalid choice”.

-> book_ticket():

  -> Take user inputs (name, age, from, to, distance, date, coach).

  -> Generate random time.

  -> Call calculate_fare(km, age, coach_type).

  -> Generate random 10-digit PNR.

  -> Print ticket.

  -> Save ticket line to railway_tickets.txt.

-> calculate_fare(km, age, coach_type):

  -> Base price = km * 1.52

  -> Multiply according to coach type.

  -> Apply child discount if age < 12.

  -> Apply senior discount if age > 60.

  -> Return integer fare.
