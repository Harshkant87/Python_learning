def weather_condition(temperature):
    if temperature > 20:
        return "Hot Weather! Stay inside your home"
    else:
        return "Cold Weather! Stay inside your home."

user_input = float(input("Enter Temperature: "))
print(weather_condition(user_input))