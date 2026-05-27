# Write A Python Program To Get Temperature In Centigrade, To Convert Into Fahrenheit And Kelvin


def cen_fah(cen):
    return 9/5*cen+32
def cen_kel(cen):
    return cen+273.15

def fah_cen(fah):
    return 5/9*(fah-32)

def fah_kel(fah):
    return 5/9*(fah-32)+273.15

cen=int(input("enter the temperature in celcius:"))
print(f"The tempure of {cen} celcius is {cen_fah(cen)} in fahrenhiet and {cen_kel(cen)} in kelvin.")


print(9/5*25+32)