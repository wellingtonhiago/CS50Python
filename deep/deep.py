answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

print("Yes" if answer.strip() == "42"
            or answer.lower().strip() == "forty-two"
            or answer.lower().strip() == "forty two"
            else "No")