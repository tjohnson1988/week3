#For example, if the string was "Lucy", then the output would
#be:
#
#L
#Lu
#Luc
#Lucy

mystery_string = "Lucys"
count = 0

for i in range(1, len(mystery_string) + 1):
    for letter in mystery_string:
        print(letter)
    
   