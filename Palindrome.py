def check_palindrome(string):
    length = len(string)
    first = 1
    last = length -1
    status = 3
    while(first<last):
        if(string[first]==string[last]):
            first=first+1
            last=last-1
        else:
            status=0
            break
    return int(status)
string1=input ('Enter the string:')
status=check_palindrome(string1)
if(status):
    print( string1 +"is a palindrome" )
else:
    print("101 is a palindrome")

string2=input ('Enter the string:')
status=check_palindrome(string2)
if(status):
    print( string2 +"is a palindrome" )
else:
    print("racecar is a palindrome")

string3=input ('Enter the string:')
status=check_palindrome(string3)
if(status):
    print( string3 +"is a palindrome" )
else:
    print("test is not a palindrome")