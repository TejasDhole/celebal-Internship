if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

# Get the marks for the query_name student
marks = student_marks[query_name]

# Calculate the average marks
average_marks = sum(marks) / len(marks)

# Print the average with 2 decimal places
print("{:.2f}".format(average_marks))
