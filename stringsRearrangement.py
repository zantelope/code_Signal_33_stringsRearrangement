import itertools
  
def stringsRearrangement(inputArray):
  
  ### make lists of all permutations of inputArray
  permutes = list(itertools.permutations(inputArray))
  
  ### variable to store total incorrect characters bewteen adjactent characters across inputArray[i]
  totalIncorrect = 0


  for i in range(len(permutes)):
    for j in range(len(permutes[i]) - 1):

      ### zip of adjacent strings
      comp = zip(permutes[i][j], permutes[i][j + 1])

      ### length of comprehensive list that holds number of all nonequal characters between permutes[i] and permutes[j + 1]
      incorrect=len([c for c,d in comp if c!=d])

      print(permutes[i][j], permutes[i][j + 1])
      print(incorrect)

      ### if no difference between adjactent strings, cannot be True, break loop
      if incorrect == 0:

        ### set totalIncorrect to 0 for the loop, so will not return True if 0 differences occurs on last loop in sequence
        totalIncorrect = 0
        break

      ### add individual incorrect elements to total incorrect across array
      totalIncorrect += incorrect
      
    ### for adjecent elements to all have 1 different char, total incorrect elements will be len(inputArray) - 1, assuming incorrect != 0 (this condition accounted for on line 32)
    ###return True if this is the case
    if totalIncorrect == len(inputArray) - 1:
      return True

    ### otherwise, set totalIncorrect to 0 and start next on iteration of inputArray[i]
    else:
      totalIncorrect = 0
      continue

  ### return False if no permutation returns total character difference of len(inputArray) - 1
  return False
