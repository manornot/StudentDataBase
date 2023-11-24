
import subprocess
import os

def test_add_student():
    # Call C program to add a student
    subprocess.run(["./studentDB.o", "add", "John", "Doe", ...], check=True)

    # Verify the student is added in the output file
    with open('students.txt', 'r') as file:
        students_data = file.read()
        assert "John Doe" in students_data



def test_remove_student():
    student_id = "123"
    # Call C program to remove a student
    subprocess.run(["./studentDB.o", "remove", student_id], check=True)

    # Verify the student is removed from the output file
    with open('students.txt', 'r') as file:
        students_data = file.read()
        assert student_id not in students_data


def test_edit_student():
    student_id = "123"
    new_name = "Jane"
    # Call C program to edit a student
    subprocess.run(["./studentDB.o", "edit", student_id, "--name", new_name], check=True)

    # Verify the student's details are updated in the output file
    with open('students.txt', 'r') as file:
        students_data = file.read()
        assert new_name in students_data

test_add_student()
test_remove_student()
test_edit_student()
