import class_notes as cellphone

def main():
    phones = make_list()
    print("Here is the data you entered: ")
    display_list(phones)

def make_list():
    phone_list = []
    print('Enter data for five phones.')
    for count in range(1,6):
        print('Phone number '+str(count)+':')
        man = input('Enter the manufacture:')
        mod = input('Enter the model:')
        retail = input_validation(input("Enter price:"))
        print()

        phone = cellphone.CellPhone(man,mod,retail)
        phone_list.append(phone)
    return phone_list

def display_list(phones):
    for phone in phones:
        print(phone.get_manufact())
        print(phone.get_model())
        print(phone.get_retail_price())
        print()

def input_validation(num):
    while str.isnumeric(num) == False:
        num = input("Invalid input. Enter price:")
    return float(num)

main()