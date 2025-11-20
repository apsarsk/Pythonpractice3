s1='state'
s2="taste"
s1=s1.lower()
s2=s2.lower()
for x in s1:
    if x.isalpha():
        if s1.count(x) != s2.count(x):
            print('not anagram')
            break
        else:
            print('anagram')