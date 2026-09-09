'''
create two set to student(java,python)
print students learning python
print student learning java
print student learning both
print studens learning either python or java
print students learning python but no java
'''

# Student enrollment sets
py = {"Aman", "Priya", "Rahul", "Sneha"}
j = {"Rahul", "Sneha", "Vikram", "Neha"}

# 1. Students enrolled in Python
print("print students learning python", py)

# 2. Students enrolled in Java
print("print student learning java", j)

# 3. Students enrolled in both (Intersection: &)
print("print student learning both", py & j)

# 4. Students enrolled in either Python or Java (Union: |)
print("print studens learning either python or java", py | j)

# 5. Students enrolled in Python but not Java (Difference: -)
print("print students learning python but no java", py - j)
