string = "It can be painful to learn from mistakes"

# Extract necessary words
learn = string[string.index('learn'):string.index('learn') + len('learn')]
painful = string[string.index("painful"):string.index("painful") + len("painful")]
mistakes = string[string.index("mistakes"):string.index("mistakes") + len("mistakes")]


print("The variable learn equals:", learn)
print("The variable painful equals:", painful)
print("The variable mistakes equals:", mistakes)