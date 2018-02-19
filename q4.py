# Conveting temperature

class Temperature:
    def convertFahrenheit(celcius):
        print("Celcius = {}\nFahrenhiet = {}".format(celcius, 1.8 * celcius + 32))


    def convertCelcius(fahn):
        print("Fahrenheit = {}\nCelcius = {}".format(fahn, (fahn-32)/1.8))


temp0 = Temperature

temp0.convertFahrenheit(18)
temp0.convertCelcius(89)