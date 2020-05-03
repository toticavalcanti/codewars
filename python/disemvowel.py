def disemvowel(string):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    return ''.join([l for l in string if l not in vowels])

print(disemvowel("This website is for losers LOL!"))
                              