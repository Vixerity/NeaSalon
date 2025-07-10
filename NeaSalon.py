import clients #Split clients and appointments into seperate modules for more efficient work.
import appointments #Enables more concise and readable code to be made.

def menu():
    while True:
        print("\nWelcome to Elegant Hair styles Salon!")
        option = input("1.Enter client details\n2.Enter appointment details\n3.Delete appointment\n4.View all clients\n5.View an appointment\n6.Edit appointments\n7.Exit\nEnter choice: ")

        if option == '1':
            clients.add() #Opens the delete function from the appointments module.

        elif option == '2':
            appointments.add() #Opens the add function from the appointments module.

        elif option == '3':
            appointments.delete() #Opens the delete function from the appointments module.

        elif option == '4':
            clients.details() #Opens the view function from the clients module.
            
        elif option == '5':
            appointments.view() #Opens the view function from the appointmens module.

        elif option == '6':
            appointments.edit() #Opens the edit function from the appointments module.

        elif option == '7':
            exit() #Exits the system.

        else:
            print("Not an option. Try again") #sends the user back to the start after an incorrect input.

menu()
