import sys 

def box(string): 
  length = len(string) 
  ret = '+' 
  for i in range(0,length + 2): 
    ret += '-'
  ret = ret +  '+' + '\n' + '| ' + string + ' |' + '\n' + '+' 
  for i in range(0,length + 2): 
    ret += '-'
  ret = ret + '+' + '\n' 
  return ret 

def toWrite(): 
  file_name = "A-small-womenIO2014.in"
  txt_file = open(file_name, "r")
  numCase = int(txt_file.readline())
  print(numCase)
  counter = 1 
  lineCoutner = 1 
  new_file = open("output.txt","w")
  while counter <= numCase: 
    print(counter)
    line = txt_file.readline()
    line = line.strip('\n') 
    new_file.write('Case #' + str(counter) + ':\n') 
    new_file.write(box(line)) 
    counter += 1
    
def main(): 
  toWrite()
  
if __name__ == "__main__":
	sys.exit(main())