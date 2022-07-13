
import csv

file = open('salve\life-expectancy.csv')

type(file)
csvreader = csv.reader(file)
header = []
header = next(csvreader)
header
rows = []
for row in csvreader:
        rows.append(row)
sortbyexpectancy = lambda x:x[3]
max(rows,key = sortbyexpectancy)



year = input('select year')

databyyear = []
for d in rows:
    if d[2] == year:
        databyyear.append(d)
databyyear.sort(key = sortbyexpectancy)
b = min(databyyear,key = sortbyexpectancy)


databyyearq = []
for dq in rows:
        databyyearq.append(dq)
databyyearq.sort(key = sortbyexpectancy)
bq = min(databyyearq,key = sortbyexpectancy)

print('Max life expectancy:',databyyearq[-1][3],',',databyyearq[-1][0],',',databyyearq[-1][2])
print('Min life expectancy:',bq[3],',',bq[0],',',bq[2])
print('///////////////////////////////////////////////////////////////////////////////////////////////')



print(f'in the year of {year}')
print('Max life expectancy:',databyyear[-1][3],',',databyyear[-1][0])
print('Min life expectancy:',b[3],',',b[0])
number = float(0)
div = float(0)
for d in rows:
    if d[2] == year:
        number += float(d[3])
        div += 1
ave = number/div
print(f' the average in this year is : {ave}')


file.close()