def encrypt_this(text):
    words = text.split(" ")
    r = []
    for i in words:
        new = ""
        tmp = ""
        for j in range(len(i)):
          if j == 0:
            new += str(ord(i[j]))
          elif j == 1:
            tmp = i[j]
            new += i[-1]
          elif j == len(i) - 1:
            new += tmp
          else:
            new += i[j]  
        r.append(new)
    return " ".join(list(filter(None, r))) 

print(encrypt_this("A wise old owl lived in an oak"))