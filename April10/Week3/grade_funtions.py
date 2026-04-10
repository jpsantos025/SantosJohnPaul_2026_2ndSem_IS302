def calculate_average(subject_one, subject_two, subject_three):
    return (subject_one + subject_two + subject_three) / 3

def get_remark(avg_score):
    if 90 <= avg_score <= 100:
        return "Excellent"
    elif 85 <= avg_score <= 89:
        return "Very Good"
    elif 80 <= avg_score <= 84:
        return "Good"
    elif 75 <= avg_score <= 79:
        return "Fair"
    else:
        return "Failed"

# Input grades
math_grade = float(input("Enter grade for Math: "))
science_grade = float(input("Enter grade for Science: "))
english_grade = float(input("Enter grade for English: "))

# Compute average
final_average = calculate_average(math_grade, science_grade, english_grade)

# Get remark
final_remark = get_remark(final_average)

# Output
print("\n----- STUDENT GRADE RESULT -----")
print("Average:", round(final_average, 2))
print("Remark:", final_remark)