sum = 2 #Start with the first term already added
term = 0
x=1
y=2

while term <= 4000000:
    term = x + y
    x = y
    y = term
    if term % 2 == 0:
        sum +=term

print ("sum value: " + str(sum))
