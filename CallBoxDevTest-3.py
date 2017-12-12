def is_power_two (my_num):
    if my_num == 0:
        return False

    while (my_num != 1):
        if my_num%2 != 0:
            return False
        my_num = my_num/2
    return True

print is_power_two(18)

# Why this will work for any integer input it receives?

# -Because the while loop works until the number is 1
# -Numbers that are power of two will loop thorugh the while and return True
# -Odd numbers will return False
# -Even numbers that are not powers of 2 will be divided by 2 unless they are equal to an odd number whereafter the loop returns False