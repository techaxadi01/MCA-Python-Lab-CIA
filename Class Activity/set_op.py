'''
create two set to student(java,python)
print students learning python
print student learning java
print student learning both
print studens learning either python or java
print students learning python but no java
'''


py = {"Aman", "Priya", "Rahul", "Sneha"}
j = {"Rahul", "Sneha", "Vikram", "Neha"}

print("print students learning python",py)
print("print student learning java",j)
print("print student learning both",py&j)
print("print studens learning either python or java",py|j)
print("print students learning python but no java",py-j)
