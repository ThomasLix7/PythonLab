def final_grade_calculator():
    print("\nEnter q to finish input!\n")
    n = 1
    total_grade = 0
    while True:
        grade = input(f"Enter grade of assignment {n}: ")
        if grade.lower() == "q":
            break
        try:
            grade = int(grade)
            if grade < 0 or grade > 100:
                raise ValueError("Grade must be a number between 0 and 100!")
            total_grade += grade
            n += 1
        except ValueError:
            print("Grade must be a number between 0 and 100!")
    print(f"\nYour final average grade is {total_grade/(n-1)}")


final_grade_calculator()