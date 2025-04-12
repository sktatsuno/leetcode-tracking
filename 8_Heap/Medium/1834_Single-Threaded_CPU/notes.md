Could have used enumerate with list comprehension instead of the way I sorted tasks. You generally do not want to mutate the original input 

I made the mistake of having an infinite while loop because didn't add in tasks[i][0] <= t condition

Refactored to create copy of original array and also use tuples instead of lists for the tasks data

And use slightly improved while condition for iterating through the tasks