def isPerfect(num):
  if num == 1:
    return False
  upper = num // 2 + 1
  factorSum = 0
  for i in range(1, upper):
    if num % i == 0:
      factorSum += i
  return num == factorSum

print("if 1 is perfect: ", isPerfect(1))
print("if 2 is perfect: ", isPerfect(2))
print("if 3 is perfect: ", isPerfect(3))
print("if 4 is perfect: ", isPerfect(4))
print("if 5 is perfect: ", isPerfect(5))
print("if 6 is perfect: ", isPerfect(6))
print("if 7 is perfect: ", isPerfect(7))
print("if 8 is perfect: ", isPerfect(8))
print("if 9 is perfect: ", isPerfect(9))
print("if 10 is perfect: ", isPerfect(10))
print("if 28 is perfect: ", isPerfect(28))
