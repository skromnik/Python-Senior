print('Hello World')

first = 23
second = "Yellow"
print(first,second)


a = 10 + 5
b = a + 30
c = (a+b) * 2

print(a,b,c)


first_string = "Hello World!"
second_string = 'Hello World!'
third_string = "'Hello World'"

name = input("Ваше Ім'я?")

greeting = "Привіт," + name
print(greeting)

text = input("Напишіть любий текст:")
text_lenght = len(text)
print(text_lenght)

result = 10 + 15

text_result = "1) Результат =" + str(result)

print(text_result)

result_2 = "10" + "15"
text_result_2 = "2) Результат = " + result_2

print(text_result_2)

print("1) Hello \n 2) World \n 3)Bye")
choose = input("Choice:")
if int(choose) =="1":
    print("-------> Hello <-------")
elif int(choose) == "2":
    print("-------> World <-------")
elif int(choose) =="3":
    print("-----------> BYE <---------")