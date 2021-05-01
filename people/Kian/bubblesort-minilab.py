def numberSort():
  List = []
  userinput = int(input("Input number of values: "))
  for i in range(userinput):
      value = int(input("Please enter the %d th value of the list: " %i))
      List.append(value)

  for i in range(userinput -1):
      for j in range(userinput - i - 1):
          if(List[j] > List[j + 1]):
               temp = List[j]
               List[j] = List[j + 1]
               List[j + 1] = temp

  print("Sorted list from smallest to biggest: ", List)
  choice()

def stringSort():
  stringInput = input("Please enter the words separated by spaces: ")

  words = [word.lower() for word in stringInput.split()]

  # sort the list
  words.sort()

  # display the sorted words

  print("Words in alphabetical order:")
  for word in words:
     print(word)
  choice()

def choice():
  print("\n\n1. Sort numbers (least to greatest) \n2. Sort words alphabetically")
  answer = int(input("\n\nType either 1 or 2: "))
  if answer == 1:
    numberSort()
  elif answer == 2:
    stringSort()
  else:
    print("Invalid input, try again!")
    redo()

def redo():
    choice()
choice()
