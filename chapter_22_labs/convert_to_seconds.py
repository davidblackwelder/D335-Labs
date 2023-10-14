# Write a program that reads in hours, minutes, and seconds as input, and outputs the time in seconds only.

# Ex: If the input is:

# 1
# 6
# 40
# where 1 is the number of hours, 6 is the number of minutes, and 40 is the number of seconds, the output is:

# Seconds: 4000

hours = int(input())
minutes = int(input())
seconds = int(input())

hours_in_seconds = (hours * 60) * 60
minutes_in_seconds = minutes * 60
total_time_in_seconds = hours_in_seconds + minutes_in_seconds + seconds

print('Seconds:', total_time_in_seconds)