student_name=input('enter the name of the student: ')
student_rollno=input('enter the roll number of the student: ')
subjects_names=input('enter the subjects: ').split(',')
unique_subjects=list(set(subjects_names))
subject_marks={}
for subject in unique_subjects:
    marks=int(input(f'enter the marks of {subject}: '))
    subject_marks[subject]=marks


print("\n     Display of Student Details     ")
print(f'Student Name: {student_name}')
print(f'Student Roll Number: {student_rollno}')
print("unique subjects:")
print(unique_subjects)
print("Subject Marks:")
for subject, marks in subject_marks.items():
    print(f'{subject}: {marks}')


