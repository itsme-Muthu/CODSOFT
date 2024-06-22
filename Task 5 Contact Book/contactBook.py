# Creating contact book using file handling (binary file) in python.

import pickle

# inserting record
def insertRecord():
    name = input("Enter the name of the Person: ")
    phoneNum = int(input("Enter the phone number: "))
    email = input("Enter the email id: ")
    address = input("Enter the address :")

    record = {'Name':name,"Phone Number":phoneNum,"Email Id":email,"Address":address}

    file = open("C:/Users/Admin/Downloads/contactBook.dat","ab")
    pickle.dump(record,file)
    print("The contact has been inserted successfully!")
    file.close()

# reading record
def readRecord():
    file = open("C:/Users/Admin/Downloads/contactBook.dat","rb")
    print("==============================================================================")
    print("Contact Book Records:")
    print("==============================================================================")
    print("{:<15} {:<15}".format("Name","Phone Number"))
    print("----------------------------------------------------------------------------")
    while True:
        try:
            record = pickle.load(file)
            print("{:<15} {:<15}".format(record["Name"],record["Phone Number"]))
            print("----------------------------------------------------------------------------")
        except EOFError:
            break
    file.close()

# searching record
def searchRecord(searchcontact):
    file = open("C:/Users/Admin/Downloads/contactBook.dat","rb")
    searching = False
    while True:
        try:
            record = pickle.load(file)
            if record["Name"].lower() == searchcontact.lower() or str(record["Phone Number"]) == searchcontact:
                print("Details of the searched contact: ")
                print("-----------------------------------")
                print("Name :",record["Name"])
                print("Phone Number :",record["Phone Number"])
                print("Email Id :",record["Email Id"])
                print("Address :",record["Address"])
                searching = True
        
        except EOFError:
            break
    if searching == False:
        print("No Record Found !")
    file.close()

# delete record
def deleteRecord(contactDelete):
    file = open("C:/Users/Admin/Downloads/contactBook.dat","rb")
    rec = []
    deleted = False
    while True:
        try:
            record = pickle.load(file)
            rec.append(record)
        except EOFError:
            break

    file.close()

    file = open("C:/Users/Admin/Downloads/contactBook.dat","wb")
    for x in rec:
        if x["Name"].lower()==contactDelete.lower():
            ch = input("Are you sure? (y/n): ")
            if ch in "Yy":
                print("The contact has been deleted successfully")
                deleted = True
                continue
            else:
                deleted = True
        pickle.dump(x,file)
    if deleted == False:
        print("The contact is not found!")
    file.close()

# update record
def updateRecord(contactUpdate,numberUpdate):
    file = open("C:/Users/Admin/Downloads/contactBook.dat","rb")
    rec = []
    updated = False
    while True:
        try:
            record = pickle.load(file)
            rec.append(record)
        except EOFError:
            break
    file.close()
    for i in range(len(rec)):
        if rec[i]["Name"].lower()==contactUpdate.lower():
            rec[i]["Phone Number"]=numberUpdate
            print("The number has been updated")
            updated = True
    if updated == False:
        print("The contact is not found!")
    file = open("C:/Users/Admin/Downloads/contactBook.dat","wb")
    for x in rec:
        pickle.dump(x,file)
    file.close()

# main function

def main():
    while True:
        print("==========================================================================")
        print('Option Available: ')
        print("==========================================================================")
        print("1. Enter a contact ")
        print("2. Display contact ")
        print("3. Search a contact ")
        print("4. Delete a contact ")
        print("5. Update a contact ")
        print("6. Exit")
        print("==========================================================================")

        choice = int(input("Enter the choice (1/2/3/4/5/6): "))

        if choice == 1:
            insertRecord()

        elif choice == 2:
            readRecord()

        elif choice == 3:
            searchcontact = input("Enter the contact details to be searched: ")                    
            searchRecord(searchcontact)

        elif choice == 4:
            contactDelete = input("Enter the contact Details to be deleted: ")
            deleteRecord(contactDelete)

        elif choice == 5:
            contactUpdate = input("Enter the contact Details to be updated: ")
            numberUpdate = int(input("Enter the new number: "))
            updateRecord(contactUpdate,numberUpdate)

        elif choice == 6:
            print("==========================================================================")
            print("You have exited from contact Book")
            print("Thank you!")
            print("==========================================================================")
            break

main()


    
