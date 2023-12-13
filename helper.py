import json



def exit_func(my_data_file,cars):
    json_string = json.dumps(cars)
    # save the list in a file
    with open(my_data_file, 'w') as file:
        file.write(json_string)
    print("see ya") 
    exit()
    

def delete_car(cars):
    
    search_id = input("Enter licence number: ")
    for car in cars:
        if car.get("licence number") == search_id:
            cars.remove(car)
            print(f"Car with license number {search_id} has been deleted.")
            return
        
    print("Cannot find your car...")