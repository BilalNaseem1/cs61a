""" Typing Test implementation """

from utils import *
from ucb import main

# BEGIN Q1-5
"*** YOUR CODE HERE ***"
#q1-p1
def lines_from_file(path=''):
    assert isinstance(path, str) and len(path) > 0
    
    lines = []
    with open(path) as file:
        for line in file:
            lines += [strip(line)]
    return lines

#q1-p2
def new_sample(path, line_nr):
    assert isinstance(path, str) and len(path) > 0

    sample = ''
    
    with open(path) as file:
        for i, line in enumerate(file):
            if i == line_nr:
                sample = strip(line)
                break
    return sample

#q2
def analyze(sample_paragraph, typed_string, start_time, end_time):    
    #returns words typed per minute
    def get_w_p_m(typed_string, start_time, end_time):
        ONE_WORD_LENGTH = 5
        SECONDS_IN_MINUTE = 60
        
        time_typing = end_time - start_time
        #words in string
        words_amount = len(typed_string) / ONE_WORD_LENGTH       
        words_per_minute = SECONDS_IN_MINUTE / time_typing * words_amount
        
        return words_per_minute
    
    #returns the accuracy of typed text
    def get_acc_p(sample_paragraph, typed_string):
        sample_words = split(sample_paragraph)
        amount_sample_words = len(sample_words)
        
        typed_words = split(typed_string)
        amount_typed_words = len(typed_words)
                
        #calculate based on required words. If less then required typed, calculate based on typed amount
        words_amount = amount_sample_words if amount_sample_words <= amount_typed_words else amount_typed_words
        
        def get_nr_of_matches(sample_words, typed_words, words_amount):
            nr_of_matches = 0
            for i in range(0, words_amount):
                    nr_of_matches += int(sample_words[i] == typed_words[i])
            return nr_of_matches
        
        nr_of_matches = get_nr_of_matches(sample_words, typed_words, words_amount)
        
        accuracy = 0.0 if nr_of_matches <= 0 else (nr_of_matches / words_amount) * 100
            
        return accuracy
        
    words_per_minute = get_w_p_m(typed_string, start_time, end_time)
    acc_p = get_acc_p(sample_paragraph, typed_string)
    
    
    return [words_per_minute, acc_p]

#q3
def pig_latin(word):
    VOWELS = 'aeiouAEIOU'
    CNSNANT_SUFFIX = 'ay'
    VOWEL_SUFFIX = 'way'
    
    begins_with_vowel = word[0] in VOWELS
    
    def translate_cnsnant_word(word):
        cnsnant_cluster = ''
        slice_index = 0
        for i in range(0, len(word)):
            if word[i] not in VOWELS:
                cnsnant_cluster += word[i]
                slice_index += 1
            else:
                break
        return word[slice_index:] + cnsnant_cluster + CNSNANT_SUFFIX
    
    return word + VOWEL_SUFFIX if begins_with_vowel else translate_cnsnant_word(word)

#q4
def autocorrect(user_input, words_list, score_function):
    if user_input in words_list:
        return user_input
    
    score_log = {}
    
    for word in words_list:
        score_key = score_function(user_input, word)
        
        if score_key not in score_log:
            score_log[score_key] = word
    
    return score_log[min(score_log)]

#q5
def swap_score(word1, word2):
    if len(word1) <= 0 or len(word2) <= 0:
        return 0
    else:
        return (0 if word1[0] == word2[0] else 1) + swap_score(word1[1:], word2[1:])
        

    
    
# END Q1-5

# Q6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    add_char = lambda word1, char: char + word1
    remove_char = lambda word1: word1[1:]
    substitute_char = lambda word1, char: char + word1[1:]
    
    ### index out of range cases BEGINNING
    #traversed all of word2, word1 is longer, only remove chars
    if len(word2) == 0 and len(word1) > 0:
        return 1 + score_function(remove_char(word1), word2)
    #traversed all of word2
    elif len(word2) == 0:
        return 0
    #only makes sense to add chars to word1
    elif len(word1) == 0:
        return 1 + score_function(add_char(word1, word2[0]), word2)
    ### index out of range cases END
    
    #we found a match, cut off the matching chars from both words
    elif word1[0] == word2[0]:
        return 0 + score_function(word1[1:], word2[1:])
    #only makes sense to remove or sub chars in word1
    elif len(word1) > len(word2):
        return 1 + min(
            [
                score_function(remove_char(word1), word2),
                score_function(substitute_char(word1, word2[0]), word2)
            ]
        )
    #try all 3 operations
    else:
        return 1 + min(
            [
                score_function(add_char(word1, word2[0]), word2),
                score_function(remove_char(word1), word2),
                score_function(substitute_char(word1, word2[0]), word2)
            ]
        )
    
# END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
def score_function_accurate(word1, word2):
    
    add_char = lambda word1, char: char + word1
    remove_char = lambda word1: word1[1:]
    substitute_char = lambda word1, char: char + word1[1:]
    
    
    ### index out of range cases BEGINNING
    #traversed all of word2, word1 is longer, only remove chars
    if len(word2) == 0 and len(word1) > 0:
        return 1 + score_function_accurate(remove_char(word1), word2)
    #traversed all of word2
    elif len(word2) == 0:
        return 0
    #only makes sense to add chars to word1
    elif len(word1) == 0:
        return 1 + score_function_accurate(add_char(word1, word2[0]), word2)
    ### index out of range cases END
    
    #we found a match, cut off the matching chars from both words
    elif word1[0] == word2[0]:
        return 0 + score_function_accurate(word1[1:], word2[1:])
    #only makes sense to remove or sub chars in word1
    elif len(word1) > len(word2):
        return min(
            [
                1 + score_function_accurate(remove_char(word1), word2),
                score_function_accurate(substitute_char(word1, word2[0]), word2)
            ]
        )
    #try all 3 operations
    else:
        return min(
            [
                1 + score_function_accurate(add_char(word1, word2[0]), word2),
                1 + score_function_accurate(remove_char(word1), word2),
                KEY_DISTANCES[word1[0], word2[0]] + score_function_accurate(substitute_char(word1, word2[0]), word2)
            ]
        )
# END Q7-8
