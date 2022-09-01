import sys

try:
    args = sys.argv[1:]
except:
    print('Argument were not assigned on script initialization ')

def main(number):
    for n in range(number-1, 1, -1):
        if number % n == 0:
            return False, n
    return True, 1

if __name__ == "__main__":
    for arg in args:
        result, largest_factor = main(int(arg))
        print(f"{arg} is {('Not', '')[result]} a prime number")
