def check(word):
    buffer = []
    reversedBuffer=[]
    
    for i in word:
        buffer.append(i)
    reversedBuffer = buffer[::-1]

    if reversedBuffer == buffer:
        return True
    else:
        return False
    
print(check("level"))