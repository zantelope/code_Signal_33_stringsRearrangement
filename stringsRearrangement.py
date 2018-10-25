import itertools
  
def stringsRearrangement(inputArray):
  ### make lists of all permutations of inputArray

  permutes = list(itertools.permutations(inputArray))
  print (permutes)

  ### go through lists and compare consecutive strings
  ### if all consecutive strings differ by one character (determined by 
  ### len(inputArray) - 1)
  ### return true
  for i in range(len(permutes)):
    for j in range(len(permutes[i]) - 1):
      comp = zip(permutes[i][j], permutes[i][j + 1])
      incorrect=len([c for c,d in comp if c!=d])
      print(permutes[i][j], permutes[i][j + 1])
    print ("***")
    if incorrect == len(inputArray) - 1:
      return True





inputArray = ["ab", "bb", "aa"]

stringsRearrangement(inputArray)



'''a='aa'
b='ab'


words=zip(a,b)
incorrect=len([c for c,d in words if c!=d])
print(incorrect)
for i, j in zip(a,b):
  print(i, "...", j)'''
