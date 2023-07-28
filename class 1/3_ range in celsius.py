# function converts from temperature in Celsius to Fahrenheit
def convert_from_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


# iterate over the range form 0 to 100 in increments of 5
for celsius in range(0, 101, 5):
    fahreinheit_output = convert_from_celsius_to_fahrenheit(celsius)
    print(f"{celsius} degrees Celsius = {fahreinheit_output} degrees Fahrenheit")

print("The temperature in Fahrenheit is: ", fahreinheit_output)
