def numberSort(userinput):
    for i in range(len(userinput) - 1, 0, -1):
        for j in range(i):
            if userinput[j] > userinput[j + 1]:
                temp = userinput[j]
                userinput[j] = userinput[j + 1]
                userinput[j + 1] = temp

def stringSort(stringInput):
  words = [word.lower() for word in stringInput.split()]

  # sort the list
  words.sort()

  # display the sorted words

  print("Words in alphabetical order:")
  for word in words:
     print(word)

if __name__ == '__main__':
    userinput = [5, 3, 8, 6, 7, 2, 9]
    stringInput = "flower, palm, find, run, banana, cup"
    print("start", userinput)
    numberSort(userinput)
    print("finish", userinput)
    print("beginning string:", stringInput)
    stringSort(stringInput)
