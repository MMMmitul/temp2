import json 

def save_contacts(Contact):
    with open('Contact.json','w')as file:
        json.dump(Contact,file,indent=4)
        
def load_contacts():
    with open('Contact.json','r')as file:
        return json.load(file)