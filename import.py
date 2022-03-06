def importer(first_name, last_name, phone, address):
    path ="file_name.json" 
    data = open (path, 'a')
    data.write (first_name, last_name, phone, address)
    data.close ()
    

