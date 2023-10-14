# People find it easier to read time in hours, minutes, and seconds rather than just seconds.

# Write a program that reads in seconds as input, and outputs the time in hours, minutes, and seconds.

# Ex: If the input is:

# 4000
# the output is:

# Hours: 1
# Minutes: 6
# Seconds: 40


# Get the seconds from the user
seconds = int(input())

# Calculate the hours from the total number of seconds by 3600 (1 hour is equal to 3600 seconds)
hours = seconds // 3600

# Calculate the remaining number of seconds from step 2
remaining_seconds_minus_hours = seconds - (hours * 3600)

# Calculate the minutes from the remaining number of seconds calculated from step 3 by dividing the remaining number of seconds by 60 (1 minute is equal to 60 seconds)
minutes = remaining_seconds_minus_hours // 60

# Calculate the remaining number of seconds from step 4
remaining_seconds = seconds - ((minutes * 60) + (hours * 3600))

# Display the hours from step 2
print('Hours:', hours)
# Display the minutes from step 4
print('Minutes:', minutes)
# Display the seconds from step 5
print('Seconds:', remaining_seconds)
