from icecream import ic
import os
import json
from enum import Enum
from helper import exit_func, delete_car



class Actions(Enum):
    PRINT = 1
    ADD = 2
    SEARCH = 3
    DELETE = 4
    EXIT = 5

cars =[]
my_data_file='cars.json'

def menu():
    for x in Actions:
       ic(f'{x.value} - {x.name}')
   
    return Actions(int(input("Enter your selection:")))

def load_data(my_data_file):# load a list from a file
    global cars
    try:
        with open(my_data_file, 'r') as file:
            json_string = file.read()
            cars = json.loads(json_string)
    except: pass
    




def main():
    os.system('cls' if os.name == 'nt' else 'clear')# clear screen
    load_data(my_data_file) #load data from a file
    

     

    while(True):
        userSelection=menu() #display a menu and get user selection and  implements menu
        if userSelection == Actions.EXIT: exit_func(my_data_file,cars)
        if userSelection ==  Actions.PRINT: ic(cars)
        if userSelection ==  Actions.SEARCH: search_car()
        if userSelection ==  Actions.ADD: add_contact()
        if userSelection ==  Actions.DELETE: delete_car(cars)
        
        


def add_contact():
    cars.append({"color":input("Enter your color:"),"model":input("Enter your model:"), "Brand":input("Enter your Brand:"),"licence number":input("Enter your licence number:")})

def search_car():
    global cars
    
    search_id = input("Enter your licence number:")
    for car in cars:

        if car.get("licence number")== search_id:
            ic(car)
            return 
    ic("Cannot find your car :)")
    return

if __name__ == "__main__":
    main()