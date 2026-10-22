# The script is a temperature converter
fahrenheit = input ("Hi there, please enter a temperature in Fahrenheit. ")
fahrenheit = float(fahrenheit)
celsius = (fahrenheit - 32) * 5 / 9
print (f"{fahrenheit:.1f}°F is {celsius:.1f}°C. ")