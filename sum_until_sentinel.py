total = 0

# TODO: keep reading integers and adding them to total.
# Stop as soon as the value you read is the sentinel, and leave it out of the total.
sentinel = 0
while True:
  num = int(input( ))
  if num == sentinel:
      break
  
  total += num

print(total)

