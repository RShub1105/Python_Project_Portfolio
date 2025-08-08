import Module
Module.say_hello("\033[35mRahul\033[0m")

import Converter
km = 11
mile = Converter.km_to_mile(km)
print(f"\033[31m {km} KM is = {mile} Mile.\033[0m")
mi = 5
km_back = Converter.mile_to_km(mi)
print(f"\033[33m {mi} Mile is = {km_back} KM.\033[0m") 

import math
import random
print( math.sqrt (16))
print( random.randint (1,100))