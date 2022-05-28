# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True


def find_anagram(str1, str2):
    # [assignment] Add your code here
    if(sorted(str1) == sorted(str2)):
        print("True")
    else:
        print("False")
str1 = "listen"
str2 = "silent"
find_anagram(str1, str2)

    
    #return True

