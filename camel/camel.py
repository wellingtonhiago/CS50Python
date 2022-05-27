camelCase = input("camelCase: ")

print("snake_case: ", end="")

for letter in camelCase:
    if letter.isupper():
        camelCase = camelCase.replace(letter, "_" + letter.lower())
        snake_case = camelCase
print(snake_case)
