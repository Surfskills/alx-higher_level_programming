0-read_file.py
A function that reads a text file (UTF8) and prints it to stdout:

    Prototype: def read_file(filename=""):
    You must use the with statement
    
1-write_file.py
A function that writes a string to a text file (UTF8) and returns the number of characters written:

    Prototype: def write_file(filename="", text=""):
    You must use the with statement
    
2-append_write.py
A function that appends a string at the end of a text file (UTF8) and returns the number of characters added:

    Prototype: def append_write(filename="", text=""):
    If the file doesn’t exist, it should be created
    You must use the with statement
        
3-to_json_string.py
A function that returns the JSON representation of an object (string):

    Prototype: def to_json_string(my_obj):

4-from_json_string.py
A function that returns an object (Python data structure) represented by a JSON string:

    Prototype: def from_json_string(my_str):
    
5-save_to_json_file.py
A function that writes an Object to a text file, using a JSON representation:

    Prototype: def save_to_json_file(my_obj, filename):
    You must use the with statement

6-load_from_json_file.py
A function that creates an Object from a “JSON file”:

    Prototype: def load_from_json_file(filename):
    You must use the with statement
    
7-add_item.py
A script that adds all arguments to a Python list, and then save them to a file:

    You must use your function save_to_json_file from 5-save_to_json_file.py
    You must use your function load_from_json_file from 6-load_from_json_file.py
    The list must be saved as a JSON representation in a file named add_item.json

8-class_to_json.py
A function that returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:

    Prototype: def class_to_json(obj):
    obj is an instance of a Class
    All attributes of the obj Class are serializable: list, dictionary, string, integer and boolean
    
9-student.py
A class Student that defines a student by:

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py)
    
10-student.py
A class Student that defines a student by: (based on 9-student.py)

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
        If attrs is a list of strings, only attribute names contained in this list must be retrieved.
        Otherwise, all attributes must be retrieved

11-student.py
A class Student that defines a student by: (based on 10-student.py)

    Public instance attributes:
        first_name
        last_name
        age
    Instantiation with first_name, last_name and age: def __init__(self, first_name, last_name, age):
    Public method def to_json(self, attrs=None): that retrieves a dictionary representation of a Student instance (same as 8-class_to_json.py):
        If attrs is a list of strings, only attributes name contain in this list must be retrieved.
        Otherwise, all attributes must be retrieved
    Public method def reload_from_json(self, json): that replaces all attributes of the Student instance:
        You can assume json will always be a dictionary
        A dictionary key will be the public attribute name
        A dictionary value will be the value of the public attribute
    You are not allowed to import any module
    
12-pascal_triangle.py
A Function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:

    Returns an empty list if n <= 0
    You can assume n will be always an integer
    You are not allowed to import any module
    

100-append_after.py
A Function that inserts a line of text to a file, after each line containing a specific string (see example):

    Prototype: def append_after(filename="", search_string="", new_string=""):
    You must use the with statement
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    









































































































    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
