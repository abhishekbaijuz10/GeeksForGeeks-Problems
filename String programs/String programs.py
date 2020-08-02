def check_palindrome(pali):
    for i in range(0, int(len(pali)/2)):
        if pali[i] == pali[len(pali) - i -1]:
            return True
    else:
        return False


palindrome = "malayalam"
ans = check_palindrome(palindrome)
if ans:
    print('Its true')
else:
    print('Its false')


rev = ''.join(reversed('abhishek'))
print(rev)