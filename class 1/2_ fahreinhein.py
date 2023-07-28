# function converts from temperature in Celsius to Fahrenheit
def convert_from_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# ask the user for current Celsius temperature
prompted_celsius = float(input("Enter the Celsius temperature: "))
fahrenheit_output = convert_from_celsius_to_fahrenheit(prompted_celsius)
print("The temperature in Fahrenheit is: ", fahrenheit_output)
