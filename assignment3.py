# import csv

# def read_data():
#     records = []

#     try:
#         with open("attendance.csv", "r") as file:
#             reader = csv.reader(file)

#             for row in reader:
#                 if len(row) == 3 and row[2].strip().capitalize() in ["Present", "Absent"]:
#                     records.append(row)
#                 else:
#                     print("Invalid record skipped")

#     except FileNotFoundError:
#         print("File not found!")

#     return records

# def calculate(records):
#     employees = {}
#     for row in records:
#         name = row[0].strip()
#         status = row[2].strip().capitalize()

#         if name not in employees:
#             employees[name] = [0, 0]

#         if status == "Present":
#             employees[name][0] += 1
#         else:
#             employees[name][1] += 1

#     return employees


# def report(employees):
#     with open("attendance_report.txt", "w") as file:
#         file.write("EMPLOYEE ATTENDANCE REPORT\n")

#         for name, data in employees.items():
#             present = data[0]
#             absent = data[1]
#             total = present + absent

#             percentage = present / total * 100

#             print("\nEmployee:", name)
#             print("Present:", present)
#             print("Absent:", absent)
#             print("Attendance:", round(percentage, 2), "%")

#             file.write("\nEmployee: " + name + "\n")
#             file.write("Present: " + str(present) + "\n")
#             file.write("Absent: " + str(absent) + "\n")
#             file.write("Attendance: " + str(round(percentage, 2)) + "%\n")

#             if percentage < 75:
#                 print("Warning: Attendance below 75%")
#                 file.write("Warning: Attendance below 75%\n")


# def add_data():
#     name = input("Enter employee name: ")
#     date = input("Enter date: ")
#     status = input("Enter status (Present/Absent): ").capitalize()

#     if not name.strip() or not date.strip():
#         print("Name and date cannot be empty!")
#         return

#     if status not in ["Present", "Absent"]:
#         print("Invalid status!")
#         return

#     with open("attendance.csv", "a", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow([name, date, status])

#     print("Record added successfully!")


# def main():
#     choice = input("Do you want to add attendance? (yes/no): ")

#     if choice.lower() == "yes":
#         add_data()

#     records = read_data()
#     employees = calculate(records)
#     report(employees)

#     print("\nReport saved in attendance_report.txt")


# main()


