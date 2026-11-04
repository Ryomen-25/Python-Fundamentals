year = int(input())

# One boolean expression over `year` goes here. It must be True for exactly
# the leap years. Replace False; do not change the printing below.
is_leap = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

if is_leap:
    print("leap")
else:
    print("not leap")
