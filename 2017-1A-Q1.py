import sys 

def fillCake(R, C, cake): 
  i = 0
  j = 0
  initial = '?' 
  
  while i < R: 
    if cake[i][0] == '?':
      j = 0 
      while j < C: 
        if cake[i][j] != '?': 
          break 
        j += 1 
      if j!= C:
        oldJ = j
        initial = cake[i][j] 
        while j > 0 : 
          cake[i][j-1] = initial 
          j = j - 1  
        j = oldJ 
        while j < C: 
          if cake[i][j] == '?': 
            initial = cake[i][j-1] 
            cake[i][j] = initial
          j += 1
    else: 
      j = 1
      while j < C: 
        if cake[i][j] == '?': 
          initial = cake[i][j-1] 
          cake[i][j] = initial
        j += 1
    i += 1 
    
  i = 0
  j = 0 
  
  while cake[i][0] == '?': 
    if i == R: 
      break 
    i += 1 
  if i!=R: 
    oldI = i 
    initialRow = cake[i] 
    while i > 0: 
      cake[i-1] = initialRow 
      i = i - 1 
    i = oldI 
    while i < R: 
      if cake[i][0] == '?': 
        initialRow = cake[i - 1] 
        cake[i] = initialRow 
      i += 1 
  return cake
     
def main(): 
 
  file_name = "A-large-practice.in"
  txt_file = open(file_name, "r")
  numCase = int(txt_file.readline())
  counter = 1 
  lineCoutner = 1 
  new_file = open("output.txt","w")
  while counter <= numCase: 
    line = txt_file.readline()
    if (line[0]).isdigit(): 
      cake = [] 
      rowCounter = 0 
      line = line.strip('\n') 
      dimensions = line.split(' ') 
      row = int(dimensions[0])
      col = int(dimensions[1])
    else: 
      line = line.strip('\n') 
      cakeRow = list(line)
      cake.append(cakeRow)     
      rowCounter += 1
    if rowCounter == row:
      newcake = fillCake(row,col,cake) 
      new_file.write('Case #' + str(counter) + ':\n')
      i = 0 
      while i < row: 
        j = 0 
        while j < col:
          new_file.write(str(newcake[i][j]))
          j += 1
        new_file.write('\n')
        i += 1
      counter += 1
  
if __name__ == "__main__":
	sys.exit(main())