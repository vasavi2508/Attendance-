# Attendance-
# Attendance Recovery Computation System

## 1. Project Overview

The **Attendance Recovery Computation System** is a Python-based application designed to calculate students' attendance percentages and determine the minimum number of future classes required to achieve the required attendance eligibility.

The system evaluates different future attendance scenarios, such as 100%, 90%, 80%, and 70%, and calculates whether a student can reach the required attendance percentage.

It helps students understand their current attendance status and plan their future class attendance.

## 2. Objectives

- To calculate the current attendance percentage.
- To identify students who are below the required attendance threshold.
- To calculate the minimum future classes required to reach eligibility.
- To evaluate different future attendance scenarios.
- To identify whether attendance recovery is possible.
- To display the projected attendance percentage.
- To help students plan their attendance effectively.

## 3. Assumptions

1. Students enter the total number of classes conducted.
2. Students enter the number of classes attended.
3. The default attendance eligibility threshold is 75%.
4. Future attendance scenarios are 100%, 90%, 80%, and 70%.
5. Fractional future attended classes are rounded down.
6. Attendance recovery is calculated using the entered eligibility threshold.
7. If the future attendance rate is equal to or below the required threshold, recovery is considered impossible when the student is currently below the threshold.
8. The program searches up to 100,000 future classes.

## 4. Formulas Used

### Current Attendance Percentage

Current Attendance = (Classes Attended / Total Classes Conducted) × 100

### Future Attendance Percentage

Future Attendance = ((Current Classes Attended + Future Classes Attended) / (Current Total Classes + Future Total Classes)) × 100

### Minimum Future Classes

The program checks future class counts one by one until the projected attendance percentage reaches the required eligibility threshold.

## 5. Algorithm

1. Start the program.
2. Enter the student's name and roll number.
3. Enter the total classes conducted.
4. Enter the number of classes attended.
5. Validate the attendance details.
6. Enter the required attendance percentage.
7. Calculate the current attendance percentage.
8. Check whether the student is already eligible.
9. If eligible, display the eligibility status.
10. Otherwise, evaluate different future attendance scenarios.
11. Calculate the minimum future classes required for each scenario.
12. Calculate the projected attendance percentage.
13. Display whether recovery is possible.
14. Display the attendance recovery analysis.
15. Stop the program.

## 6. Pseudocode

```text
START

INPUT student name
INPUT roll number

INPUT total classes
INPUT attended classes

IF total classes <= 0 OR
   attended classes < 0 OR
   attended classes > total classes:

    DISPLAY invalid attendance details

ELSE:

    INPUT required attendance percentage

    IF threshold <= 0 OR threshold > 100:

        DISPLAY invalid threshold

    ELSE:

        current attendance =
        (attended classes / total classes) * 100

        DISPLAY current attendance

        IF current attendance >= threshold:

            DISPLAY already eligible

        ELSE:

            SET scenarios = [100, 90, 80, 70]

            FOR each future attendance rate:

                IF future rate <= threshold:

                    DISPLAY recovery not possible

                ELSE:

                    FOR future classes from 1 to 100000:

                        future attended =
                        floor(future classes * future rate / 100)

                        projected attendance =
                        (attended + future attended) /
                        (total classes + future classes) * 100

                        IF projected attendance >= threshold:

                            DISPLAY minimum future classes
                            DISPLAY projected attendance

                            STOP searching this scenario

DISPLAY attendance analysis completed

STOP
```

## 7. Test Cases

| Test Case | Total Classes | Attended | Threshold | Expected Current Attendance |
|---|---:|---:|---:|---:|
| 1 | 100 | 60 | 75% | 60% |
| 2 | 100 | 75 | 75% | 75% |
| 3 | 80 | 72 | 75% | 90% |
| 4 | 120 | 60 | 75% | 50% |
| 5 | 50 | 30 | 80% | 60% |

### Expected Results for Test Case 1

- Current attendance: 60%
- Required attendance: 75%
- At 100% future attendance: 60 classes required.
- At 90% future attendance: 100 classes required.
- At 80% future attendance: 300 classes required.
- At 70% future attendance: Recovery not possible.

## 8. Sample Output

```text
==========================================
       ATTENDANCE RECOVERY SYSTEM
==========================================

Student Name       : Rahul
Roll Number        : 101
Classes Conducted  : 100
Classes Attended   : 60
Current Attendance : 60.0 %
Required Attendance: 75.0 %

Status: Attendance below required threshold.

==========================================
       ATTENDANCE RECOVERY ANALYSIS
==========================================

Future Attendance Scenario: 100 %
Minimum Future Classes: 60
Future Classes Attended: 60
Projected Attendance: 75.0 %

Future Attendance Scenario: 90 %
Minimum Future Classes: 100
Future Classes Attended: 90
Projected Attendance: 75.0 %

Future Attendance Scenario: 80 %
Minimum Future Classes: 300
Future Classes Attended: 240
Projected Attendance: 75.0 %

Future Attendance Scenario: 70 %
Recovery is not possible under this scenario.

==========================================
Attendance analysis completed.
==========================================
```

## 9. Python Concepts Used

- Variables and data types
- Input and output statements
- Arithmetic operators
- Conditional statements (if, elif, else)
- For loops
- Functions
- Function arguments and return values
- Lists
- Basic calculations

## 10. Conclusion

The Attendance Recovery Computation System successfully calculates students' current attendance percentages and determines the minimum number of future classes required to achieve the eligibility threshold.

It evaluates different future attendance scenarios and identifies whether attendance recovery is possible.

This project demonstrates the practical application of Python programming concepts in solving real-world student attendance management problems.

## 11. Project Structure

```text
Attendance-Recovery-System/
│
├── attendance_recovery.py
├── README.md
│
└── screenshots/
    └── output.png
```

## 12. Execution Instructions

1. Install Python on your computer.
2. Open the project folder in Visual Studio Code.
3. Open `attendance_recovery.py`.
4. Run the program using:

```bash
python attendance_recovery.py
```

5. Enter the student details.
6. View the current attendance percentage.
7. Check the future attendance recovery scenarios.
8. Capture the actual program output screenshot.
9. Upload the Python file, README, and screenshot to GitHub.

## 13. Author Details

- **Name:** v.v.s.s.gayathri
- **Roll Number:** N26V01A0388
- **Branch:** CSE
- **Section:** Section-5
- **Subject:** Python Programming
- **Project:** Attendence recovery 
