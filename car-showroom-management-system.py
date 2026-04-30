# Project Title: Car Showroom Management System

# # Contributors: Syed Mustafa Haider Rizvi, Axis Verma
# Last Updated On: <2025-11-09>

import pickle 

# User Defined Functions/Methods
def add_car():
    car = {
        'id': input("Enter Car ID: "),
        'brand': input("Enter Brand: "),
        'model': input("Enter Model: "),
        'price': float(input("Enter Price: ")),
        'fuel': input("Enter Fuel Type: "),
        'available': input("Available (Yes/No): ")
    }
    with open("Car.dat", "ab") as f:
        pickle.dump(car, f)
    print("Car added successfully.\n")

def display_cars():
    try:
        with open("Car.dat", "rb") as f:
            while True:
                car = pickle.load(f)
                print(car)
    except FileNotFoundError:
        print("Car file not found.\n")
    except EOFError:
        pass

def search_car(car_id):
    found = False
    try:
        with open("Car.dat", "rb") as f:
            while True:
                car = pickle.load(f)
                if car['id'] == car_id:
                    print("Car Found:", car)
                    found = True
                    break
    except FileNotFoundError:
        print("Car file not found.\n")
    except EOFError:
        if not found:
            print("Car not found.\n")

def update_car(car_id):
    cars = []
    found = False
    try:
        with open("Car.dat", "rb") as f:
            while True:
                car = pickle.load(f)
                if car['id'] == car_id:
                    car['price'] = float(input("Enter new price: "))
                    car['available'] = input("Available (Yes/No): ")
                    found = True
                cars.append(car)
    except FileNotFoundError:
        print("Car file not found.\n")
        return
    except EOFError:
        pass

    with open("Car.dat", "wb") as f:
        for car in cars:
            pickle.dump(car, f)

    if found:
        print("Car updated.\n")
    else:
        print("Car not found.\n")

def delete_car(car_id):
    cars = []
    deleted = False
    try:
        with open("Car.dat", "rb") as f:
            while True:
                car = pickle.load(f)
                if car['id'] != car_id:
                    cars.append(car)
                else:
                    deleted = True
    except FileNotFoundError:
        print("Car file not found.\n")
        return
    except EOFError:
        pass

    with open("Car.dat", "wb") as f:
        for car in cars:
            pickle.dump(car, f)

    if deleted:
        print("Car deleted.\n")
    else:
        print("Car not found.\n")


def add_employee():
    emp = {
        'id': input("Enter Employee ID: "),
        'name': input("Enter Name: "),
        'designation': input("Enter Designation: "),
        'salary': float(input("Enter Salary: ")),
        'contact': input("Enter Contact: ")
    }
    with open("Employee.dat", "ab") as f:
        pickle.dump(emp, f)
    print("Employee added successfully.\n")

def display_employees():
    try:
        with open("Employee.dat", "rb") as f:
            print("\n--- Employee List ---")
            while True:
                emp = pickle.load(f)
                print(emp)
    except FileNotFoundError:
        print("Employee file not found.\n")
    except EOFError:
        pass

def search_employee(emp_id):
    found = False
    try:
        with open("Employee.dat", "rb") as f:
            while True:
                emp = pickle.load(f)
                if emp['id'] == emp_id:
                    print("Employee Found:", emp)
                    found = True
                    break
    except FileNotFoundError:
        print("Employee file not found.\n")
    except EOFError:
        if not found:
            print("Employee not found.\n")

def update_employee(emp_id):
    emps = []
    found = False
    try:
        with open("Employee.dat", "rb") as f:
            while True:
                emp = pickle.load(f)
                if emp['id'] == emp_id:
                    emp['salary'] = float(input("Enter new salary: "))
                    emp['contact'] = input("Enter new contact: ")
                    found = True
                emps.append(emp)
    except FileNotFoundError:
        print("Employee file not found.\n")
        return
    except EOFError:
        pass

    with open("Employee.dat", "wb") as f:
        for emp in emps:
            pickle.dump(emp, f)

    if found:
        print("Employee updated.\n")
    else:
        print("Employee not found.\n")

def delete_employee(emp_id):
    emps = []
    deleted = False
    try:
        with open("Employee.dat", "rb") as f:
            while True:
                emp = pickle.load(f)
                if emp['id'] != emp_id:
                    emps.append(emp)
                else:
                    deleted = True
    except FileNotFoundError:
        print("Employee file not found.\n")
        return
    except EOFError:
        pass

    with open("Employee.dat", "wb") as f:
        for emp in emps:
            pickle.dump(emp, f)

    if deleted:
        print("Employee deleted.\n")
    else:
        print("Employee not found.\n")

def summary_reports():
    brand_count = {}
    high_salary = []

    try:
        with open("Car.dat", "rb") as f:
            while True:
                car = pickle.load(f)
                brand = car['brand']
                if brand not in brand_count:
                    brand_count[brand] = []
                brand_count[brand].append(car)
    except FileNotFoundError:
        print("Car file not found.\n")
    except EOFError:
        pass

    try:
        with open("Employee.dat", "rb") as f:
            while True:
                emp = pickle.load(f)
                if emp['salary'] > 50000:
                    high_salary.append(emp['name'])
    except FileNotFoundError:
        print("Employee file not found.\n")
    except EOFError:
        pass

    print("\nBrand Count:")
    for brand in brand_count:
        if len(brand_count[brand]) == 0:
            print(brand, ": No cars")
        else:
            count = len(brand_count[brand])
            print(brand, ":", count)

    print("\nHigh Salary Employees (> ₹50,000):")
    if len(high_salary) == 0:
        print("None")
    else:
        for name in high_salary:
            print(name)
# Main Code
while True:
     print("\n===== Car Showroom Management =====")
     print("1. Add Car")
     print("2. Display Cars")
     print("3. Search Car")
     print("4. Update Car")
     print("5. Delete Car")
     print("6. Add Employee")
     print("7. Display Employees")
     print("8. Search Employee")
     print("9. Update Employee")
     print("10. Delete Employee")
     print("11. Summary Reports")
     print("12. Exit")
     choice = input("Enter your choice: ")

     if choice == '1':
          add_car()
     elif choice == '2':
          display_cars()
     elif choice == '3':
          cid = input("Enter Car ID to search: ")
          search_car(cid)
     elif choice == '4':
          cid = input("Enter Car ID to update: ")
          update_car(cid)
     elif choice == '5':
          cid = input("Enter Car ID to delete: ")
          delete_car(cid)
     elif choice == '6':
          add_employee()
     elif choice == '7':
          display_employees()
     elif choice == '8':
          eid = input("Enter Employee ID to search: ")
          search_employee(eid)
     elif choice == '9':
          eid = input("Enter Employee ID to update: ")
          update_employee(eid)
     elif choice == '10':
          eid = input("Enter Employee ID to delete: ")
          delete_employee(eid)
     elif choice == '11':
          summary_reports()
     elif choice == '12':
          print("Exiting program.")
          break
     else:
          print("Invalid choice. Try again.\n")