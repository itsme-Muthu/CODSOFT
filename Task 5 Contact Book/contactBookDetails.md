<h2> Task 5: Contact Book </h2>

The provided Python code implements a contact book using file handling with binary files. Here’s a detailed description:

---

<h3>Functionality Overview:</h3>

<h3>Inserting a Record (insertRecord()):</h3>

- Allows the user to input a person's name, phone number, email, and address.
- Stores this information as a dictionary in a binary file (contactBook.dat) using the pickle module.
- Confirms successful insertion of the contact.

<h3>Reading Records (readRecord()):</h3>

- Opens the binary file and displays all stored contacts.
- Prints the name and phone number of each contact in a formatted manner.

<h3>Searching for a Record (searchRecord(searchcontact)):

- Prompts the user to enter either a contact's name or phone number to search for.
- Searches through the binary file for matching records.
- Displays details (name, phone number, email, address) of the contact if found.
- If no match is found, it informs the user accordingly.

<h3>Deleting a Record (deleteRecord(contactDelete)):</h3>

- Takes a contact's name as input and offers confirmation for deletion.
- Removes the matching record from the binary file if confirmed.
- Notifies the user upon successful deletion or if the contact was not found.

<h3>Updating a Record (updateRecord(contactUpdate, numberUpdate)):</h3>

- Prompts the user to enter a contact's name for updating.
- Allows the user to input a new phone number.
- Updates the phone number of the specified contact in the binary file.
- Confirms successful update or informs if the contact was not found.

<h3>Main Function (main()):</h3>

- Displays a menu of options (enter, display, search, delete, update, exit).
- Based on user input, executes the corresponding function for managing contacts.
- Continues until the user chooses to exit the program.

<h3>Purpose:</h3>
The program provides basic functionalities for managing a contact book:

- Adding new contacts.
- Viewing all contacts.
- Searching for specific contacts by name or phone number.
- Deleting contacts.
- Updating contact information.

It utilizes binary file handling with pickle for data storage and retrieval, <b>ensuring persistence across sessions</b>. The menu-driven interface facilitates user interaction, making it straightforward to perform operations on the contact book data.

