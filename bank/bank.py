answer = input("Greeting: ")

new_answer = answer.lower().strip()

print("$0" if "hello" in new_answer else "$100" if 'h' == new_answer[0] else "$20" )