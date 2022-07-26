#program for phonebook with contacts

contacts = {}
exit = True

while exit == True:
    ans = input("Phonebook Options: " 
                "\nA. To add a new contact"
                "\nB. To retreive a contact's details"
                "\nC. To remove a contact"
                "\nD. To display all the contacts"
                "\nE. Exit"
                "\nPlease choose an option to access the phonebook: ")

    if ans == 'A' or ans == 'a':
        new_cont = input("To add a new contact - Enter the name: ")
        info = input("Enter the contact's phone number and email address: ")
        contacts[new_cont] = info
        exit = True

    elif ans == 'B' or ans == 'b':
        get_cont = input("To retreive a contact's details - Enter the contact's name: ")
        if get_cont in contacts:
            print(contacts[get_cont])
        else:
            print("This contact is not in the phonebook, please choose another option.")
        exit = True

    elif ans == 'C' or ans == 'c':
        remove_cont = input("To remove a contact - Enter the contact's name: ")
        del contacts[remove_cont]
        exit = True

    elif ans == 'D' or ans == 'd':
        print(contacts)
        
    else:
        exit = False
