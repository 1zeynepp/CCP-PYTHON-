import math

# Part A: Function to calculate the average of a list
def Average(num_list):
    total = 0
    for num in num_list:
        total += num
    return total / len(num_list)

# Function to calculate the standard deviation of a list
def StdDev(num_list):
    avg = Average(num_list)
    sum_sq_diff = 0
    for num in num_list:
        sum_sq_diff += (num - avg) ** 2
    return math.sqrt(sum_sq_diff / (len(num_list) - 1))

# Part B: Read Grades.txt and output average and standard deviation
grades = []
with open("Grades.txt", "r") as infile:
    for line in infile:
        if line.strip():
            grades.append(float(line.strip()))

avg_score = Average(grades)
std_score = StdDev(grades)

print(f"The average of the scores is: {avg_score:.1f}")
print(f"The standard deviation is: {std_score:.1f}")
