totalDays = int(input("how many day's temperature ? "))
totalTemp = 0
day_List = []
for i in range(0,totalDays):
    temp = int(input(f"Day {i+1} 's high temprate"))
    totalTemp += temp
    day_List.append(temp)

n = 0
avg = round((totalTemp / totalDays),2)

result =  [i for i in day_List if i >= avg]
print(f"Average : {avg}")
print(f"{len(result)} days(s) above average")
