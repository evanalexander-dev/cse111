from datetime import datetime
from math import pi

def tire_volume(w: int, a: int, d: int):
    return round((pi * w ** 2 * a * (w * a + 2540 * d)) / 10_000_000_000, 2)


width = int(input("Enter the width of the tire in mm (ex 205): "))
aspect_ratio = int(input("Enter the aspect ratio of the tire (ex 60): "))
diameter = int(input("Enter the diameter of the wheel in inches (ex 15): "))

volume = tire_volume(width, aspect_ratio, diameter)
print(f"The approximate volume is {volume} liters")

buy_tire = input("Would you like to buy tires with the dimensions you entered? ")
if buy_tire.lower() == "yes":
    quantity = int(input("How many tires would you like to buy? "))
    phone_number = input("Please enter your phone number: ")

with open("volumes.txt", "at") as f:
    print(datetime.now().strftime("%Y-%m-%d"), width, aspect_ratio, diameter, volume, sep=", ", end="", file=f)
    if buy_tire.lower() == "yes":
        print("", quantity, phone_number, sep=", ", end="", file=f)  # Blank string is to add the correct comma to file
    print(file=f)
