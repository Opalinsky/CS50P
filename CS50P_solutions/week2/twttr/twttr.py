text = input("Input: ")
text_after = []
for i in range(len(text)):
    if text[i]=="a" or text[i]=="e" or text[i]=="i" or text[i]=="o" or text[i]=="u" or text[i]=="A" or text[i]=="E" or text[i]=="I" or text[i]=="O" or text[i]=="U" :
        continue
    else:
        text_after.append(text[i])

mySeparator = ''
x = mySeparator.join(text_after)
print(x)
