import random

print('H A N G M A N')
words = ['python', 'java', 'kotlin', 'javascript']
word = random.choice(words)
n = len(word)
user_word = str(n * '-')
i = 1
while i < 9:
    print()
    print(user_word)
    if '-' in user_word:
        if i <= 8:
            letter = input('Input a letter: ')
            if letter in word:
                count_letter = word.count(letter)
                count_letter_user_w = user_word.count(letter)
                if count_letter > count_letter_user_w:
                    if count_letter == 1:
                        letter_index_l = word.find(letter)
                        user_word = user_word[:letter_index_l] + letter + user_word[letter_index_l + 1:]
                        done = True
                    if count_letter == 2:
                        letter_index_l = word.find(letter)
                        letter_index_r = word.find(letter, letter_index_l + 1)
                        user_word = user_word[:letter_index_l] + letter + user_word[letter_index_l + 1: letter_index_r] + letter + user_word[letter_index_r + 1:]
                        done = True
                else:
                    print('No improvements')
                    i += 1
                    if i > 8:
                        print('You lost!')
                        break
            else:
                print("That letter doesn't appear in the word")
                i += 1
                if i > 8:
                    print('You lost!')
                    break
    else:
        print('You guessed the word!')
        print('You survived!')
        break



