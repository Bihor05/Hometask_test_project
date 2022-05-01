word = str(input("Enter your word: "))
pal = word[::-1]
if pal == word:
    print(f"Word {word} = {pal}. It's palyndrome!")
else:
    print("Try another word!")