from Storage import save_contacts,load_contacts
def add_contacts(name,Email,Phone_number, Address):
    Contact=[]
    contacts={
            "name":name,
            "Email":Email,
            "Phone_number": Phone_number,
            "Address":Address,
           "status":"pending" }
    Contact.append(contacts)
    save_contacts(Contact)
def view_contacts():
    Contact=load_contacts
    print("\nContact list:\n")
    for contacts in Contact:
        print(f"name:{contacts['name']}, Email:{contacts['Email']}, Phone_number:{contacts['Phone_number']},Address:{contacts['Address']},status:{contacts['status']}" )
def Remove_contacts(index):
    pass
def Search_contacts(query):
    pass
def update_contacts(index):
    pass

    
    