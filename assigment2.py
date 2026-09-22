1.

#Catalog ={"laptop" : 800, "mouse" : 20, "keyboard" : 50, "monitor" : 150,}
#print(Catalog)
#item = input("Enter item to buy(or 'checkout' /'exit'): ").lower()
#grand_total = 0
#total_saved = 0
#final_total = 0

#while True :
    #if item in Catalog:
        #price = Catalog[item]
        #grand_total += price
        #print(f"{item} added to order. Price: ${price}")
        #item = input("Enter item to buy(or 'checkout' /'exit'): ").lower()
        
    #elif item == "exit":
        #print("Exiting the program.")
        #break
        
    #elif item == "checkout":
        #if grand_total >=500:
            #total_saved = grand_total * 0.1
            #final_total = grand_total - total_saved
        
        #elif 200<= grand_total < 500:
                    #total_saved = grand_total * 0.05
                    #final_total = grand_total - total_saved
        
        #else:
            #print("no discount")
            
        #print("=============================================")
        #print (f"Grand total: ${grand_total}")
        #print("=============================================")
        #print(f"Total saved: ${total_saved}")
        #print("=============================================")
        #print(f"Final total: ${final_total}")
        #break
        
        
        
    #else:
        #print("item not found in Catalog. try again")
        #break
    
    
2.

#count = int(input("How many student enteries do you want to create?")) 
#student_records = {}

#for i in range(count):
    #student_name = input("Enter student name: ")
    #student_score = int(input("Enter student score: "))
    #student_records[student_name] = student_score
    
    #passed_students = 0
    
    #for student, score in student_records.items():
        #grade = ["A", "B", "C"]
        #status = ["Passed with distinction", "Passed", "needs improvement"]
        
        #if score >= 70:
            #passed_students += 1
            #print(f"{student} scored {score} and got grade {grade[0]} and status {status[0]}")
            
        #elif score >= 50:
            #passed_students += 1
            #print(f"{student} scored {score} and got grade {grade[1]} and status {status[1]}")
            
        #else :
            #print(f"{student} scored {score} and got grade {grade[2]} and status {status[2]}")
            
#total_score = sum(student_records.values())
#class_average = total_score / count

#failed_students = count - passed_students

#print(f"Total number of students who passed: {passed_students}")
#print(f"Total number of students who failed: {failed_students}")
#print(f"Class average: {class_average}")
    
        
3

Raw_user_records = ("userID", "Name", "Role", "Is_Active", "Login_Attempt")   
users =[(101, "Alice", "admin", True, 1),
        (102, "Bob", "member", True, 4),
        (103, "Charlie", "editor", False, 0),
        (104, "Diana", "admin", False, 6),
        (105, "Even", "member", True, 2),
        (106, "Fiona", "guest", True, 0)
        ]
total_active = 0

for user in users:
    if user[4] >= 5:
        print(f"Account for {user[1]} is locked due to too many login attempts.")
    
    if user[3] == True and user[2] == "admin":
        total_active += 1
        print(f"Full system access granted to {user[1]} with userID {user[0]}.")
        
    elif user[3] == True and user[2] == "editor" or user[2] == "member":
        total_active += 1
        print(f"Standard system access granted to {user[1]} with userID {user[0]}.")
        
    elif user[3] == True and user[2] == "guest":
            total_active += 1
            print(f"Standard system access granted to {user[1]} with userID {user[0]}.")
        
    else:
        print(f"Account for {user[1]} is inactive)")
        
total_inactive = len(users) - total_active
total_security_alerts = sum(1 for user in users if user[4] >= 5)

print(f"\n Total Active Users: {total_active} \n Total Inactive Users: {total_inactive} \n Total Security Alerts: {total_security_alerts}")
    