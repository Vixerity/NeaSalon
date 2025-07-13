import json #Had to research more efficient ways of storing and displaying data.
import uuid #Used to generate a unique ID to link clients and their appointments.
import utils #Different name for my validation function.
import re #Required a more efficient way to validate complex strings.

def add():
    first_name = utils.validate("First Name: ", lambda x: x != "")
    last_name = utils.validate("Last Name: ", lambda x: x != "")
    allergy = utils.validate("Allergy (Can leave this blank): ", lambda x: True)  # Allow blank input.
    if allergy == None:
         allergy = "None"
    email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$" #Had to look up regex pattern to Validate Email.
    email = utils.validate("Enter your email: ", lambda x: re.match(email_pattern, x) is not None)
    phone_pattern = r"^\s*\d{10,15}\s*$" #Had to look up regex pattern to Validate Phone Number.
    raw_phone = utils.validate("Enter your phone number: +44 ", lambda x: re.match(phone_pattern, x.replace(" ", "")) is not None)
    phone_number = "+44" + raw_phone.replace(" ", "")
    address = utils.validate("Address: ", lambda x: x != "")
    id = uuid.uuid4() #Assigns an ID to the clients, to enable appointment linking.
    clients.append({"id": str(id), "first_name": first_name, "last_name": last_name,"allergy": allergy,"email": email, "phone_number": phone_number,"address": address })
    save()

def save():
    with open('clients.json', 'w') as file:
        json.dump(clients, file, indent= 2) #Saves the information to a file called clients.json

with open('clients.json', 'r') as file:
   clients = json.loads(file.read()) #Allows the JSON file to be read

def find():
      print("\nNumber\tName")
      for i, client in enumerate(clients, start=1):
        print("{}\t{} {}".format(i,client['first_name'],client['last_name']))

def details():
     find()
     i = int(input("Enter the number of the client that you want to view: "))
     client = clients[i-1]
     print("\nName:{} {}\nAddress:\t{}\nPhone:\t\t{}\nEmail:\t\t{}\nAllergy:\t{}".format(client['first_name'],client['last_name'],client['address'],client['phone_number'],client['email'],client['allergy']))
     #Displays client information in a clean and understandable format

