def Prime(num):
  for i in range (2, num):
    if (num%i == 0):
      return False
  return True
class List():
  def __init__(self, a):
    self.a = a
  def filtering(self):
    return list(filter(lambda num : Prime(num), self.a))

myList = List([0, 4, 3, 3, 5, 7, 10, 20, 30, 99, 37, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89])
print(myList.filtering())