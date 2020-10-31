# multiples of 3 => FIZZ
# multiples of 5 => BUZZ
# multiples of 3 and 5 => FIZZBUZZ

# Second Approach
for i in range(1,301):
    t = ""
    if i % 3 == 0:
        t+="FIZZ"
    if i % 5 == 0:
        t+="BUZZ"
    if t == "":
        print(str(i))
print("GIT WORKSHOP")
print("Test for Nano editor")
print("I made a change in branch-to-merge")
print("I am in master branch fizzbuzz2.py")
