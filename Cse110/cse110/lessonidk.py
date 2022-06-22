divide = int(0)
num = int(0)
great = int(0)
stop = -1
while stop == -1:
    nus =  int(input("number:"))
    if nus == 0:
        stop = 1
    else:
        num += int(nus)
        divide +=1 
        if nus < num:
            great = nus

print(f"{num/divide}")
print(f" sum : {num}")
print(f" memebers : {divide}")
print(f"greatest number = {great}")