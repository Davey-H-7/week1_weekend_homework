# For the following list of numbers:

numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even = []
for number in numbers:
    if number % 2 == 0:
      even.append(number)
print (even)


# 2. Print the difference between the largest and smallest value:
value_min = min(numbers)
value_max = max(numbers)
print (value_max - value_min)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
result = False
check = None
for number in numbers:
    if number == 2 and number == check:
        result = True
    check = number
   
print (result)
      


# 4. Print the sum of the numbers, 
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
sum = 0
allowed = True
for number in numbers:
    if number == 6 or allowed ==False:
        allowed = False
        if number == 7:
            allowed = True
    else:
        sum += number

print(sum)


# 5. HARD! Print the sum of the numbers. 
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#
#    So [5, 13, 2] would have sum of 5. 

total_sum = 0
previous = None
for number in numbers:
    if number != 13 and previous != 13:
        total_sum += number
    previous = number


print (total_sum)








