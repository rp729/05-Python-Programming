import class_notes as cellphone

'''Main function'''
def main():
    '''Define object'''
    man = input("Enter manufacture:")
    mod = input("Enter the model:")
    retail = input_validation(input("Enter price:"))

    '''Assign values to object in class'''
    phone = cellphone.CellPhone(man,mod,retail)

    '''Display formatted data'''
    print('Manufacture: ',phone.get_manufact())
    print("Model: ",phone.get_model())d
    print(f"Retail price: ${phone.get_retail_price():.2f}")

'''Input validation to verify user enters a number'''
def input_validation(num):
    while str.isnumeric(num) == False:
        num = input("Invalid input. Enter price:")
    return float(num)


main()