def histogram(nums):
  for i in nums:
        while i > 0:
            print("*", end = "")
            i -= 1
        print('')

histogram([1,2,4,0,0,7,5])