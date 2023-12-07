# Variable annotations
This directory contains a collection of Python scripts focused on variable annotations and type hints. Each script within this directory addresses specific aspects of type annotations, covering basic annotation concepts, complex types, and practical use cases. The scripts aim to enhance code readability, maintainability, and reliability by incorporating type information into variable declarations and function signatures.  

The scripts are organized based on different annotation scenarios, such as basic arithmetic operations (add, concat, floor), string representation of floats (to_str), defining variables with specific values (define_variables), handling lists of floats (sum_list), and more. The directory serves as a learning resource for developers seeking to understand and implement variable annotations in Python for better code quality.  

## Example
```
#!/usr/bin/env python3
'''
Simple script with an 'add' function to perform addition of two numbers.
'''


def add(a: float, b: float) -> float:
    '''
    Adds two numbers and returns the result.
    '''
    return a + b
```

## Sample usage
```
└─$ cat 0-main.py 
#!/usr/bin/env python3
add = __import__('0-add').add

print(add(1.11, 2.22) == 1.11 + 2.22)
print(add.__annotations__) 

└─$ ./0-main.py
True
{'a': <class 'float'>, 'b': <class 'float'>, 'return': <class 'float'>}
```