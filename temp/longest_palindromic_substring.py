#!/usr/bin/env python
"""
Given a string, find the longest substring which is palindrome. For example, if the given string is 'forgeeksskeegfor', the output should be 'geeksskeeg'.
"""


def max_palindrome(s, ini, end):
    """ Returns a tuple with ini and end of max palindrome found from initial (ini, end)"""
    while ini > 0 and end < len(s)-1:
        if s[ini - 1] == s[end + 1]:
            ini -= 1
            end += 1
        else:
            break
    return ini, end


def longest_palindrome(s):
    result = ''
    max_len = 0
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            ini, end = max_palindrome(s, i, i + 1)
            if end - ini > max_len:
                max_len = end - ini
                result = s[ini:end+1]
        if i == 0:
            continue
        if s[i - 1] == s[i + 1]:
            ini, end = max_palindrome(s, i - 1, i + 1)
            if end - ini > max_len:
                max_len = end - ini
                result = s[ini:end+1]
    return result


def test(s):
    print ("Longest palidrome substring of {} is {}".format(
        s, longest_palindrome(s)))


test("forgeeksskeegfor")
test("forgeekskeegfor")
test("forrofabc")
test("abcforrof")
test("abcdefgh")
test("1234567654345678987654321")
