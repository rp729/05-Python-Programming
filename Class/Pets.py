import Pet_Class

'''Main function'''
def main():
    pet_name = input("Enter the name of your pet:")
    pet_type = input("Enter your pet's animal type:")
    pet_age = input_validation(input("Enter your pet's age in human years:"))

    '''Call on the class to define objects'''
    pet = Pet_Class.Pet(pet_name,pet_type,pet_age)

    '''Display attributes'''
    print(f'{pet.get_name()} is a {pet.get_type()} and is {pet_age} years old.')

'''Simple input validation'''
def input_validation(num):
    while str.isnumeric(num) == False:
        num = input("INVALID INPUT: Enter your pet's age in human years:")
    return num

main()