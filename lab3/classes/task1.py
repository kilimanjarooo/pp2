class string:
  def getString(self):
    self.s = str(input())
  def printString(self):
    print(self.s.upper())

answer = string()
answer.getString()
answer.printString()