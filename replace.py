def anti_vowel(text):
    for char in text:
        if char in 'AEIOUaeiou':
            text = text.replace(char,'')
    return text
print anti_vowel('cars')

def censor(text, word):
    lst = text.split()
    for s in lst:
        if s == word:
            lst[lst.index(s)] = "*" * len(word)
    return " ".join(lst)