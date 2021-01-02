# Program to right justify the string such that the last character appears on the 70th Column

def right_justify(argument):
    length=len(argument)
    putspace=70-length
    print(putspace*' '+ argument)

a=1
while a:
    print("Enter a string to right justify")
    argument=input()
    right_justify(argument)
    print("Do you want to continue? Enter Yes or No")
    test=input().capitalize()
    if test=="No":
        a=0
