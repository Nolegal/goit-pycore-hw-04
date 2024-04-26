def show_phone(args,contacts): 
    #name, = args
    name=args[0]
    res = contacts.get(name)
    return res