def count_char(text, char):
    count = 0
    for c in text.upper():
        if c == char:
            count += 1
    return count


def count_charforuserinput(userinput, character):
    count = 0
    for c in userinput.upper():
        if c == character:
            count += 1
    return count


filename = "491words.txt"
with open(filename) as f:
    text = f.read()

for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
    textanalyzer = count_char(text, char)
    print("| {0} => {1}".format(char, textanalyzer), end=" ",)

userinput = input("\nEnter some text here:")
for character in "ABCDEFGHIJKLMNOPQRSTUVWXY":
    textanalyzerforuserinput = count_charforuserinput(userinput, character)
    print("| {0} => {1}".format(character, textanalyzerforuserinput), end=" ")
