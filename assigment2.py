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
            
        #print(f"Grand total: ${grand_total} \n Total saved: ${total_saved} \n Final total: ${final_total}")  
        #break
    #else:
        #print("item not found in Catalog. try again")
        #break
    
    
2.

count = int(input("How many student enteries do you want to create?")) 
student_records = {}

for i in range(count):
    student_name = input("Enter student name: ")
    student_score = int(input("Enter student score: "))
    student_records[student_name] = student_score
    
    passed_students = 0
    
    for student, score in student_records.items():
        grade = ["A", "B", "C"]
        status = ["Passed with distinction", "Passed", "needs improvement"]
        
        if score >= 70:
            passed_students += 1
            print(f"{student} scored {score} and got grade {grade[0]} and status {status[0]}")
            
        elif score >= 50:
            passed_students += 1
            print(f"{student} scored {score} and got grade {grade[1]} and status {status[1]}")
            
        else :
            print(f"{student} scored {score} and got grade {grade[2]} and status {status[2]}")
            
total_score = sum(student_records.values())
class_average = total_score / count

failed_students = count - passed_students

print(f"Total number of students who passed: {passed_students}")
print(f"Total number of students who failed: {failed_students}")
print(f"Class average: {class_average}")
    
        
    
    