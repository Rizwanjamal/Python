# Array Initialization 
cars = ["Mira", "Corolla"];

# Array Insertion
cars.append("BMW");

# Array Insertion At Specific Position
cars.insert(1, "Honda");

# Array Slice
favouriteCars = cars[1:];

print('Cars:', cars);
print('favouriteCars', favouriteCars);

# Get Specific Array Value By Index 
tasks = ["email Frank", "call Sarah", "meet with Zain", "discuss strategies with Rizwan"]
print(tasks[0]) #is "email Frank"
print(tasks[1]) #is "call Sarah"
print(tasks[2]) #is "meet with Zach"

# Remove Array Element by Index
taskAccomplished = tasks.pop(2)  
print('taskAccomplished :', taskAccomplished) # meet with Zain

# Delete task at index 0
del tasks[0] # Deleted "email Frank"
print(tasks) # Remaining tasks will be ["call Sarah", "meet with Zain"]

# Delete task by value instead of index
tasks.remove("call Sarah") # Deleted "call Sarah"
print(tasks)



