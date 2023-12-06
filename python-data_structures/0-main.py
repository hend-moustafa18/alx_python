#!/usr/bin/python3
if __name__ == "__main__":
    no_c = __import__('0-no_c').no_c
word = "School"
new_word = no_c(word)

print(new_word)
print(word)