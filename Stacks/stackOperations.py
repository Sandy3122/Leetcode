stack = []

stack.append(40)
stack.append(50)
stack.append(60)
stack.append(70)
stack.append(80)
stack.pop(1)
print(stack)
stack.pop(3)

print(stack)
# print(stack.isEmpty())



# Stack operations using a list
stack_list = []

# Push
stack_list.append(1)
stack_list.append(2)
stack_list.append(3)

# Peek
top_element = stack_list[-1]
print("Peek:", top_element)

# Pop
popped_element = stack_list.pop()
print("Popped:", popped_element)

# Check if empty
is_empty = len(stack_list) == 0
print("Is Empty:", is_empty)

# Get size
stack_size = len(stack_list)
print("Size:", stack_size)
