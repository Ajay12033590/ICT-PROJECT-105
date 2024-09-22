

subjects = ["Introduction to Programming",
    "Calculus I",
    "Data Structures and Algorithms",
    "Linear Algebra",
    "Physics I",
    "Chemistry I",
    "Biology I",
    "Microeconomics",
    "Macroeconomics",
    "Psychology I",
    "History I",
    "English Composition I",
    "Introduction to Philosophy",
    "Calculus II",
    "Discrete Mathematics"]

# Print the list in its original order.

print(subjects)

# Sort the list alphabetically without modifying the original list.
sort_subjects = sorted(subjects)
print(sort_subjects)

# Print the list in reverse alphabetical order using sorted().

reverse_sort_subjects = sorted(subjects, reverse=True)
print(reverse_sort_subjects)
# Reverse the order of the list using reverse().
subjects.reverse()
print(subjects)

# Reverse the list back to its original order.
subjects.reverse()
print(subjects)

# Sort the list alphabetically and store it.

subjects.sort()
print(subjects)

#Sort the list in reverse alphabetical order and store it.

subjects.sort(reverse=True)
print(subjects)


# Use sorted() and print the available subjects with a message.

sorted_subjects = sorted(subjects)
print("The following courses are available for expression of interest if the students meet the prerequisites:")
for subjects in sorted_courses:
    print(subjects)
# Replace a subject and print a message.

subjects[0] = "Advanced Python Programming"
print("The subject'Psychology I' has been replaced with 'Advanced Python Programming'.")
#Insert new subjects and append a subjects.

subjects.insert(0, "Artificial Intelligence")
subjects.insert(len(courses)//2, "Data Science")
subjects.append("Cybersecurity")
print(subjects)
# Use pop() to remove subjects.

removed_subjects = [subjects.pop() for _ in range(4)]
print(f"The following subjects are unavailable due to technical issues: {', '.join(removed_subjects)}")

# Create a list of tuples.

subjects_data = [
    (1, "Introduction to Programming"),
    (2, "Calculus I"),
    (3, "Data Structures and Algorithms"),
    (4, "Linear Algebra"),
    (5, "Physics I"),
    (6, "Chemistry I"),
    (7, "Biology I"),
    (8, "Microeconomics"),
    (9, "Macroeconomics"),
    (10, "Psychology I")
]
# Loop through tuples and extract names.

subjects_names = []
for subjects_id, subjects_name in subjects_data:
    subjects_names.append(subjects_name)
# Print the subjects names
print("subjects Names:", subjects_names)