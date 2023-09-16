#Exercise 1 

file_path = input("Enter the path to the CSV file: ") 
records = [] 
with open(file_path, 'r') as file: #opens the user imput
    csv_reader = csv.DictReader(file)
    '''this function uses dictreader to create an object that operates like a regular reader but maps the information in each row to a dictionary'''
    for row in csv_reader:
        records.append(row)
    '''this for loop adds the data from the csv file to an empty list - to be used later in calculations'''


total = sum(float(record['Grade']) for record in records)
average = total / len(records)
print(f"Average Grade: {average}")
print("--------------------")
'''these operations sum the (transformed float) data from the records list in the grade column, and divide by the length of the list to then print the average grade'''


filtered_records = [record for record in records if float(record['Grade']) >= 80.0]
'''this function uses the entire row in the records list to filter students who got a grade above 80'''
'''by using the entire row from the original csv file, we get all column informations like student name and grade'''


print("Student Report")
print("--------------")
for record in filtered_records:
    print(f"Name: {record['Name']}")
    print(f"Grade: {record['Grade']}")
    print("--------------------")
'''these print functions loop over for every entry with a grdae higher than 80, and print the respective student name and their grade'''