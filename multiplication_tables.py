#Write a program that will print the times table for the
#value given by mystery_int. The times table should print a
#two-column table of the products of every combination of
#two numbers from 1 through mystery_int. Separate consecutive
#numbers with either spaces or tabs, whichever you prefer.
#
#For example, if mystery_int is 5, this could print:
#
#1	2	3	4	5
#2	4	6	8	10
#3	6	9	12	15
#4	8	12	16	20
#5	10	15	20	25

mystery_int = 3

for x in range(1, mystery_int + 1):
    for y in range(1, mystery_int + 1):
        print(x * y, end = '\t')
    print('')

#For example, if the string was "Lucy", then the output would
#be:
#
#L
#Lu
#Luc
#Lucy

mystery_string = "Lucy"

for string in range(0, len(mystery_string)):
    print(string)