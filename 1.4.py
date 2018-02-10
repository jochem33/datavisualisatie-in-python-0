def Palindrome (S):
    for i in range(len(S)):
        hoi = i + 1
        if S[i] != S[hoi]:
            print("het is geen palindrome")
            break

Palindrome("lepel")
