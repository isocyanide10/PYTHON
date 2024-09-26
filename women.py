from twilio.rest import Client
import mysql.connector

# Twilio credentials
ACCOUNT_SID = 'your_account_sid'
AUTH_TOKEN = 'your_auth_token'
TWILIO_PHONE_NUMBER = '+your_twilio_number'

# Connect to the MySQL database
def get_logged_in_users_phone_numbers():
    # Database connection details
    db = mysql.connector.connect(
        host="localhost",  # Replace with your DB host
        user="root",  # Replace with your DB user
        password="password",  # Replace with your DB password
        database="your_database"  # Replace with your DB name
    )
    
    cursor = db.cursor()

    # SQL query to fetch phone numbers of logged-in users
    query = "SELECT phone_number FROM users WHERE is_logged_in = 1"  # Assuming `is_logged_in` is a flag indicating logged-in status
    cursor.execute(query)
    
    # Fetch all phone numbers
    phone_numbers = [row[0] for row in cursor.fetchall()]
    
    cursor.close()
    db.close()
    
    return phone_numbers

# Function to send SMS using Twilio
def send_bulk_sms(phone_numbers, message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    for number in phone_numbers:
        try:
            message = client.messages.create(
                body=message,
                from_=TWILIO_PHONE_NUMBER,
                to=number
            )
            print(f"Message sent to {number}, SID: {message.sid}")
        except Exception as e:
            print(f"Failed to send message to {number}: {str(e)}")

# Main function
def main():
    # Message to send
    message = "This is a test alert message to all logged-in users."

    # Fetch logged-in user phone numbers
    phone_numbers = get_logged_in_users_phone_numbers()
    
    if phone_numbers:
        # Send SMS to all fetched numbers
        send_bulk_sms(phone_numbers, message)
    else:
        print("No logged-in users found.")

if __name__ == "__main__":
    main()