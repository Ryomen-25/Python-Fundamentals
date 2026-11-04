n = int(input())

# TODO: print the ten lines of the table for n, one line per product.
# Loop over the numbers 1 through 10 and build each line with an f-string.
# Nothing is printed yet, so every test fails until you add the loop.
lst = [1,2,3,4,5,6,7,8,9,10]
for num in range(len(lst)):
  print(f"{n} x {lst[num]} = {n * lst[num]} ")

