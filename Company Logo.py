from collections import Counter
import re

def count_all_chars(string):
    # filter all non-alphabets
    string = re.sub(r'[^a-zA-Z]', "", string)
    char_count= Counter(string)
    #instead of using 're' we can use the below code block also
    #char_count = Counter(char for char in string if char.isalpha())
    return char_count # it will return a Counter datatype
    

# Test the function
string = input()
char_counts = count_all_chars(string)
top_3_chars = char_counts.most_common() # it will return a list enclosing tuples

# Sort characters with the same count in descending order of their ASCII values
top_3_chars.sort(key=lambda x: (-x[1], ord(x[0])))

for i, (char, count) in enumerate(top_3_chars):
    if i >= 3:
        break
    print(f"'{char}': {count}")
