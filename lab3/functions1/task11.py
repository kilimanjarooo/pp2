def isPalindrome(str):
  t = "".join(reversed(str))
  if str == t :
    return True

  return False

s = str(input())
print (isPalindrome(s))