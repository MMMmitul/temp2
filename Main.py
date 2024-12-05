from Task_manager import add_contacts,view_contacts

while True:
    print("contact book management system")
    print("1.Add contacs")
    print("2.view contacts")
    print("3.Remove contacts")
    print("4.Search contacts")
    print("5.Update contacts")
    print("6.Exit")
    
    choice=input("please insert the number: ")
    if choice=="1":
        name=input("enter your name: ")
        Email=input("enter your email: ")
        Phone_number=input("enter your mobile number: ")
        Address=input("enter your Address: ")
        add_contacts(name,Email,Phone_number, Address)
        print("You have successfully added your task")
    elif choice=="2":
        view_contacts()
           
    #         
            
    #         print(f"This{contact}has been updated") 
            
    # elif menu=="2":
    #     contact=input("please give detail contact to view contact")
    #     if contact in contacts:
    #         contact_details=contacts[contact]
        
                
            
        
    