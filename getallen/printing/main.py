# Number of completed transactions
completed = 60 // 7
# Number of remaining minutes
minutes = 60 % 7
# Set the number of remaining transactions
remaining_tasks = 10 - completed
# Set the total time needed to complete all transactions
required_time = 10 * 7

# Print the results
print("The number of remaining transactions is", remaining_tasks)
print("The number of minutes needed to complete all transactions is", required_time)