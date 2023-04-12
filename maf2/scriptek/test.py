from math import sqrt

print("na ez itt kiíródik, nincs mese")

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
        
def print_module_name():
    print(__name__)
    
if __name__ == "__main__":
    import sys
    print(is_prime(int(sys.argv[1])))
    print(sys.argv[0])
    #s=input()