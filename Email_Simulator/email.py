### --- OOP Email Simulator --- ###
""" 
This script simulates an email inbox system using Object-Oriented 
Programming (OOP) concepts. 
Users can read emails, view unread emails, and quit the application.
"""
class Email():    
    """Create the class, constructor and methods to create a new Email 
    # object."""
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    # Declare the class variable, with default value, for emails. 
    has_been_read = False
    
    def mark_as_read(self):
        """# Create the method to change 'has_been_read' emails from False to 
            # True."""
        self.has_been_read == True
    
# Initialise an empty list to store the email objects.
inbox = []

def populate_inbox():
    """# Create 3 sample emails and add it to the Inbox list."""
    email1 = Email(
        "john.doe@example.com", "Meeting Agenda for Next Week",
        """Hi team, I've attached the agenda for our meeting next 
        eek. Please review it and let me know if there are any 
        topics you'd like to add or discuss. Thanks!"""
    )
    email2 = Email(
        " mary.smith@example.com", "Invitation to Company Event",
        """Dear colleagues, You're invited to our company's annual picnic 
        on Saturday. Please RSVP by Friday if you plan to attend. We look 
        forward to seeing you there!"""
    )
    email3 = Email(
        "david.jones@example.com", 
        "Important Update: Project Deadline Extended",
        """Hi everyone, Due to unforeseen circumstances, we've decided to 
        extend the deadline for the project by one week. Please take this 
        extra time to ensure the quality of your work. Thank you for your 
        understanding."""
    )
    inbox.extend([email1, email2, email3])

def list_emails():
    """# Create a function which prints the email’s subject_line, along 
    # with a corresponding number."""
    for i, email in enumerate(inbox):
        if not email.has_been_read:
            print(f"{i+1} [UNREAD] {email.subject_line}")
        else:
            print(f"{i+1} {email.subject_line}")

def read_email(index):
    """# Create a function which displays a selected email."""
    if 0 < index <= len(inbox):
        email = inbox[index-1]
        print(f"From: {email.email_address}")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        # Once displayed, call the class method to set its 
        # 'has_been_read' variable to True.
        email.mark_as_read()
    else:
        print("Invalid email index")

# Call the function to populate the Inbox for further use in your 
# program.
populate_inbox()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # 
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
        
    elif user_choice == 2:
        # 
        list_emails()
            
    elif user_choice == 3:
        # 
        print("Exiting application.")
        break
    else:
        print("Oops - incorrect input.")
