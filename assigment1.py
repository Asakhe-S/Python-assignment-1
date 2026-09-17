1. 

personal_info = {'Name': 'Asakhe', 'Age': 25, 'Height': 175.0, 'Student': True}

#print(f"Name: {personal_info['Name']}")
#print(f"Age: {personal_info['Age']}")
#print(f"Height: {personal_info['Height']}")
#print(f"Student: {personal_info['Student']}")

2.
data_type = {'name': "abdurrahman", 'age': 25, 'height': 1.75, 'is_student': True}

#print(f"String: {str(data_type['name'])}")
#print(f"Integer: {int(data_type['age'])}")
#print(f"Float: {float(data_type['height'])}")
#print(f"Boolean: {bool(data_type['is_student'])}")

3.
favourite_foods = ["burger", "pizza", "sushi", "pasta", "ice cream"]

#print(favourite_foods)
#print(favourite_foods[0])  # Accessing the first item
#print(favourite_foods[-1])  # Accessing the third item

favourite_foods.append("chicken")
#print(favourite_foods)  # Adding a new item to the list

favourite_foods.remove("pizza")
#print(favourite_foods)  # Removing an item from the list

favourite_foods[2] = "chocolate"  # Changing an item in the list
#print(favourite_foods)  # Printing the Changed list

#print(favourite_foods)  # Printing the final list

4.
scores = [75, 80, 65, 90, 85]

#print(f"Scores: {scores}")
#print(f"Highest Score: {max(scores)}")  # Finding the highest score
#print(f"Lowest Score: {min(scores)}")  # Finding the lowest score

scores.append(100)  # Adding a new score

#print(f"Updated Scores: {scores}")

5.

week_days = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

#print(f"Week Days: {week_days}")
#print(f"First Day: {week_days[0]}")  # Accessing the first day  
#print(f"Last Day: {week_days[-1]}")  # Accessing the last day  

#week_days[5] = "Funday"  # Attempting to change a tuple item 
#print(week_days) 

#i got an error 

# A tuple is different from a list because in some cases we need a list of items stored in a variable to be immutable

6.

numbers = [1, 2 ,3, 4, 2, 5, 3, 6, 1]

#print(set(numbers))

#Sets doesn't allow duplicates, which is why certain values disappeared when I converted the list to a set

7.

Languages = ["Python", "Java", "Python", "C++", "JavaScript", "Python"]

#print(set(Languages))

Languages.append("Django") # Attempting to add an item to a set 
#print(set(Languages))  

8.

Student = {"Name" : "Sinawo", "Age" : 20, "course" : "Medicine", "Level" : "3rd Year", "Skills" : ["Diagnostic", "Presentation", "Reasoning"]}

#print(f"Student Info: {Student}") #printing the entire dictionary
#print(f"Student Name: {Student['Name']}") #printing the value of the key "Name"

Student["Email"] = "sinawo@gmail.com" #Adding a new key-value pair to the dictionary
#print(f"Student Info: {Student}")

Student["Level"] = "final year" #Updating the value of the key "Level"
#print(f"Student Info: {Student}") 

del Student["Age"] #Removing the key-value pair with the key "Age"
#print(f"Student Info: {Student}") 

9.

Student_1 ={"Name" : "Amanda", "Age" : 23, "course" : "Data Science", "Skills" : ["Python", "SQL", "Machine Learning"]}
#print(f"Name: {Student_1['Name']}") 
#print(f"Age: {Student_1['Age']}")
#print(f"Course: {Student_1['course']}")
#print(f"Skills: {(Student_1['Skills'])}") 

Student_2 ={"Name" : "Buhle", "Age" : 19, "course" : "Frontend Developer", "Skills" : ["HTML", "CSS", "JavaScript"]} 
#print(f"Name: {Student_2['Name']}") 
#print(f"Age: {Student_2['Age']}")
#print(f"Course: {Student_2['course']}")
#print(f"Skills: {(Student_2['Skills'])}") 

Student_3 ={"Name" : "Thando", "Age" : 21, "course" : "Backend Developer", "Skills" : ["Python", "Django", "Flask"]} 
print(f"Name: {Student_3['Name']}") 
print(f"Age: {Student_3['Age']}")
print(f"Course: {Student_3['course']}")
print(f"Skills: {(Student_3['Skills'])}") 


