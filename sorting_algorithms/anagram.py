def anagram(word1, word2):
    count = 0
    for i in word1:
        for j in word2:
            if i == j:
                count += 1
    try:
        if count == len(word1):
            print("the entered word is  anagram")
    except Exception as e:
        print("the entered word not match please check entered word", e)


if __name__ == '__main__':
    string1 = input("enter the first word")
    string2 = input("enter the second string")
    anagram(string1, string2)
