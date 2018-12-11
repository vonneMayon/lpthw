name = 'Desiree Y. Mayon'
age = 31 # not a lie
height = round(52 * 2.54) # cm
weight = round(180 * .45) # lbs
eyes = 'Hazel'
teeth = 'White'
hair = 'Black'

# 1 lb = .45 kg
# 1 in. = 2.54 cm
print(f"Let's talk about {name}.")
print(f"She's {height} centimeters tall.")
print(f"She's {weight} Kg heavy.")
print("Actually that's not too heavy.")
print(f"She's got {eyes} eyes and {hair} hair.")
print(f"Her teeth are usually {teeth} depending on the coffee.")

#this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")
