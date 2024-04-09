#Author: Kilyn Crenshaw
#Date: 4/8/2024

#Class for Vehicle
class Vehicle:
    def __init__(self,vehicleType):
        self.vehicleType = vehicleType
#Subclass for Automobile
class Automobile(Vehicle):
    def __init__(self,vehicleType,year,make,model,doors,roof):
        super().__init__(vehicleType)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof
#Getting user input
def gettingInput():
    vehicleType = "car"
    year = int(input("Enter the year of the car: "))
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")  
    #Making sure correct input is provided
    while True:
       doors = int(input("Enter the number of doors (2 or 4): "))
       if (doors == 2 or doors == 4):
            break
       else:
            print("Invalid input. Please try again")
    #Making sure correct input is provided
    while True:
       roof = ((input("Enter the type of roof on the vehicle (solid or sunroof): ")).lower())
       if (roof == "solid" or roof == "sunroof"):
            break
       else:
            print("Invalid input. Please try again")
    #Creating new object with user input as attributes
    newVehicle = Automobile(vehicleType,year,make,model,doors,roof)
    #returning object
    return newVehicle
#Printing results
def printingResults(newVehicle):
    #Printing data using object created in last function
    print("Vehicle type: "+newVehicle.vehicleType)
    print("Year: "+str(newVehicle.year))
    print("Make: "+newVehicle.make)
    print("Model: "+newVehicle.model)
    print("Number of doors: "+str(newVehicle.doors))
    print("Type of roof: "+newVehicle.roof)

newVehicle = gettingInput()
printingResults(newVehicle)