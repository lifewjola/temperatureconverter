# Temperature converter

celc = 0
far = 0
kel = 0
print("WELCOME TO THE ULTIMATE TEMPERATURE CONVERTER")
print("Press C for Celsius \nPress F for fahrenheit \nPress K for Kelvin \n")
conv_from = input("Convert temperature from: ")
if conv_from == 'C' or conv_from == 'c':
    print("Only enter the figures")
    celc = float(input("Enter a temperature in Degree Celsius (°C): "))
if conv_from == 'F' or conv_from == 'f':
    print("Only enter the figures")
    celc = float(input("Enter a temperature in Fahrenheit (°F): "))
if conv_from == 'K' or conv_from == 'k':
    print("Only enter the figures")
    celc = float(input("Enter a temperature in Kelvin (K): "))
print("Let's Convert it!")
conv_to = input("REMEMBER: \nPress C for Celsius \nPress F for fahrenheit \nPress K for Kelvin \nConvert temperature to: \n")

if conv_from == 'C' or conv_from == 'c':
    if conv_to == 'F' or conv_to == 'f':
        far = (celc * 9/5) + 32
        print(celc, "°C is ", far, "°F")
    elif conv_to == 'K' or conv_to == 'k':
        kel = celc + 273.15
        print(celc, "°C is ", kel, "°K")
    else:
        print("Invalid input.")
elif conv_from == 'F' or conv_from == 'f':
    if conv_to == 'C' or conv_to == 'c':
        celc = (far - 32) * 5/9
        print(far, "°F is ", celc, "°C")
    elif conv_to == 'K' or conv_to == 'k':
        kel = (far - 32) * 5/9 + 273.15
        print(far, "°F is ", kel, "°K")
    else:
        print("Invalid input.")
elif conv_from == 'K' or conv_from == 'k':
    if conv_to == 'C' or conv_to == 'c':
        celc = kel - 273.15
        print(kel, "K is ", celc, "°C")
    elif conv_to == 'F' or conv_to == 'f':
        far = (kel - 273.15) * 9/5 + 32
        print(kel, "K is ", far, "°F")
    else:
        print("Invalid input.")
else:
    print("Invalid input.")
    print("Press 'F' for Fahrenheit")
    print("Press 'K' for Kelvin")
    print("Press 'C' for Celsius")
