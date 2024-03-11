# Working with csv files
import csv

fields = ['Employees code', 'Name', 'Age', 'Salary']
rows = [['A101', 'Ajay', '27', '9000.10'],
        ['A102', 'Sujay', '30', '19100.50'],
        ['A171', 'Amog', '34', '54565756876'],
        ['A191', 'Akshat', '23', '10000000000'],
        ['A192', 'Tanmay', '27', '7800.45'],
        ['A110', 'Aditya', '34', '5000000']]
csvfile = open('EmpData.csv', 'w', newline='')
file = csv.writer(csvfile)
file.writerow(fields)
file.writerows(rows)
csvfile.close()


f = []
r = []

csvfile = open('EmpData.csv', 'r')
csvreader = csv.reader(csvfile)

fields = next(csvreader)
for row in csvreader:
        r.append(row)

# print(fields)
# print(r)

num_of_rows = csvreader.line_num
csvfile.close()


for fid in fields:
        print(f"{fid:20}", end='')

for row in r[:num_of_rows]:
     print()
     for col in row:
         print(f"{col:20}", end='')

print(num_of_rows)

