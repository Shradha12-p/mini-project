#STUDENT REPORT CARD
import os

class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.grade = self.calculate_grade()

    def calculate_grade(self):
        try:
            avg = sum(self.marks) / len(self.marks)
            if avg >= 90:
                return 'A'
            elif avg >= 75:
                return 'B'
            elif avg >= 60:
                return 'C'
            elif avg >= 40:
                return 'D'
            else:
                return 'F'
        except ZeroDivisionError:
            return 'Invalid'

    def save_to_file(self):
        try:
            with open("students.txt", "a") as f:
                f.write(f"{self.roll},{self.name},{','.join(map(str, self.marks))},{self.grade}\n")
            print("✔️ Student data saved successfully!\n")
        except Exception as e:
            print(f"❌ Error saving data: {e}")

    @staticmethod
    def fetch_student(roll):
        try:
            with open("students.txt", "r") as f:
                for line in f:
                    data = line.strip().split(',')
                    if data[0] == roll:
                        print(f"\n📋 Report for Roll No. {roll}:")
                        print(f"Name: {data[1]}")
                        print(f"Marks: {data[2:-1]}")
                        print(f"Grade: {data[-1]}\n")
                        return
                print("❌ No student found with that roll number.\n")
        except FileNotFoundError:
            print("❌ File not found. No records yet.\n")

def main():
    while True:
        print("🎓 Student Report Card Generator")
        print("1. Add Student")
        print("2. View Report Card")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            try:
                roll = input("Enter Roll Number: ")
                name = input("Enter Name: ")
                marks = list(map(int, input("Enter marks of 3 subjects separated by space: ").split()))
                if len(marks) != 3 or any(m < 0 or m > 100 for m in marks):
                    raise ValueError("Marks must be 3 values between 0 and 100.")
                s = Student(roll, name, marks)
                s.save_to_file()
            except ValueError as ve:
                print(f"❌ Invalid input: {ve}\n")
        elif choice == '2':
            roll = input("Enter Roll Number to fetch: ")
            Student.fetch_student(roll)
        elif choice == '3':
            print("Exiting... 🚪")
            break
        else:
            print("❌ Invalid option. Try again.\n")

if __name__ == "__main__":
    main()
