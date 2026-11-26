# Full name input
full_name = "A R C H I E S E L L O T E"

# Convert to uppercase so 'a' and 'A' are treated the same
full_name = full_name.upper()

# 1. Build the unsorted list (letters only, no spaces/symbols, no duplicates)
unsorted_list = []

for letter in full_name:
    # Keep only A-Z letters (skips spaces, punctuation, symbols, numbers)
    if "A" <= letter <= "Z":
        # Add only if we haven't seen this letter yet
        if letter not in unsorted_list:
            unsorted_list.append(letter)

# 2. Copy the unsorted list so we can sort it without changing the original
sorted_list = []
for letter in unsorted_list:
    sorted_list.append(letter)

# 3. Bubble Sort to arrange letters from A to Z
total_letters = len(sorted_list)

for i in range(total_letters):
    for j in range(total_letters - 1):
        # If the left letter comes AFTER the right letter, swap them
        if sorted_list[j] > sorted_list[j + 1]:
            temp = sorted_list[j]
            sorted_list[j] = sorted_list[j + 1]
            sorted_list[j + 1] = temp

# 4. Display results
print("Unsorted:", unsorted_list)
print("Sorted  :", sorted_list)