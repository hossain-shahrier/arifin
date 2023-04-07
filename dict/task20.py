sentence = input("Enter a sentence: ")
# The secret of getting ahead is getting started.
# I love Programming. Python is love.

special_chars = input("Enter a list of special characters separated by commas: ").split(',')
# -,=,+,*,%
# @,$,&,#
words = sentence.replace('.', '').split()
print(words)
print(len(special_chars))
word_dict = {}

for word in words:
    index = sum(ord(c) for c in word) % len(special_chars)
    print(index)
    if special_chars[index] not in word_dict:
        word_dict[special_chars[index]] = [word]
    elif word not in word_dict[special_chars[index]]:
        word_dict[special_chars[index]].append(word)

print("Words in the given String:", words)
print("Answer:", word_dict)
