def subs(str1,str2):
    if str2 in str1:
        print(str1.index(str2))
    else:
        return False

print(subs("sanandverma","ana"))