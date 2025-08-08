
# Contact Management App
A simple command-line contact management application written in Python using SQLite for persistent data storage. This app allows users to create, view, search, update, and delete contact records.



## Features

- Add new contacts with name, phone number, and email address
- View all saved contacts
- Search for contacts by name
- Update existing contact information
- Delete contacts from the database 


## Installation

Python 3.x installed on your machine

Clone the repository or download the contact_app.py file.

Run the Python script: The script will automatically create a contact.db SQLite database file if it doesn't already exist.
    
## File Structure

contact_app.py   # Main script containing all functions for managing contacts
contact.db       # SQLite database (auto-created)

## Usage
- create_table() – Initializes the database with a contacts table
- add_contact(name, phone, email) – Adds a new contact
- view_contact() – Prints all stored contacts
- search_contact(name) – Returns contacts that match the search term
- Update_contact(name, phone, email, contact_id) – Updates contact by ID

## Example

from contact_app import *

create_table()
add_contact("Alice", "123-456-7890", "alice@example.com")
print(search_contact("Alice"))
view_contact()
update_contact("Alice Smith", "987-654-3210", "alice@newmail.com", 1)

## Note

- Make sure the contact ID is known before updating a record.

- Error handling is minimal—consider adding checks for production use.


## License

This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/)

