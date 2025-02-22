def convert_celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

def calculate_wind_chill(scale, wind_speeds):
    for i in wind_speeds:
        wind_chill = 35.74 + (0.6215 * scale) - (35.75 * (i ** 0.16)) + (0.4275 * scale * (i ** 0.16))
        print(f"At temperature {scale} .OF, and wind speed {i}, the wind chill in mph is: {wind_chill: .2f}F")



wind = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60]
temp = float(input("What is the temperature? "))
scale = str(input("What is the scale, Celsius or Fahrenheit (C/F)? ")).lower()

if scale == "c":
    scale = convert_celsius_to_fahrenheit(temp)
    print(f"The temperature in Fahrenheit is {scale}")
    calculate_wind_chill(scale, wind)
 
elif scale == "f":
    calculate_wind_chill(temp, wind)
