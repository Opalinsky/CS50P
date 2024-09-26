def Main():
    str = input()
    ConvertedStr = Convert(str)
    print(ConvertedStr)

def Convert(str):
    if ":)" in str:
        str = str.replace(":)",'🙂',)
    if ":(" in str:
        str = str.replace(":(",'🙁',)
    return str

Main()
