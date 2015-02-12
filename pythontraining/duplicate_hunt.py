__author__ = 'talluri'

numbers = [56,75,46,97,75,46,46,22,34,44,44,45,44]

def duplicates(number_list):
    num_dict = {}
    for num in number_list:
        # if num in num_dict.keys(): # less efficient
        if num in num_dict:
            num_dict[num] = num_dict[num]+1
        else:
            num_dict[num] = 1
    for dup in num_dict:
        if num_dict[dup] > 1:
            print dup,":",num_dict[dup]

duplicates(numbers)


