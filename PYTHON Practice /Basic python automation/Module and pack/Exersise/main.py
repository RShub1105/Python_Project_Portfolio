import greet
greet.say_greet("\033[32m Rahul \033[0m")

import Convert
celcius = int(input("Enter the celcius to convert Fahranite = "))
farha = Convert.celcius_to_faheranite(celcius)
print(f"{celcius}℃ is = {farha}℉.")
fr=int(input("Enter the Fahranite to celcius = "))
celcius_back = Convert.faheranite_to_celcius(fr)
print(f"{fr}℉ is = {celcius_back}℃.")

import math
import random
print(math.sqrt(11))
print(random.randint(1,50))
