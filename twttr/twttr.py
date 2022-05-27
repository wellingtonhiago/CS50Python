answer = input("Input: ")
print("Output: ", end="")

new_answer = [letter for letter in answer if letter.lower() not in "aeiou"]
print(''.join(new_answer))