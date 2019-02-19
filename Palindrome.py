#not as function
# list=input('enter a string to test for palindrome: ')
# list=list.replace(" ", "").replace(".", "").replace(",", "").replace("-", "").replace("!", "")
# list=list.lower()
# if (list==list[::-1]):
#     print ("It is a palindrome")
# else:
#    print("it is not palindrome")

   #function
import re 
def palindrome(pal):
    #pal=input('enter palindrome here: ')
    pal=re.sub(r'[^A-Za-z]', '', pal.lower())
    print(pal)
    if pal==pal[::-1]:
        print('this is a palindrome')
    else:
        print('this is not a palindrome')
palindrome(input('Type something in there: '))