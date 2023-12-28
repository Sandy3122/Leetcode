arr = [1, 0, 1, 2, 3, 4, 5, 5, 5, 0, 1, 6, 9, 8, 7, 5, 4, 4]

hashMap = {}
for num in arr:
    if num in hashMap:
        hashMap[num] += 1
    else:
        hashMap[num] = 1

sortedKeys = sorted(hashMap.keys())

for key in sortedKeys:
    print(f"{key}: {hashMap[key]}")




# Finding the maximum element in the array
max_element = max(arr)

# Initialize frequency array with zeros
frequency = [0] * (max_element + 1)
print(frequency)

# Count occurrences of each number in the array
for num in arr:
    frequency[num] += 1

# Display the frequencies in increasing order
for i in range(len(frequency)):
    if frequency[i] > 0:
        print(f"{i}: {frequency[i]}")
