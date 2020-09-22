
from random import randrange
def shuffle(card, n):

    for i in range(n):
        r = i + randrange(n - i)
        card[i], card[r] = card[r], card[i]

if __name__ == "__main__":
    a=[0, 1, 2, 3, 4, 5, 6, 7, 8, 
    9, 10, 11, 12, 13, 14, 15, 
    16, 17, 18, 19, 20, 21, 22,  
    23, 24, 25, 26, 27, 28, 29, 
    30, 31, 32, 33, 34, 35, 36, 
    37, 38, 39, 40, 41, 42, 43,  
    44, 45, 46, 47, 48, 49, 50, 
    51] 
    shuffle(a, 52)
    print(a)