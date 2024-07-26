# BMI Calculator  - Weight(in kg) / height*height(in meter)

height = float(input("Enter your height \n"))
weight = float(input("Enter your weight \n"))

BMI = (weight)/(height**2)


if BMI < 18.5 :
   print("Underweight")  
elif BMI > 18.5 and BMI < 25 :
   print("Normal")  
elif BMI > 25 and BMI < 30 :
   print("Overweight")
elif BMI > 30 and BMI < 35:
   print("Obese")     
else:
   print("How are you not dead yet?")

