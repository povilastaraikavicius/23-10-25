# Write a function that takes two lists and adds the first element in the first list 
# with the first element in the second list, the second element in the first list with the 
# second element in the second list, etc, etc. Return True if all element combinations add up to 
# the same number. Otherwise, return
# False. Example:
# Parašykite funkciją, kuri paima du sąrašus ir prie pirmojo sąrašo pirmojo elemento prideda 
# antrojo sąrašo pirmąjį elementą, antrojo sąrašo antrąjį elementą, antrojo sąrašo antrąjį 
# elementą ir antrojo sąrašo antrąjį elementą. pirmąjį sąrašą su antruoju antrojo sąrašo 
# elementu ir t. t., ir t. t. Grąžinkite True, jei visi elementų deriniai sudaro tą patį skaičių. 
# Priešingu atveju grąžinama False. Pavyzdys:

# def list_sum(list1:list, list2:list) ->bool:
#     if len(list1) !=len(list2):
#         return False
    
#     first_sum = list1[0] + list2[0]

#     for i in range(1, len(list1)):
#         if list1[i] + list2[i] != first_sum:
#             return False
        
#     return True

# list1 = [5,2,3]
# list2 = [1,4,3]

# result = list_sum (list1, list2)
# print(result)

# Create a function that takes a list of integers, sums the even and odd numbers
# separately, then returns the difference between the sums of the even and odd numbers.

# Sukurkite funkciją, kuri paimtų sveikųjų skaičių sąrašą, atskirai suskaičiuotų lyginių ir nelyginių skaičių sumas, 
# tada grąžintų lyginių ir nelyginių skaičių sumų skirtumą skaičių.

# def even_and_odd_numbers_sum(list1):
#     even_sum = 0
#     odd_sum = 0

#     for num in list1:
#         if num % 2 == 0:
#             even_sum += num
#         else:
#             odd_sum += num

#     return even_sum - odd_sum


# list1 = [4,5,8,2,7,6,9]
# result = even_and_odd_numbers_sum(list1)
# print(result)


# from typing import List


# number_list =[1,2,3,4,5]
# def number_war(number_list:List[int])-> int:
#     even = [numb for numb in number_list if numb % 2 == 0]
#     odd = [numb for numb in number_list if numb % 2 != 0]
#     return sum(even) - sum(odd) if sum(even) > sum(odd) else sum(odd) - sum(even)
# print(number_war(number_list))
# # 3prat.
# You are given an input array of bigrams, and an array of words.
# Write a function that returns True if every single bigram from this array can be found at least once in an array of words.

# Jums duotas bigramų masyvas ir žodžių masyvas. Parašykite funkciją, kuri grąžintų True, jei iš šio masyvo
# galima rasti kiekvieną bigramą bent vieną kartą žodžių masyve.


# from typing import List
# def can_find(bi_list: List[str], words_list: List[str]) -> bool:
#       check_list: list = [bi for bi in bi_list if any(bi in word for word in words_list)]    
#       if check_list == bi_list:        
#         return True    
#       return False  

# print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))
# print(can_find(["ay", "be", "ta", "cu"], ["maybe", "beta", "abet", "course"]))
# print(can_find(["th", "fo", "ma", "or"], ["the", "many", "for", "forest"]))
# print(can_find(["oo", "mi", "ki", "la"], ["milk", "chocolate", "cooks"]))

# 4.3# can_find = lambda bi_list, words_list: 
# True if bi_list == [x for x in bi_list if any(x in bi for bi in words_list)] else False


from typing import List


def find_sum(number_list: List[int]) -> int:
    return sum(number_list)
numbers_input = input("Please enter 5 random numbers: ")
number_list = [int(number) for number in numbers_input.split(",")]
num_sum = sum (number_list)

print ("sum of numbers: ", num_sum)


