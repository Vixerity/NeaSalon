import json #Enables better storage and transfer of data.
import utils #Allows for validation of service.
import clients #Enables linking of clients and appointments.
import re #Allows for more efficient validation of code

def add():
    client = clients.find()
    i = int(input("Enter the number of the client that you want to view: "))
    client = clients.clients[i-1]#uses the input from the user to find the client they want to view.  
    date_pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{4})$" #Had to look up regex pattern to Validate Date.
    date = utils.validate("Enter appointment date (DD/MM/YYYY): ", lambda x: re.match(date_pattern, x) is not None) #Displayed as DD/MM/YYYY to allow the user to more efficiently understand what it requires for date.
    time_pattern = r"^([01][0-9]|2[0-3]):([0-5][0-9])$" #Had to look up regex pattern to Validate Time of day
    time = utils.validate("Enter appointment time (HH:MM): ", lambda x: re.match(time_pattern, x) is not None) #Displayed as HH:MM to allow the user to more efficiently understand what it requires for time.
    service = utils.validate("Service: ", lambda x: x != "")
    appointments.append({"client_id": client['id'], "date": date, "time": time, "service": service})
    save()

def delete():
     view()
     appointment = find()
     if appointment == None:
         print("Appointment not found in database, returning to menu")
         return    
     appointments.remove(appointment)
     print("Appointment deleted successfully.")
     save()

def edit():
     view()
     appointment = find()
     if appointment == None:
        print("Appointment not found in database, returning to menu")
        return 
     appointment['date'] = utils.validate("Date: ", lambda x: x != "", appointment["date"])
     appointment['time'] = utils.validate("Time: ", lambda x: x != "", appointment["time"])
     appointment['service'] = utils.validate("Service: ", lambda x: x != "", appointment["service"])
     save()

def find():
     date = utils.validate("\nWhat Date?: ", lambda x: x != "")
     time = utils.validate("What Time?: ", lambda x: x != "")
     for appointment in appointments:
        if appointment["date"] == date and appointment["time"] == time:
                return appointment
  
def save():
    with open('appointments.json', 'w') as file:
        json.dump(appointments, file, indent= 2)

with open('appointments.json', 'r') as file:
    appointments = json.loads(file.read())


def view():
    clients.find()
    i = int(input("Enter the number of the client that you want to view: "))
    client = clients.clients[i-1]#uses the input from the user to find the client they want to view.
    print("\nCustomer Name: {} {}".format(client['first_name'], client['last_name']))
    print("\nDate\t\tTime\tService")
    for appointment in appointments:
        if appointment["client_id"] == client["id"]:
            print("{}\t{}\t{}".format(appointment['date'], appointment['time'], appointment['service']))
# This function displays all appointments for a specific client.
