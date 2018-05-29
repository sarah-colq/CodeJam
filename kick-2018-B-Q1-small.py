import sys 

def hasNine(num):  
  str_num = str(num) 
  for digit in str_num: 
    if digit == '9': 
      return True 
  return False
  
def biggest9Digit(str_num): 
  length = len(str_num) 
  i = 0 
  while((i < length) and str_num[i] != '9'): 
    i += 1 
  final = length - i 
  return final 
  
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
    print(A)
    new_file.write('Case #' + str(counter) + ': ')
    val = findLegals(A[0],A[1])
    new_file.write(str(val) + '\n')
    counter += 1
  
def main(): 
  print(findLegals('16','26'))
  print(findLegals('88','102'))
  toWrite()
  
if __name__ == "__main__":
	sys.exit(main())
  
