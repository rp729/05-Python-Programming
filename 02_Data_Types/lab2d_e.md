|[Table of Contents](/00-Table-of-Contents.md)|
|---|

---

## Lab 2D & Lab2E

**Lab 2D: Strings**

**Instructions:**

Write a program that reverses a user inputted string then outputs the new string, in all uppercase letters.

**Bonus:** Add additional functionality, experiment with other string methods.

```
print(''.join(reversed(input('Enter some words.'))).upper())

########################################

user_input = input("Enter some characters:")

reverse_string = user_input[::-1]

upper_string = reverse_string.upper()

print(upper_string)

```

## Lab 2E: Count Words

**Instructions:**

Write a program that takes a string as user input then counts the number of words in that sentence.

**Bonus:** Add additional functionality, experiment with other string methods.

ex: Output number of characters, number of uppercase letters, etc...

```
user_input = input("Enter a sentence.")

input_list = user_input.split(" ")

word_count = len(input_list)

print(word_count)
```
---

|[Next Topic](/02_Data_Types/04_lists.md)|
|---|
