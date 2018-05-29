#Finds number of natural numbers in range [A,B] such that they are 'legal': aka not divisible by nine and has no digit that is a nine
import sys 

#Checks if any digit is a nine
def hasNine(num):  
  str_num = str(num) 
  for digit in str_num: 
    if digit == '9': 
      return True 
  return False
 
# Checks which is the largest digit that is a 9
def biggest9Digit(str_num): 
  length = len(str_num) 
  i = 0 
  while((i < length) and str_num[i] != '9'): 
    i += 1 
  final = length - i 
  return final 
 
#Recursive function to skip to next number without a nine
def skipToNext(num):
  if not hasNine(num): 
    return num 
  else: 
    str_num = str(num)
    new_num = str_num
    length = len(str_num)
    digit = biggest9Digit(str_num) 
    if digit == length: 
      new_num = 10**digit
    else:  
      numI = int(str_num[-(digit+1)]) + 1
      j = 0 
      end = ''
      while j < digit : 
        j += 1 
        end = end + '0'
      beg = str_num[:-(digit+1)]
      new_num = beg + str(numI) + end
    return skipToNext(int(new_num))

#Find legal numbers in inputed range
def findLegals(F,L): 
  count = 0
  toCheck = int(F) + 1 
  final = int(L)
  while(toCheck < final): 
    if hasNine(toCheck): 
      toCheck = skipToNext(toCheck) 
    else: 
      if toCheck % 9 != 0:
        count += 1 
      toCheck += 1 
  return count + 2
 
def toWrite(): 
  file_name = "A-small-practice.in"
  txt_file = open(file_name, "r")
  numCase = int(txt_file.readline())
  counter = 1 
  new_file = open("output.txt","w")
  while counter <= numCase: 
    line = txt_file.readline()
    line = line.strip('\n')
    A = line.split(' ')
    new_file.write('Case #' + str(counter) + ': ')
    val = findLegals(A[0],A[1])
    new_file.write(str(val) + '\n')
    counter += 1
  
def main(): 
  toWrite()
  
if __name__ == "__main__":
	sys.exit(main())
  
