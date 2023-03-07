from math import sqrt

def is_prime(n):
    prime_flag = 0

    if(n > 1):
        for i in range(2, int(sqrt(n)) + 1):
            if (n % i == 0):
                prime_flag = 1
                break
        if (prime_flag == 0):
            return True
        else:
            return False
    else:
        return False
        
    
if __name__ == "__main__":
    import sys
    for i in range(10000000):
        print(i, is_prime(i))
    #s=input()