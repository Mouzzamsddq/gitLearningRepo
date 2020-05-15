n=int(input())
physics_student=[]
for i in range(n):
    student=[]
    name=input()
    grades=float(input())
    student.append(name)
    student.append(grades)
    physics_student.append(student)
dict_phy_student=dict(physics_student )
l1,l2=zip(*physics_student)
names=list(l1)
grades=sorted(list(l2))
min_grades=min(grades)
grades.remove(min_grades)
new_grades=[]
for i in grades:
    if min_grades!=i:
        new_grades.append(i)
        

# print(new_grades)
check=True
while check:
    if new_grades[0]!=new_grades[-1]:
        new_grades.pop()
    else:
        check=False
# print(new_grades)
updated_dict={}
for name,grade in dict_phy_student.items():
    if grade in new_grades:
        updated_dict[name]=grade
    else:
        pass 
second_lowest=sorted(updated_dict)
for name in second_lowest:
    print(name)
           
print("Hello I am Mouzzam Siddiqui modification for git hub")