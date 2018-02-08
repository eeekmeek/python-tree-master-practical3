# Displaying matrix of 0s and 1s

import random
#random.randint(0,1)

def print_matrix(n):
    for i in range(n):
        for j in range(n):
            print(random.randint(0,1),end=" ")
        print()

print_matrix(5)
