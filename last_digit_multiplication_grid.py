n = int(input())

for row in range(1, n + 1):
    # TODO: add an inner loop over the columns 1..n.
    # Print each cell's digit without ending the line,
    # and let the print() below close the row.
    for col in range(1, n+1):
        digit = (row * col) % 10
        print(digit, end="")
    print()
