import sys 

def generateString(parameters):
  s1 = parameters[0]
  s2 = parameters[1]
  N = int(parameters[2])
  A = int(parameters[3])
  B = int(parameters[4]) 
  C = int(parameters[5])
  D = int(parameters[6])
  i = 2 
  s = s1 + s2 
  x = [] 
  x.append(ord(s1))
  x.append(ord(s2)) 
  while i < N : 
    x.append(( A * x[i-1] + B * x[i-2] + C ) % D)
    s += chr(97 + ( x[i] % 26 ))
    i += 1 
  return s 

def checkWord(word,text): 
  length = len(word) 
  first = word[0] 
  last = word[length - 1] 
  middle = sorted(word[1:length-1])
  cutoff = text[:-(length - 1)]
  i = 0 
  for letter in cutoff: 
    if letter == first: 
      if text[i + length - 1] == last: 
        b = sorted(text[i+1:i+length-1])
        if middle == b: 
          return 1 
    i+=1
  return 0   
  
def checkWords(wordList,text): 
  count = 0 
  for word in wordList: 
    count += checkWord(word,text)
  return count 

def toWrite(): 
  file_name = "C-large-practice.in"
  txt_file = open(file_name, "r")
  numCase = int(txt_file.readline())
  print(numCase)
  counter = 1 
  new_file = open("output.txt","w")
  while counter <= numCase: 
    print(counter)
    smallCount = int(txt_file.readline()) 
    line = txt_file.readline()
    line = line.strip('\n')
    words = line.split(' ') 
    line = txt_file.readline()
    line = line.strip('\n')
    parameters = line.split(' ') 
    wordCount = checkWords(words,generateString(parameters))
    new_file.write('Case #' + str(counter) + ': ')
    new_file.write(str(wordCount) + '\n')
    counter += 1
    
def main(): 
  # print(checkWords(['axpaj', 'apxaj', 'dnrbt', 'pjxdn','abd'],generateString(['a','a',50,1,1,1,30])))
  toWrite()

if __name__ == "__main__":
	sys.exit(main())
  