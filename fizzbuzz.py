# multiples of 3 => FIZZ
# multiples of 5 => BUZZ
# multiples of 3 and 5 => FIZZBUZZ

# First Approach
for i in range(1,101):
    if i % 3 == 0 and i % 5 ==0:
        print("FIZZBUZZ")
    elif i % 3 == 0:
        print("FIZZ")
    elif i % 5 == 0:
        print("BUZZ")
    else:
        print(str(i))
print("END")
