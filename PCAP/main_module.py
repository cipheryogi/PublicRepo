# this is how we call the own modules into the main module (called and calling program concept). Note that the called program (lists_utils) is coded in a way to verify that the defined fuctions work fine when the lists_utils is executed independently. The program checks whether its being run independently or being called (imported) by using __name__ == '__main__'. 

import lists_utils

user_list = [10,20,30,40]

# this is how to use the functions defined in the called program

print(lists_utils.sum_elements(user_list)) 

print(lists_utils.double_each_element(user_list))

print(lists_utils.get_usage_counter())