% Code to solve minimum number of 'calculator presses' (either addition or substraction) to get a number with all even digits.  
% For example, input 2018 gives solution 2, input 11 gives solution 3, input 4 gives solution 0.  

import sys 

def check(num): 
% Checks if all digits are even in a number.  
  str_num = str(num)
  for digit in str_num: 
    dig_num = int(digit)
    if dig_num % 2 == 1: 
      return False 
  return True 

def largestOddDigit(int_num): 
% Returns largest odd digit in a given number.  For example, 8315 returns 3.  
  num = str(int_num)
  length = len(num) 
  i = 0 
  while(i < length and int(num[i]) % 2 == 0): 
    i += 1 
  final = length - i - 1
  return final 

def findMin(num):
% Checks both addition and substraction directions, and returns the minimum of the two.  
  int_num = int(num)  
  if check(int_num) : 
    return '0' 
  else: 
    minimum = min(findMinAdd(int_num,0),findMinSub(int_num,0))
    return str(minimum) 
   
def findMinSub(num,count): 
% Recursive function to find the minimum number of presses in the substraction direction.
  if check(num): 
    return count
  str_num = str(num)
  length = len(str_num)
  digit = largestOddDigit(num)
  offset = (10**digit)*(int(str_num[length - digit - 1]))
  toStart = int(str_num[len(str_num) - digit - 1:]) 
  count += toStart - offset + 1
  num = num - (toStart - offset + 1) 
  return findMinSub(num,count) 
  
  
def findMinAdd(num,count): 
% Recursive function to find the minimum number of presses in the addition direction.  
  if check(num): 
    return count
  str_num = str(num)
  length = len(str_num)
  digit = largestOddDigit(num)
  offset = (10**digit)*(int(str_num[length - digit - 1]) + 1)
  toSub = int(str_num[len(str_num) - digit - 1:])
  count += offset - toSub
  num += offset - toSub
  return findMinAdd(num,count)

def toWrite(): 
  file_name = "InputKick3Large.in"
  txt_file = open(file_name, "r")
  numCase = int(txt_file.readline())
  counter = 1 
  new_file = open("output.txt","w")
  while counter <= numCase: 
    line = txt_file.readline()
    new_file.write('Case #' + str(counter) + ': ')
    val = findMin(line)
    new_file.write(str(val) + '\n')
    counter += 1
  
def main(): 
  toWrite()

if __name__ == "__main__":
	sys.exit(main())
