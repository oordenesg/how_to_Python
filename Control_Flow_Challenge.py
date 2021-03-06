# 1. Create a function named large_power() that takes two parameters named base and exponent. 
# If base raised to the exponent is greater than 5000, return True, otherwise return False

def large_power(base,exponent):
  if (base**exponent)>5000:
    return True
  else:
    return False

print(large_power(2, 13)) # should print True
print(large_power(2, 12)) # should print False

# 2. Create a function called over_budget that has five parameters named budget, food_bill, electricity_bill, internet_bill, and rent. 
# The function should return True if budget is less than the sum of the other four parameters — you’ve gone over budget! Return False otherwise.

def over_budget(budget,food_bill,electricity_bill,internet_bill,rent):
  if budget < (food_bill+electricity_bill+internet_bill+rent):
    return True
  else:
    return False

print(over_budget(100, 20, 30, 10, 40)) # should print False
print(over_budget(80, 20, 30, 10, 30)) # should print True

# 3. Create a function named twice_as_large() that has two parameters named num1 and num2.
# Return True if num1 is more than double num2. Return False otherwise.

def twice_as_large(num1,num2):
  if num1 > num2*2:
    return True
  else:
    return False

print(twice_as_large(10, 5)) # should print False
print(twice_as_large(11, 5)) # should print True

# 4. Create a function called divisible_by_ten() that has one parameter named num.
# The function should return True if num is divisible by 10, and False otherwise. Consider using modulo operator % to check for divisibility.

def divisible_by_ten(num):
  if num%10 == 0:
    return True
  else:
    return False

print(divisible_by_ten(20)) # should print True
print(divisible_by_ten(25)) # should print False

# 5. Create a function named not_sum_to_ten() that has two parameters named num1 and num2.
# Return True if num1 and num2 do not sum to 10. Return False otherwise.

def not_sum_to_ten(num1,num2):
  if (num1+num2) != 10:
    return True
  else:
    return False
  
print(not_sum_to_ten(9, -1)) # should print True
print(not_sum_to_ten(9, 1)) # should print False
print(not_sum_to_ten(5,5)) # should print False


# 6. Create a function named in_range() that has three parameters named num, lower, and upper.
# The function should return True if num is greater than or equal to lower and less than or equal to upper. Otherwise, return False.

def in_range(num,lower,upper):
  if (num >= lower) & (num <= upper):
    return True
  else:
    return False

print(in_range(10, 10, 10)) # should print True
print(in_range(5, 10, 20)) # should print False

# 7. Create a function named same_name() that has two parameters named your_name and my_name.
# If our names are identical, return True. Otherwise, return False.

def same_name(your_name, my_name):
  if your_name == my_name:
    return True
  else:
    return False

print(same_name("Colby", "Colby")) # should print True
print(same_name("Tina", "Amber")) # should print False

# 8. Create a function named always_false() that has one parameter named num.
# Using an if statement, your variable num, and the operators >, and <, make it so your function will return False no matter what number is stored in num.
# An if statement that is always false is called a contradiction. You will rarely want to do this while programming, but it is important to realize it is possible to do this.

def always_false(num):
  if (num > 0 and num < 0):
    return True
  else:
    return False

print(always_false(0)) # should print False
print(always_false(-1)) # should print False
print(always_false(1)) # should print False


# 9. Create a function named movie_review() that has one parameter named rating.
# If rating is less than or equal to 5, return "Avoid at all costs!". If rating is between 5 and 9, return "This one was fun.". 
# If rating is 9 or above, return "Outstanding!"

def movie_review(rating):
  if rating <= 5:
    return ("Avoid at all costs!")
  elif (rating > 5) & (rating < 9):
    return ("This one was fun.")
  else:
    return ("Outstanding!")

print(movie_review(9)) # should print "Outstanding!"
print(movie_review(4)) #should print "Avoid at all costs!"
print(movie_review(6)) # should print "This one was fun."

# 10. Create a function called max_num() that has three parameters named num1, num2, and num3.
# The function should return the largest of these three numbers. If any of two numbers tie as the largest, you should return "It's a tie!".

def max_num(num1,num2,num3):
  if (num1 > num2) & (num1 > num3):
    return num1
  elif (num2 > num1) & (num2 > num3):
    return num2
  elif (num1 == num2) | (num1 == num3) | (num2 == num3):
    return ("It's a tie!")
  else:
    return num3

print(max_num(-10, 0, 10)) # should print 10
print(max_num(-10, 5, -30)) # should print 5
print(max_num(-5, -10, -10)) # should print -5
print(max_num(2, 3, 3)) # should print "It's a tie!"

# 11. Create a function called append_size that has one parameter named lst.
# The function should append the size of lst (inclusive) to the end of lst. The function should then return this new list.
# For example, if lst was [23, 42, 108], the function should return [23, 42, 108, 3] because the size of lst was originally 3.

def append_size(lst):
  new_list = lst.append(len(lst))
  return lst

print(append_size([23, 42, 108])) # should print [23, 42, 108, 3]

# 12. Write a function named append_sum that has one parameter — a list named named lst.
# The function should add the last two elements of lst together and append the result to lst. It should do this process three times and then return lst.
# For example, if lst started as [1, 1, 2], the final result should be [1, 1, 2, 3, 5, 8].

ef append_sum(lst):
  new_list = lst
  for i in range(0,3):
    last_element = sum(lst[-2:])
    new_list.append(last_element)
  return new_list

print(append_sum([1, 1, 2])) # should print [1, 1, 2, 3, 5, 8]

# 13. Write a function named larger_list that has two parameters named lst1 and lst2.
# The function should return the last element of the list that contains more elements. If both lists are the same size, then return the last element of lst1.

def larger_list(lst1,lst2):
  if len(lst1) > len(lst2):
    return lst1[-1]
  elif len(lst2) > len(lst1):
    return lst2[-1]
  else:
    return lst1[-1]

print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10])) # should print 5

# 14. Create a function named more_than_n that has three parameters named lst, item, and n.
# The function should return True if item appears in the list more than n times. The function should return False otherwise.

def more_than_n(lst,item,n):
  count = 0
  for i in range(0,len(lst)):
    if item == lst[i]:
      count += 1
  if count > n:
    return True
  else:
    return False
  
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3)) # should print True

# second option

def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

# 15. Write a function named combine_sort that has two parameters named lst1 and lst2.
# The function should combine these two lists into one new list and sort the result. Return the new sorted list.

def combine_sort(lst1,lst2):
  return sorted(lst1+lst2)

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10])) # should print [-10, 2, 2, 4, 5, 5, 10, 10]


# 16. Create a function called every_three_nums that has one parameter named start.
# The function should return a list of every third number between start and 100 (inclusive). 
# For example, every_three_nums(91) should return the list [91, 94, 97, 100]. If start is greater than 100, the function should return an empty list

def every_three_nums(start):
  new_list = []
  if start > 100:
    return new_list
  else:
    for i in range(start,101,3):
      new_list.append(i)
  return new_list
      
print(every_three_nums(91)) # should print [91, 94, 97, 100]

# second option
def every_three_nums(start):
  return list(range(start, 101, 3))

# 17. Create a function named remove_middle which has three parameters named lst, start, and end.
# The function should return a list where all elements in lst with an index between start and end (inclusive) have been removed.
# For example, the following code should return [4, 23, 42] because elements at indices 1, 2, and 3 have been removed:

def remove_middle(lst,start,end):
  return lst[:start]+lst[end+1:]

print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3)) # should print [4, 23, 42]

# 18. Create a function named more_frequent_item that has three parameters named lst, item1, and item2.
# Return either item1 or item2 depending on which item appears more often in lst.
# If the two items appear the same number of times, return item1.

def more_frequent_item(lst,item1,item2):
  if lst.count(item1) > lst.count(item2):
    return item1
  elif lst.count(item2) > lst.count(item1):
    return item2
  else:
    return item1

print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3)) # should print 3


# 19. Create a function named double_index that has two parameters: a list named lst and a single number named index.
# The function should return a new list where all elements are the same as in lst except for the element at index. 
# The element at index should be double the value of the element at index of the original lst.
# If index is not a valid index, the function should return the original list.
# For example, the following code should return [1,2,6,4] because the element at index 2 has been doubled:
# double_index([1, 2, 3, 4], 2)

def double_index(lst,index):
  if index in range(0,len(lst)):
    lst[index] = lst[index]*2
    return lst
  else:
    return lst

print(double_index([3, 8, -10, 12], 2)) # should print [3, 8, -20, 12]

# 20. Create a function called middle_element that has one parameter named lst.
# If there are an odd number of elements in lst, the function should return the middle element. 
# If there are an even number of elements, the function should return the average of the middle two elements.

def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

print(middle_element([5, 2, -10, -4, 4, 5])) # should print -7.0

# 21. Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.
# Return the count of how many numbers in the list are divisible by 10.

def divisible_by_ten(nums):
  count = 0
  for i in nums:
    if i%10 == 0:
      count += 1
  return count

print(divisible_by_ten([20, 25, 30, 35, 40])) # should print 3

# 22. Create a function named add_greetings() which takes a list of strings named names as a parameter.
# In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.
# Return the new list containing the greetings.

def add_greetings(names):
  greeting_list = []
  for i in names:
    greeting_list.append('Hello, ' + i)
  return greeting_list

print(add_greetings(["Owen", "Max", "Sophie"])) # ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']

# 23. Write a function called delete_starting_evens() that has a parameter named lst.
# The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.
# For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].
# Make sure your function works even if every element in the list is even!

def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0)
    lst = lst[1:]
  return lst

print(delete_starting_evens([4, 8, 10, 11, 12, 15])) # should print [11,12,15]
print(delete_starting_evens([4, 8, 10])) # should print []

# 24. Create a function named odd_indices() that has one parameter named lst.
# The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.
# For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

def odd_indices(lst):
  new_list = []
  for i in range(0,len(lst)):
    if i%2 != 0:
      new_list.append(lst[i])
  return new_list

print(odd_indices([4, 3, 7, 10, 11, -2])) # should print [3, 10, -2]

# second option

def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst

# 25. Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.
# For example, consider the following code.
# exponents([2, 3, 4], [1, 2, 3])
# the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.

ef exponents(bases,powers):
  new_list = []
  for i in range(0,len(bases)):
    for j in range(0,len(powers)):
      new_list.append(bases[i]**powers[j])
  return new_list

print(exponents([2, 3, 4], [1, 2, 3])) # should print [2, 4, 8, 3, 9, 27, 4, 16, 64]

# 26. Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.
# The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

def larger_sum(lst1,lst2):
  if sum(lst1) == sum(lst2):
    return lst1
  else:
    if sum(lst1) > sum(lst2):
      return lst1
    else:
      return lst2

print(larger_sum([1, 9, 5], [2, 3, 7])) # should print [1, 9, 5]

# 27. Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.
# The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.
# For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

def over_nine_thousand(lst):
  sum_over = 0
  if lst == []:
    return 0
  else:
    for i in lst:
      sum_over += i
      if sum_over >= 9000:
        break
    return sum_over

print(over_nine_thousand([8000, 900, 120, 5000])) # should print 9020

# 28. Create a function named max_num() that takes a list of numbers named nums as a parameter.
# The function should return the largest number in nums

ef max_num(nums):
  return max(nums)

print(max_num([50, -10, 0, 75, 20])) # should print 75

# second option

def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum


# 29. Write a function named same_values() that takes two lists of numbers of equal size as parameters.
# The function should return a list of the indices where the values were equal in lst1 and lst2.
# For example, the following code should return [0, 2, 3]

def same_values(lst1,lst2):
  index_list = []
  for i in range(0,len(lst1)):
    if lst1[i] == lst2[i]:
      index_list.append(i)
  return index_list

print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])) # should print [0, 2, 3]

# 30. Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.
# The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.
# For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

def reversed_list(lst1,lst2):
  if lst1 == lst2[::-1]:
    return True
  else:
    return False

print(reversed_list([1, 2, 3], [3, 2, 1])) # should print True
print(reversed_list([1, 5, 3], [3, 2, 1])) # should print False

# 31. Write a function named tenth_power() that has one parameter named num.
# The function should return num raised to the 10th power.

def tenth_power(num):
  return num**10

print(tenth_power(1)) # 1 to the 10th power is 1
print(tenth_power(0)) # 0 to the 10th power is 0
print(tenth_power(2)) # 2 to the 10th power is 1024

# 32. Write a function named square_root() that has one parameter named num.
# Use exponents (**) to return the square root of num.

def square_root(num):
  return num**(1/2)

print(square_root(16)) # should print 4
print(square_root(100)) # should print 10

# 33. Create a function called win_percentage() that takes two parameters named wins and losses.
# This function should return out the total percentage of games won by a team based on these two numbers.

def win_percentage(wins,losses):
  return (wins/(wins+losses))*100

print(win_percentage(5, 5)) # should print 50
print(win_percentage(10, 0)) # should print 100

# 34. Write a function named average() that has two parameters named num1 and num2.
# The function should return the average of these two numbers.

def average(num1,num2):
  return (num1+num2)/2

print(average(1, 100)) # The average of 1 and 100 is 50.5
print(average(1, -1)) # The average of 1 and -1 is 0

# 35. Write a function named remainder() that has two parameters named num1 and num2.
# The function should return the remainder of twice num1 divided by half of num2.

def remainder(num1,num2):
  return (num1%(num2/2))*2

print(remainder(15, 14)) # should print 2
print(remainder(9, 6)) # should print 0

