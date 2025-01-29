def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"


def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number>10:
        return "Greater"
    if number < 10:
        return "Lesser"
    if number == 10:
        return "Equal"


def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    sum = 0
    for i in range(n+1):
       sum += i
    return sum



def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    sum_of_elements =  sum(numbers);
    
    maximum_element = max(numbers)
    
    minimum_element = min(numbers)
    return(sum_of_elements,maximum_element,minimum_element)



def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    students_above80 = [name for name, score in students_dict.items() if score>80]
    return students_above80

def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    common_elements = set(list1) & set(list2)
    return common_elements

def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    sum = a+b
    difference = a-b
    product = a*b
    if b == 0:
        quotient = "undefined"
    else:
        quotient = a/b
   
    return {"sum":sum,
            "difference":difference,
            "product":product,
            "quotient":quotient}

def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    And  = x and y
    Or = x or y
    Not_x = not x
   
    return {"and":And,
            "or":Or,
            "not_x":Not_x
            }

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    bitwise_and = a & b
    bitwise_or = a|b
    bitwise_xor = a^b
    return {"and" : bitwise_and,
            "or":bitwise_or,
            "xor":bitwise_xor} 