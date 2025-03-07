def is_palindrome(word):
    return word == word[::-1]
def find_palindrome(word):
    return [i for i in word if is_palindrome(i)]

words = ['madam', 'hello', 'world', 'level', 'python', 'radar', 'mom']

palindromes = find_palindrome(words)

print(palindromes)
