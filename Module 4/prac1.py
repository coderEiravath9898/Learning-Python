#Gross Pay With Overtime

working_hours = float(input("Enter Working Hours \n"))
hourly_rate = float(input("Enter Hourly Rate In  ₹ \n"))

if(working_hours<=40):
    print(f"The amount to be paid is {working_hours*hourly_rate}")
else:
    extra_time = working_hours-40;
    print(f"The amount to be paid is ₹ {round((40*hourly_rate)+ (1.5*hourly_rate*extra_time),2)} ")


