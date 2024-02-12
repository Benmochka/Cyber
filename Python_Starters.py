import math
def prime_numbers(num):
    if num == 1:
        return True
    else:
        for i in range(2,math.sqrt(num)):
            if num%i == 0:
                return False
            i+=1
    return True

def return_inversed(word):
    word = word[::-1]
    return word

def is_palindrome(word):
    for i in range(len(word)/2):
        if word[i] != word[-i]:
            return False
    return True

def longest_word(sentence):
    sentence.split()
    word = sentence[0]
    for i in range(1,len(sentence)):
        if sentence[i] > word:
            word = sentence[i]
    return word
