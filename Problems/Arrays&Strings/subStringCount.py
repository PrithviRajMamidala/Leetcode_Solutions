def stingOccurs(string1, string2):
    if string2 in string1:
        count = string1.count(string2)
        print(count)




if __name__ == '__main__':
    string1 = "rrotparrotpaparrot"
    string2 = "parrot"
    print(stingOccurs(string1, string2))