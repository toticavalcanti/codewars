def is_isogram(string):
    if sorted(string.lower()) == sorted(''.join(set(string.lower()))):
        return True
    return False

print(is_isogram("Ad"))