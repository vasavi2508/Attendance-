
# Attendance Recovery Computation System

# Function to calculate current attendance
def calculate_attendance(attended, total):

    if total == 0:
        return 0

    percentage = (attended / total) * 100

    return percentage


# Function to calculate future attendance
def calculate_future_attendance(attended, total,
                                future_attended,
                                future_total):

    new_attended = attended + future_attended
    new_total = total + future_total

    percentage = (new_attended / new_total) * 100

    return percentage


# Function to find minimum future classes
def find_minimum_classes(attended, total, threshold,
                         future_rate):

    if attended / total * 100 >= threshold:
        return 0

    if future_rate <= threshold:
        return -1

    for classes in range(1, 100001):

        # Round down future attended classes
        future_attended = int(classes * future_rate / 100)

        percentage = calculate_future_attendance(
            attended,
            total,
            future_attended,
            classes
        )

        if percentage >= threshold:
            return classes

    return -1


# Main program
print("==========================================")
print("       ATTENDANCE RECOVERY SYSTEM")
print("==========================================")

# Get student details
name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

# Get attendance details
total = int(input("Enter total classes conducted: "))
attended = int(input("Enter classes attended: "))

# Validate attendance details
if total <= 0 or attended < 0 or attended > total:

    print("Invalid attendance details!")

else:

    threshold = float(
        input("Enter required attendance percentage: ")
    )

    if threshold <= 0 or threshold > 100:

        print("Invalid eligibility threshold!")

    else:

        # Calculate current attendance
        current = calculate_attendance(attended, total)

        print("\n==========================================")
        print("          STUDENT ATTENDANCE")
        print("==========================================")

        print("Student Name       :", name)
        print("Roll Number        :", roll_number)
        print("Classes Conducted  :", total)
        print("Classes Attended   :", attended)
        print("Current Attendance :", round(current, 2), "%")
        print("Required Attendance:", threshold, "%")

        # Check current eligibility
        if current >= threshold:
            print("\nStatus: Eligible for attendance requirement.")
            print("No additional classes are required.")

        else:
            print("\nStatus: Attendance below required threshold.")

            print("\n==========================================")
            print("       ATTENDANCE RECOVERY ANALYSIS")
            print("==========================================")

            # Different future attendance scenarios
            scenarios = [100, 90, 80, 70]

            for rate in scenarios:

                print("\nFuture Attendance Scenario:", rate, "%")

                minimum = find_minimum_classes(
                    attended,
                    total,
                    threshold,
                    rate
                )

                if minimum == 0:
                    print("Already eligible.")

                elif minimum == -1:
                    print("Recovery is not possible under this scenario.")

                else:

                    future_attended = int(minimum * rate / 100)

                    final_percentage = calculate_future_attendance(
                        attended,
                        total,
                        future_attended,
                        minimum
                    )

                    print("Minimum Future Classes:", minimum)
                    print("Future Classes Attended:", future_attended)
                    print(
                        "Projected Attendance:",
                        round(final_percentage, 2), "%"
                    )

        print("\n==========================================")
        print("Attendance analysis completed.")
        print("==========================================")
