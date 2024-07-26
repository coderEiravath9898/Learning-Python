#Create Call Sign - Greet The User, Prompt Them To Enter Their Name, Favourite Color, Favourite Animal, Date(DD) of Birth And Month(MM) Of Birth', Finally Display THeir Call Sign

print("Hello! Lets Get Your Callsign")
user_name=input("Enter Your Name \n")
fav_color = input("Enter Your Favourite Color \n")
fav_animal = input("Favourite Animal \n")
day_birth = input("Your Day of Birth (1-31)")
month_birth = input("Your Month of Birth (1-12)")

callsign = f"{fav_color}-{fav_animal}-{9}-{8}"
print(f"Hello {user_name} your call sign is {callsign}")