import csv
student_header = ['email', 'cohort']
student_data = [
    ['audit@example.com', 'C1'],
    ['enfa4@unicauca.edu.co', 'C2'],
    ['honor@example.com', 'C2'],
    ['staff@example.com', 'C3'],
    ['verified@example.com', 'C3']
]
with open('cohorts.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(student_header)
    # Use writerows() not writerow()
    writer.writerows(student_data)