import csv
# from website.models import Student


def read_csv_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Assuming the CSV file has 3 columns: name, age, and email
            sr_no, course, branch, name, contact_no = row
            print(name)
            # Create a new instance of MyModel with the data from the CSV file
            # my_model = Student(name=name, age=age,)
            # Save the new instance to the database
            # my_model.save()


read_csv_file(r'C:\Users\DEV\Downloads\student.csv')
