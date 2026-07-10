# Write a python program using function to convert Celsius to Fahrenheit.

def temp_conversion(celsius):
    fahrenheit=((9/5)*celsius)+32
    return fahrenheit

celsius=float(input('Enter temperature in celsius: '))
result=temp_conversion(celsius)
print(f"{celsius}°C = {result:.2f}°F")