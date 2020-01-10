#two important keywords when working with loops - these are 'break' and 'continue'
#--------
# nums = [1,2,3,4,5]
# for num in nums:
#     if num == 3:
#         print('Found!')
#         continue
#     print(num)

""" output will be:
1
2
Found!
4
5
"""
#---------

#--------
#Loop within a loop

# nums = [1,2,3,4,5]
# for num in nums:
#     for letter in 'abc':
#         print(num, letter)

#-----------

#------------
#Range is a function which allows function to loop certain number of times. For e.g. just run through a loop ten times.
# for i in range (10):
#      print(i)
#Output: Starts at 0 and print until 9 (not including this number we passed.
""" 
0
1
2
3
4
5
6
7
8
9
 """
 #if we don't want to start at 0 we can also pass a starting value into range
# for i in range (1,11):
x = 0
while x <= 10:
    print("a")
    x += 1
    x = x+1
