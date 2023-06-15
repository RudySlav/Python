## CORRECT SOLUTION SAMPLE
## SCORE = 28 MARKS OUT OF 28 MARKS
# Hashtag and not starting with m function
def hash_m_finder(user_list):
    correct_words = []
    for word in user_list:
        if '#' in word and not word.startswith('m'):
            correct_words.append(word)
    return correct_words

# Common Character Check Function
def common_characters(user_list):
    common_letters = []
    for char in set(user_list[0]):
        if char not in common_letters:
           if all(char in string for string in user_list[1:]):
               common_letters.append(char)
    return common_letters

# User List
user_list = []

# Loop to get User Input for List
while True:
    user_input = input("Enter a word to add to the list. Write the word end to stop. -> ")
    if user_input == "end":
        break
    user_list.append(user_input)

# Function running test on m and # and printing out information if present
answear = hash_m_finder(user_list)
if len(answear) >= 1:
    print("Hash marks and no m check:")
    for i in range(len(answear)):
        print(str(answear[i]) + " hash mark is present and does not start with m")

# Function running comon character check and printing out information in order
list = common_characters(user_list)
if list:
    for char in list:
        words_with_character = []
        character_amount = []
        for i in range(len(user_list)):
            check = user_list[i]
            if char in check:
                words_with_character.append(check)
                character_amount.append(check.count(char))
        print(f"The character {char} is common in all these words:")
        for i in range(len(words_with_character)):
            word = words_with_character[i]
            amount = character_amount[i]
            print(f"{word} containes {char} {amount} amount of times")


