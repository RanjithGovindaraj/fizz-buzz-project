# multiples of 3 => FIZZ
# multiples of 5 => BUZZ
# multiples of 3 and 5 => FIZZBUZZ

# Second Approach
for i in range(1,101):
    t = ""
    if i % 3 == 0:
        t+="FIZZ"
    if i % 5 == 0:
        t+="BUZZ"
    if t == "":
        print(str(i))
