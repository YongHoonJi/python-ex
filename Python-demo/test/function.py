#function without return value
def print_my_info(name, phone, email):
    print('name:'+name)
    print('phone:'+phone)
    print('email:'+email)
    return

#function with return value
def return_my_info(name, phone, email):
    return name+','+phone+','+email

#call functions
print('function 1')
print_my_info('ji','01075504676','jimang80@gmail.com')

print('function 2')
print(return_my_info('ji','01075504676','jimang80@gmail.com'))

      
