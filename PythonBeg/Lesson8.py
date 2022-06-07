# Створити метод, який принімає строку і сивол, та вивести на екран, скільки разів цей символ повторюється в цій строчці
sentence = str(input("Please enter your text: "))
symb_count = str(input("Please enter symbol that need to be counted: "))
cnt = 0
for counter in sentence:
    if counter == symb_count:
        cnt += 1
print(cnt)
