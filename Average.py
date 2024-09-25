x = int(input("Enter a number: "))
y = int(input("Enter another number: "))
z = int(input("Enter another number: "))

sum = x + y + z
avg = sum/3

print("Sum = " , sum)
print(f"{x} + {y} + {z} = {sum}")
print("Average = " , avg)
print("Average = %0.2f" %avg)