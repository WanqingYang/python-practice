def isComposite(num):
  if num < 4:
    return False
  i = 2
  while i * i <= num:
    if num % i == 0:
      return True
    i += 1
  return False

print("if 1 is composite: ", isComposite(1))
print("if 1 is composite: ", isComposite(2))
print("if 1 is composite: ", isComposite(3))
print("if 1 is composite: ", isComposite(4))
print("if 1 is composite: ", isComposite(5))
print("if 1 is composite: ", isComposite(6))
print("if 1 is composite: ", isComposite(7))
print("if 1 is composite: ", isComposite(8))
print("if 1 is composite: ", isComposite(9))
print("if 1 is composite: ", isComposite(10))
