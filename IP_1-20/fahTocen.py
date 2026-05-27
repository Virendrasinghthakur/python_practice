# Write A Python Program To Get Temperature In Fahrenheit, To Convert Into Centigrade And Kelvin


def fah_cen(fah):
    return 5/9*(fah-32)

def fah_kel(fah):
    return 5/9*(fah-32)+273.15

fah=float(input("enter the temperature in fahrenhiet:"))
print(f"The tempure of {fah} celcius is {fah_cen(fah)} in celsius and {fah_kel(fah)} in kelvin.")
