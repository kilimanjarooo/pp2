def has_33(nums):
  for x in range(0, len(nums)-1):
    if (nums[x] == nums[x+1] == 3):
      print("True")
      return True
  print("False")
  return False

has_33([1, 3, 3])
has_33([1, 3, 1, 3])
has_33([3, 1, 3])