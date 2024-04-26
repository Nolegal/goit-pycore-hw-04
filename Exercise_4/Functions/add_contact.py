def add_contact(args, contacts):
    name, phone = args
    contacts.update({name : phone})
   
    return "Contact added."