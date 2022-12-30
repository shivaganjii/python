#create basic scenraios for python projects with answers.



###Write a program to input a number from the user and print its square. (tavane 2)

# num = int(input("Enter a number: "))
# print("The square of the number is", num**2)

#################################################################################

###Write a program to input two numbers from the user and print their sum. (jamee +)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print("The sum of the numbers is", num1 + num2)

#################################################################################

###Write a program to input a string from the user and print it in uppercase. (kalame kapital)

# string = input("Enter a string: ")
# print(string.upper())

#################################################################################

###Write a program to input a string from the user and print the number of characters in it. (tolle kalame)

# # string = input("Enter a string: ")
# print("The number of characters in the string is", len(string))

#################################################################################

###Write a program to input a list of numbers from the user and print the sum of all the numbers. (jam zadane list)

# numbers = input("Enter a list of numbers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# print("The sum of the numbers is", sum(numbers))

#################################################################################

###Write a program to input a list of strings from the user and print the longest string. (tolani tarin kalame)

# strings = input("Enter a list of strings separated by space: ").split()
# longest_string = max(strings, key=len)
# print("The longest string is", longest_string)

#################################################################################

###Write a program to input a string from the user and print the first and last characters. (avali o akharin harfe kalame)

# string = input("Enter a string: ")
# print("The first character is", string[0])
# print("The last character is", string[-1])

#################################################################################

###Write a program to input a string from the user and check if it is a palindrome "a word or phrase that reads the same backward as forward". (palindrome bodan "dad" / aval o akhar yeki)

# string = input("Enter a string: ")
# if string == string[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

#################################################################################

###Write a program to input a list of strings from the user and check if any of them are palindromes. (kalame aval o akhare list yeki bashe ya nabashe)

# strings = input("Enter a list of strings separated by space: ").split()
# palindromes = [x for x in strings if x == x[::-1]]
# if palindromes:
#     print("The following strings are palindromes:", palindromes)
# else:
#     print("There are no palindromes in the list.")

#################################################################################

###Write a program to input a list of integers from the user and print the maximum and minimum values. (max o min az listi ke behesh dadi)

# numbers = input("Enter a list of integers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# print("The maximum value is", max(numbers))
# print("The minimum value is", min(numbers))

#################################################################################

###Write a program to input a string from the user and count the number of vowels in it. (az horofe "aeiouAEIOU" chandta dashte bashe)

# string = input("Enter a string: ")
# vowels = "aeiouAEIOU"
# count = 0
# for character in string:
#      if character in vowels:
#        count += 1
# print("The number of vowels in the string is", count)

#################################################################################

###Write a program to input a string from the user and replace all spaces with underscores. (jaye " " ro "_" bezar)

# string = input("Enter a string: ")
# print(string.replace(" ", "_"))

#################################################################################

###Write a program to input a list of integers from the user and print only the even numbers. (adade zoj ro joda mikone)

# numbers = input("Enter a list of integers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# evens = [x for x in numbers if x % 2 == 0]
# print("The even numbers are", evens)

#################################################################################

###Write a program to input a list of strings from the user and print only the ones that start with a vowel. (kalamati ke "aeiouAEIOU" ro daran list mishe)

# strings = input("Enter a list of strings separated by space: ").split()
# vowels = "aeiouAEIOU"
# starts_with_vowel = [x for x in strings if x[0] in vowels]
# print("The strings that start with a vowel are", starts_with_vowel)

#################################################################################

###Write a program to input a string from the user and check if it is a palindrome ignoring spaces and case. (harfe aval o akhar yeki bashe)

# string = input("Enter a string: ")
# string = string.lower().replace(" ", "")
# if string == string[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

#################################################################################

###Write a program to input a list of integers from the user and print the average value. (moadel giri)

# numbers = input("Enter a list of integers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# average = sum(numbers) / len(numbers)
# print("The average value is", average)

#################################################################################

###Write a program to input two strings from the user and check if they are anagrams "contain the same characters in a different order". (tole 2 string yeki bashe)

# string1 = input("Enter the first string: ")
# string2 = input("Enter the second string: ")
# if sorted(string1) == sorted(string2):
#     print("The strings are anagrams.")
# else:
#     print("The strings are not anagrams.")

#################################################################################

###Write a program to input a list of strings from the user and print the ones that contain the letter 'a'. (kalamati tu list ke "a" daran)

# strings = input("Enter a list of strings separated by space: ").split()
# contains_a = [x for x in strings if 'a' in x]
# print("The strings that contain the letter 'a' are", contains_a)

#################################################################################

###Write a program to input a list of integers from the user and print the ones that are divisible by 3. (bakhsh pazir bar 3)

# numbers = input("Enter a list of integers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# divisible_by_3 = [x for x in numbers if x % 3 == 0]
# print("The numbers that are divisible by 3 are", divisible_by_3)

#################################################################################

###Write a program to input a string from the user and check if it is a palindrome ignoring punctuation and spaces.!!!!

# import string
# string = input("Enter a string: ")
# string = ''.join(c for c in string if c not in string.punctuation)
# string = string.replace(" ", "")
# string = string.lower()
# if string == string[::-1]:
#     print("The string is a palindrome.")
# else:
#     print("The string is not a palindrome.")

#################################################################################

###Write a program to input a list of strings from the user and sort them in alphabetical order. (moratab bar asas "alfabet")

# strings = input("Enter a list of strings separated by space: ").split()
# strings.sort()
# print("The strings sorted in alphabetical order are", strings)

#################################################################################

###Write a program to input a list of integers from the user and sort them in ascending order. (moratab az kochak be bozorg)

# numbers = input("Enter a list of integers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# numbers.sort()
# print("The numbers sorted in ascending order are", numbers)

#################################################################################

###Write a program to input a list of integers from the user and sort them in descending order. (moratab az bozorg be kochak)

# numbers = input("Enter a list of integers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# numbers.sort(reverse=True)
# print("The numbers sorted in descending order are", numbers)

#################################################################################

###Write a program to input a list of strings from the user and print the ones that are palindromes. (bar ax kalamei mani dashte bashad "mesle madam dad ....")

# strings = input("Enter a list of strings separated by space: ").split()
# palindromes = [x for x in strings if x == x[::-1]]
# if palindromes:
#     print("The palindrome strings are", palindromes)
# else:
#     print("There are no palindrome strings in the list.")

#################################################################################

###Write a program to input a list of strings from the user and print the ones that are palindromes ignoring spaces and case. (kalamati ke bar ax mani dashte bashand)

# strings = input("Enter a list of strings separated by space: ").split()
# palindromes = [x for x in strings if x.lower() == x[::-1].lower()]
# if palindromes:
#     print("The palindrome strings are", palindromes)
# else:
#     print("There are no palindrome strings in the list.")

#################################################################################

###Write a program to input a list of strings from the user and print the ones that are palindromes ignoring spaces. (bar axe kalame mani dashte bashe)

# strings = input("Enter a list of strings separated by space: ").split()
# palindromes = [x for x in strings if x.replace(" ", "") ==
# x [::-1].replace(" ", "")]
# if palindromes:
#     print("The palindrome strings are", palindromes)
# else:
#     print("There are no palindrome strings in the list.")

#################################################################################

###Write a program to input a list of integers from the user and print the ones that are odd. (adade fard toye list ru print mikone)

# numbers = input("Enter a list of integers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# odds = [x for x in numbers if x % 2 == 1]
# print("The odd numbers are", odds)

#################################################################################

###Write a program to input a list of integers from the user and check if any of them are prime numbers using a function. (adade AVAL touye list ru peyda o print)

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#         return True
# numbers = input("Enter a list of integers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# primes = [x for x in numbers if is_prime(x)]
# if primes:
#     print("The prime numbers are", primes)
# else:
#     print("There are no prime numbers in the list.")

#################################################################################

###Write a program to input a list of strings from the user and print the ones that contain the letter 'e'. (kalamati ke "e" daran)

# strings = input("Enter a list of strings separated by space: ").split()
# contains_e = [x for x in strings if 'e' in x]
# print("The strings that contain the letter 'e' are", contains_e)

#################################################################################

###Write a program to input a list of integers from the user and check if any of them are even numbers using a function. (adade zoj)

# def is_even(n):
#     return n % 2 == 0
# numbers = input("Enter a list of integers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# evens = [x for x in numbers if is_even(x)]
# if evens:
#     print("The even numbers are", evens)
# else:
#     print("There are no even numbers in the list.")

#################################################################################

###Write a program to input a list of integers from the user and print the ones that are divisible by 5. (bakhshPazir bar 5)

# numbers = input("Enter a list of integers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# divisible_by_5 = [x for x in numbers if x % 5 == 0]
# print("The numbers that are divisible by 5 are", divisible_by_5)

#################################################################################

###Write a program to input a list of strings from the user and print the ones that start with a consonant. (kalamati ke ba in liste horof shoro beshan "masalan a nadare o allways ro print nemikone")

# strings = input("Enter a list of strings separated by space: ").split()
# consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
# starts_with_consonant = [x for x in strings if x[0] in consonants]
# print("The strings that start with a consonant are", starts_with_consonant)

#################################################################################

###Write a program to input a list of integers from the user and check if any of them are odd numbers using a function. (adade fard ro joda kone)

# def is_odd(n): return n % 2 == 1
# numbers = input("Enter a list of integers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# odds = [x for x in numbers if is_odd(x)]
# if odds:
#     print("The odd numbers are", odds)
# else:
#     print("There are no odd numbers in the list.")

#################################################################################

###Write a program to input a list of strings from the user and print the ones that contain the letter 'i'. (kalamati ke "i" dashte bashan)

# strings = input("Enter a list of strings separated by space: ").split()
# contains_i = [x for x in strings if 'i' in x]
# print("The strings that contain the letter 'i' are", contains_i)


#################################################################################

###Write a program to input a list of integers from the user and print the ones that are divisible by 7. (bakhshPazir bar 7)

# numbers = input("Enter a list of integers separated by space: ").split()
# numbers = [int(x) for x in numbers]
# divisible_by_7 = [x for x in numbers if x % 7 == 0]
# print("The numbers that are divisible by 7 are", divisible_by_7)

#################################################################################

