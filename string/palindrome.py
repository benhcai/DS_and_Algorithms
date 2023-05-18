def palindrome(str):
    left = 0
    right = len(str) - 1
    while left < right:
        if str[left] == str[right]:
            left = left + 1
            right = right - 1
        else:
            return False
    return True

print(palindrome(""))
print(palindrome("a"))
print(palindrome("aba"))
print(palindrome("ab"))
print(palindrome("abcdedcba"))
