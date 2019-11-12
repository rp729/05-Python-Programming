import Car_Class

'''Main function'''
def main():
    year = input("Enter the year of your car:")
    make = input("Enter the make of your car:")

    '''Format data to display'''
    car_speed = Car_Class.Car(year,make)
    print(f'Your {year} {make} is going {car_speed.get_speed()} mph')
    print(f'Your {year} {make} is going {car_speed.accelerate()} mph after acceleration.')
    print(f'Your {year} {make} is going {car_speed.decelerate()} mph after breaking.')

    for count in range(5):
        print(car_speed.accelerate())


main()