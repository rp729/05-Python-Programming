'''
This program accept user data and display it in an organized fashion.
'''
name = input("Enter your name:")
location = input("Enter your address (include city, state and zip):")
phone = input("Enter your phone number:")
afsc = input("Enter your AFSC or MOS:")

'''
Display output
'''
print(F"\nThe data you entered is as followed:\
      \nName:{name}\
      \nAddress:{location}\
      \nPhone Number:{phone}\
      \nCareer:{afsc}")