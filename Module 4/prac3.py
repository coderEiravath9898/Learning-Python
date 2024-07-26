# Love Calculator

name1 = input("Enter First Name").lower()
name2 = input("Enter Second Name").lower()

# Lower Function converts a string to lower case

count_name1=[]
count_name2=[]

for letter in "truelove":
    count_name1.append(name1.count(letter))
    count_name2.append(name2.count(letter))
    
    
sum_name1=0;
sum_name2=0;

for num in count_name1:
    sum_name1+=num
    
for num in count_name2:
    sum_name2+=num
    
    
print("Total love score is "+str(sum_name1)+str(sum_name2))
total_score=int(str(sum_name1)+str(sum_name2))

if total_score>=0 and total_score <40:
    print("You dont go well together")
    
elif total_score >=40 and total_score<=100:
    print("You go well together")
    
else:
    print("Soulmates!")



