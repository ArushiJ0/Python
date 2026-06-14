def Palindrome(text):
    text =text.lower().replace(" " ,"")
    return text ==text[::-1]

print(Palindrome('Madam'))

        
