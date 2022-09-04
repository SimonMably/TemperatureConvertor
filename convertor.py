
class Convertor:

    def fahrenheit_to_celsius(self, user_input: float):
        output = (float(user_input) - 32) * 5 / 9
        return str(round(output, 2))

    def fahrenheit_to_kelvin(self, user_input: float):
        output = (float(user_input) - 32) * 5 / 9 + 273.15
        return str(round(output, 2))

    def celsius_to_fahrenheit(self, user_input: float):
        output = (float(user_input) * 9 / 5) + 32
        return str(round(output, 2))

    def celsius_to_kelvin(self, user_input: float):
        output = float(user_input) + 273.15
        return str(round(output, 2))

    def kelvin_to_fahrenheit(self, user_input: float):
        output = (float(user_input) - 273.15) * 9 / 5 + 32
        return str(round(output, 2))

    def kelvin_to_celsius(self, user_input: float):
        output = float(user_input) - 273.15
        return str(round(output, 2))
