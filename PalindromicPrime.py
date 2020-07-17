import numpy as np
import itertools as itr

#...........FIND..ALL..PALINDROMS..COMBINATIONS............

x_set = np.arange(10) #set {0,1...9}
permutations_with_Repetition = [p for p in itr.product(x_set, repeat=6)] # permutation with repetition of the set over 6 places

array_two_d_of_permutations = np.array(permutations_with_Repetition) #convert the result into ndarray # shape (1000000, 6)

# 7[5][1][5]7 our range of values: 700..7 to 7999..7
#we get the first [5] digits
five_elements = array_two_d_of_permutations[:,:-1]
five_elements = five_elements.astype(int)

#we flip the first [5] digits to create the second part palindrome
reversed_five_element = np.flip(five_elements,1) # we reverse the
reversed_five_element = reversed_five_element.astype(int)

sadle_elements = array_two_d_of_permutations[:,-1] # the last element from each combinations with repetition "var: permutations_with_Repetition"
sadle_elements = np.reshape(sadle_elements,(1000000,1)).astype(int)
sadle_elements = sadle_elements.astype(int)

sevens = np.ones((1000000,1))*7 # 7302000000 - 24 h  1000000000000
sevens = sevens.astype(int)
#we concatenate the first five digits with the sadle and with the flipped first elements to get all the palindroms between 799...7 and 7000..7
'''
print(f"first sevens {sevens.shape} + first five digits{five_elements.shape} + saddle digit {sadle_elements.shape} + flipped 5 digits {reversed_five_element.shape}+lest sevens{sevens.shape}")
#OUTPUT : first sevens (1000000, 1) + first five digits(1000000, 5) + saddle digit (1000000, 1) + flipped 5 digits (1000000, 5)+lest sevens(1000000, 1)

'''
temp = np.concatenate(((np.concatenate((np.concatenate((sevens,five_elements),axis=1),sadle_elements),axis=1)),reversed_five_element),axis=1)
polindromes= np.concatenate((temp,sevens),axis=1)

# some concatenations and data type manipulations
polindroms_list = polindromes.astype(str).tolist()
polindroms_list = [''.join(row) for row in polindroms_list]
polindroms_list = list(map(int, polindroms_list))

def check_prime(num):
    # prime numbers are greater than 1
    if num > 1:
        # check for factors
        for i in range(2 ,num):
            if (num % i) == 0:
                break
        else:
            return 1

polindroms_asc = polindroms_list. reverse()

polindroms_asc = np.array(polindroms_asc)
print("53")
print(polindroms_asc)
































