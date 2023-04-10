from contact import Contact
from db import dbHandler
db = dbHandler('localhost',"root","Usama222","database")

def add_Contact(contact):
    db.insertContact(contact)

def show_contacts():
    return db.showAllContacts()
def show_contact_name(name):
    return db.showContactbyName(name) 
def insert_user(email,password):
    return db.insertUser(email,password)    
def get_user():
    return db.getUser()    
def validatePasword(password):
    if(len(password) > 8 ):
        return True
    else:
        return False
def delete_contact(id):
    return db.deleteContact(id)
def get_contact(id):
    return db.getContact(id)                    

def update_contact(id,nam,mb,c,p):
    db.updateContact(id,nam,mb,c,p,)    