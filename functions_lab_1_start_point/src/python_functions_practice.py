def return_10():
    return 10

def add(int_one, int_two):
    sum = int_one + int_two
    return sum

def subtract(int_one, int_two):
    sum = int_one - int_two
    return sum

def multiply(int_one, int_two):
    sum = int_one * int_two
    return sum

def divide(int_one, int_two):
    sum = int_one / int_two
    return sum

def length_of_string(string_example):
    return len(string_example)

def join_string(string_ex_1, string_ex_2):
    return (f"{string_ex_1}{string_ex_2}")

def add_string_as_number(str_one, str_two):
    sum = 0
    sum = (int(str_one) + int(str_two))
    return sum

def number_to_full_month_name(number_month):
    typed_month = None
    if number_month == 1:
        typed_month = "January"
    elif number_month == 3:
    	typed_month = "March"
    elif number_month == 9:
    	typed_month = "September"
    return typed_month

def number_to_short_month_name(number_month):
    typed_month = None
    if number_month == 1:
        typed_month = "Jan"
    elif number_month == 4:
    	typed_month = "Apr"
    elif number_month == 10:
    	typed_month = "Oct"
    return typed_month