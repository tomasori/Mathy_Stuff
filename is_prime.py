''''
Source:

https://stackoverflow.com/questions/1801391/how-to-create-the-most-compact-mapping-n-%E2%86%92-isprimen-up-to-a-limit-n

'''

def is_prime(n):
    if n <= 1:          # negative numbers, 0 or 1
        return False
    if n <= 3:          # 2 and 3
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    for i in range(5, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True
