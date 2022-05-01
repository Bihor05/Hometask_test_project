# Створити метод, який принімає строку і сивол, та вивести на екран, скільки разів цей символ повторюється в цій строчці

sentence = str(input("Please enter your text: "))
symb_count = str(input("Please enter symbol that need to be counted: "))
print("Result:" + str(sentence.count(symb_count)))
