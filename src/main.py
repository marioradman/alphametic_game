# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import csv
import random
import sys
import traceback
import uuid
import json

PATH_TO_RES = 'res/'
PATH_TO_DATA = 'data/'
# FILENAME = 'test.csv'
FILENAME_DICTIONARY = 'wordlist_maxlength_9.csv'
FILENAME_QUIZ = 'quiz.txt'
FILENAME_ANSWERS = 'answers.txt'
WORD_LENGTH_MIN = 3
WORD_LENGTH_MAX = 8

# WORD SELECTIONS - Words with how many characters minimum or maximum
W_3_MIN = 2
W_3_MAX = 3
W_4_MIN = 3
W_4_MAX = 5
W_5_MIN = 6
W_5_MAX = 8
W_6_MIN = 4
W_6_MAX = 6
W_7_MIN = 1
W_7_MAX = 3
W_8_MIN = 0
W_8_MAX = 1

# RANDOM WORDS
RANDOM_WORDS_LENGTH_MIN = 3
RANDOM_WORDS_LENGTH_MAX = 5

# ADDED IN MAIN
DICTIONARIES_COUNT = {}

# VALUE SELECTIONS
# including next higher number: 0-1ß, 11-20, 21-30, etc.
# V_0_MIN = 2
# V_0_MAX = 3
# V_1_MIN = 0
# V_1_MAX = 2
# V_2_MIN = 0
# V_2_MAX = 2
# V_3_MIN = 5
# V_3_MAX = 7
# V_4_MIN = 1
# V_4_MAX = 3
# V_5_MIN = 4
# V_5_MAX = 6
# V_6_MIN = 3
# V_6_MAX = 5
# V_7_MIN = 0
# V_7_MAX = 1
V_0_MIN = 0
V_0_MAX = 10
V_1_MIN = 2
V_1_MAX = 10
V_2_MIN = 1
V_2_MAX = 10
V_3_MIN = 4
V_3_MAX = 8
V_4_MIN = 0
V_4_MAX = 4
V_5_MIN = 3
V_5_MAX = 7
V_6_MIN = 2
V_6_MAX = 6
V_7_MIN = 0
V_7_MAX = 2

def create_word_selection_min_max_dict() -> {int: []}:
    dict = {}
    dict[3] = [W_3_MIN, W_3_MAX]
    dict[4] = [W_4_MIN, W_4_MAX]
    dict[5] = [W_5_MIN, W_5_MAX]
    dict[6] = [W_6_MIN, W_6_MAX]
    dict[7] = [W_7_MIN, W_7_MAX]
    dict[8] = [W_8_MIN, W_8_MAX]
    return dict


def get_dictionary_from_csv(filename: str) -> {int: []}:
    filepath = PATH_TO_RES + filename
    all_dictionaries = create_blank_dictionaries()

    with open(filepath, 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            entry = row.pop().split(';')
            push_entry_into_dictionary(all_dictionaries, entry)

    return all_dictionaries


def count_dictionaries(dictionaries: {int: []}):
    for key, dict in dictionaries.items():
        DICTIONARIES_COUNT[key] = len(dict)


def create_blank_dictionaries() -> {}:
    dictionaries = {}
    for i in range(WORD_LENGTH_MIN, WORD_LENGTH_MAX + 1):
        dictionaries[i] = []
    return dictionaries


def push_entry_into_dictionary(dictionaries: {int: []}, entry: []):
    # print(str(entry[0]))
    # print(str(entry[1]))
    dictionaries[int(entry.pop(1))].append(entry.pop(0))


def create_wordlist(dictionary, word_selection_min_max):
    word_list = []
    for word_length in range(WORD_LENGTH_MIN, WORD_LENGTH_MAX + 1):
        if DICTIONARIES_COUNT[word_length] == 0:
            continue
        amount = get_amount_of_words(word_length, word_selection_min_max)
        words = get_words_from_dictionary(word_length, amount, dictionary)
        word_list.extend(words)
    return word_list


def get_amount_of_words(word_length: int, word_selection_min_max: {int: []}) -> str:
    min_amount = word_selection_min_max[word_length][0]
    max_amount = word_selection_min_max[word_length][1]
    return random.randint(min_amount, max_amount)


def get_words_from_dictionary(word_length: int, amount: int, dictionary: {int: []}) -> []:
    word_set = set()
    while True:
        if len(word_set) == amount:
            return word_set
        word_index = random.randint(0, DICTIONARIES_COUNT[word_length] - 1)
        word_set.add(dictionary[word_length][word_index])
        # print(str(word_length))
        # print(word_set)


def add_random_words(wordlist: [], dictionary: {int: []}) -> []:
    while len(wordlist) < 20:
        new_word = get_random_word(dictionary)
        if new_word not in wordlist:
            wordlist.append(new_word)


def get_random_word(dictionary: {int: []}) -> str:
    word_length = random.randint(RANDOM_WORDS_LENGTH_MIN, RANDOM_WORDS_LENGTH_MAX)
    word_index = random.randint(0, DICTIONARIES_COUNT[word_length] - 1)
    return dictionary[word_length][word_index]


# def generate_word_list():
#     word_selection_min_max = create_word_selection_min_max_dict()
#     dictionary = get_dictionary_from_csv(FILENAME)
#     count_dictionaries(dictionary)
#     wordlist = create_wordlist(dictionary, word_selection_min_max)
#     if len(wordlist) < 20:
#         add_random_words(wordlist, dictionary)
#     # print(wordlist)
#     return wordlist

def generate_word_list(dictionary, word_selection_min_max):
    wordlist = create_wordlist(dictionary, word_selection_min_max)
    if len(wordlist) < 20:
        add_random_words(wordlist, dictionary)
    # print(wordlist)
    return wordlist


### VALUE GENERATION
def generate_value_list():
    value_list = {}
    letters_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for value in range(1, 27):
        letter_index = random.randint(0, len(letters_list)-1)
        char = letters_list.pop(letter_index)
        value_list[char] = value
    return value_list


def generate_words_with_values_list(wordslist, valuelist):
    list = {}
    for word in wordslist:
        list[word] = calculate_sum(word, valuelist)
    return list


def calculate_sum(word, valuelist):
    try:
        sum = 0
        charlist = list(word)
        for char in charlist:
            sum += valuelist[char.upper()]
        return sum
        # print(word + ': ' + str(sum))
    except Exception as err:
        try:
            exc_info = sys.exc_info()

            # do you usefull stuff here
            # (potentially raising an exception)
            try:
                raise TypeError("Again !?!")
            except:
                pass
            # end of useful stuff
            # print(word)
            # print(valuelist)
            return 100
        finally:
            # Display the *original* exception
            # traceback.print_exception(*exc_info)
            del exc_info


### VALUE TESTING
def create_number_selection_min_max_dict() -> {int: []}:
    dict = {}
    dict[0] = [V_0_MIN, V_0_MAX]
    dict[1] = [V_1_MIN, V_1_MAX]
    dict[2] = [V_2_MIN, V_2_MAX]
    dict[3] = [V_3_MIN, V_3_MAX]
    dict[4] = [V_4_MIN, V_4_MAX]
    dict[5] = [V_5_MIN, V_5_MAX]
    dict[6] = [V_6_MIN, V_6_MAX]
    dict[7] = [V_7_MIN, V_7_MAX]
    return dict


def init_value_range_dict():
    dict = {}
    dict[0] = 0
    dict[1] = 0
    dict[2] = 0
    dict[3] = 0
    dict[4] = 0
    dict[5] = 0
    dict[6] = 0
    dict[7] = 0
    return dict

def count_value_ranges(words_with_values_list):
    dict = init_value_range_dict()
    # print(words_with_values_list)
    for word, value in words_with_values_list.items():
        if value <= 10:
            dict[0] += 1
            continue
        if value <= 20:
            dict[1] += 1
            continue
        if value <= 30:
            dict[2] += 1
            continue
        if value <= 40:
            dict[3] += 1
            continue
        if value <= 50:
            dict[4] += 1
            continue
        if value <= 60:
            dict[5] += 1
            continue
        if value <= 70:
            dict[6] += 1
            continue
        if value <= 80:
            dict[7] += 1
            continue
        if value > 80:
            return None
    return dict


def check_if_value_ranges_are_valid(value_ranges, expected_list):
    try:
        for range, amount in value_ranges.items():
            min = expected_list[range][0]
            max = expected_list[range][1]
            if amount < min or amount > max:
                return False
        return True
    except Exception as err:
        try:
            exc_info = sys.exc_info()

            # do you usefull stuff here
            # (potentially raising an exception)
            try:
                raise TypeError("Again !?!")
            except:
                pass
            # end of useful stuff
            # print(value_ranges)
            # print(expected_list)
            return False

        finally:
            # Display the *original* exception
            # traceback.print_exception(*exc_info)
            del exc_info


def value_testing(number_selection_min_max_dict, words_with_values_list):
    count_of_values_range = count_value_ranges(words_with_values_list)

    if count_of_values_range is None:
        return False

    # print(words_with_values_list)
    # print(count_of_values_range)
    # return True # for testing purposes
    return check_if_value_ranges_are_valid(count_of_values_range, number_selection_min_max_dict)


def save_quiz_and_result(wordlist, valuelist):
    id = random.randint(1000, 9999)
    filepath_quiz = PATH_TO_DATA + FILENAME_QUIZ
    with open(filepath_quiz, 'a') as file:
        file.write(str(id) + ': ')
        file.write(json.dumps(wordlist))
        file.write('\n')

    filepath_answers = PATH_TO_DATA + FILENAME_ANSWERS
    with open(filepath_answers, 'a') as file:
        file.write(str(id))
        file.write(json.dumps(valuelist))
        file.write('\n')


if __name__ == '__main__':
    words_with_values_list = None
    valuelist = None
    values_are_valid = False
    word_selection_min_max = create_word_selection_min_max_dict()
    dictionary = get_dictionary_from_csv(FILENAME_DICTIONARY)
    count_dictionaries(dictionary)
    wordlist = generate_word_list(dictionary, word_selection_min_max)
    repetition_counter = 0
    number_selection_min_max_dict = create_number_selection_min_max_dict()

    for i in range(2):
        while True:
            valuelist = generate_value_list()
            # print(valuelist)
            words_with_values_list = generate_words_with_values_list(wordlist, valuelist)
            values_are_valid = value_testing(number_selection_min_max_dict, words_with_values_list)

            if values_are_valid:
                break

            repetition_counter += 1

            if repetition_counter == 100:
                repetition_counter = 0
                wordlist = generate_word_list(dictionary, word_selection_min_max)

        print(words_with_values_list)
        save_quiz_and_result(words_with_values_list, valuelist)