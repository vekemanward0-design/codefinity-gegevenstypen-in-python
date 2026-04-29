string = "My goal is to achieve way beyond what I expected"
# Extract the very last symbol using negative indexation
symbol1 = string[-1]
# Extract the very last symbol using `len()` function
symbol2 = string[len(string) - 1]

# Print symbols
print("Variable symbol1 equals:", symbol1)
print("Variable symbol2 equals:", symbol2)