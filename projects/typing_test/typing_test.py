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
    #words typed per minute
    stripped_typed = strip(typed_string)

    def words_per_minute(typed_string, start_time, end_time):
        ONE_WORD_LENGTH = 5
        SECONDS_IN_MINUTE = 60
        
        time_typing = end_time - start_time
        #words in string
        words_amount = len(typed_string) / ONE_WORD_LENGTH       
        words_per_minute = SECONDS_IN_MINUTE / time_typing * words_amount
        
        return words_per_minute
    
    #the accuracy of typed text
        
    def accuracy(sample, typed):
        sample_words = sample.split()
        typed_words = typed.split()

        if len(typed_words) <= 0:
            return 0.0

        words_matched = 0
        for s, t in zip(sample_words, typed_words):
            if lower(s) == lower(t):
                words_matched += 1

        #calculate based on required words. If less then required typed, calculate based on typed amount
        total_words = len(sample_words) if len(sample_words) < len(typed_words) else len(typed_words)
        match_percentage = (words_matched / total_words) * 100

        return match_percentage
    
    return [words_per_minute(typed_string, start_time, end_time), accuracy(sample_paragraph, stripped_typed)]

#q3
def pig_latin(word):
    VOWELS = 'aeiouAEIOU'
    CNSNANT_SUFFIX = 'ay'
    VOWEL_SUFFIX = 'way'
    
    begins_with_vowel = word[0] in VOWELS

    if begins_with_vowel:
        return word + VOWEL_SUFFIX
    else:
        cnsnant_cluster = ''
        slice_index = 0

        for i in range(len(word)):
            if word[i] not in VOWELS:
                 cnsnant_cluster += word[i]
                 slice_index += 1
            else:
                 break
        return word[slice_index:] + cnsnant_cluster + CNSNANT_SUFFIX
    

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

add_char = lambda word1, char: char + word1
rem_char = lambda word1: word1[1:]
sub_char = lambda word1, char: char + word1[1:]
def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""
    #words match
    if word1 == word2:
        return 0
    #if len(word2) is 0 return len(word1)
    elif len(word2) == 0:
        return len(word1)
    elif len(word1) == 0:
        return 1 + score_function(add_char(word1, word2[0]), word2)
    elif word1[0] == word2[0]:
        return 0 + score_function(word1[1:], word2[1:])
    elif len(word1) > len(word2):
        return 1 + min(
            score_function(sub_char(word1, word2[0]), word2),
            score_function(rem_char(word1), word2)
        )
    else:
        return 1 + min(
            score_function(sub_char(word1, word2[0]), word2),
            score_function(rem_char(word1), word2),
            score_function(add_char(word1, word2[0]), word2)
        )
    
# END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
def score_function_accurate(word1, word2):
    #words match
    if word1 == word2:
        return 0
    #if len(word2) is 0 return len(word1)
    elif len(word2) == 0:
        return len(word1)
    elif len(word1) == 0:
        return 1 + score_function_accurate(add_char(word1, word2[0]), word2)
    elif word1[0] == word2[0]:
        return 0 + score_function_accurate(word1[1:], word2[1:])
    elif len(word1) > len(word2):
        return min(
            KEY_DISTANCES[word1[0], word2[0]] + score_function_accurate(sub_char(word1, word2[0]), word2),
            1 + score_function_accurate(rem_char(word1), word2)
        )
    else:
        return min(
            KEY_DISTANCES[word1[0], word2[0]] + score_function_accurate(sub_char(word1, word2[0]), word2),
            1 + score_function_accurate(rem_char(word1), word2),
            1 + score_function_accurate(add_char(word1, word2[0]), word2)
        )


def score_function_final(word1, word2):
    cache = {}
    
    def save_in_cache(word1, word2, score):
        cache[word1+word2] = score
        cache[word2+word1] = score

    def score_function(word1, word2):
        #words match
        if word1 == word2:
            return 0
        #if len(word2) is 0 return len(word1)
        elif len(word2) == 0:
            return len(word1)
        elif len(word1) == 0:
            return 1 + score_function_memo(add_char(word1, word2[0]), word2)
        elif word1[0] == word2[0]:
            return 0 + score_function_memo(word1[1:], word2[1:])
        elif len(word1) > len(word2):
            return min(
                KEY_DISTANCES[word1[0], word2[0]] + score_function_memo(sub_char(word1, word2[0]), word2),
                1 + score_function_memo(rem_char(word1), word2)
            )
        else:
            return min(
                KEY_DISTANCES[word1[0], word2[0]] + score_function_memo(sub_char(word1, word2[0]), word2),
                1 + score_function_memo(rem_char(word1), word2),
                1 + score_function_memo(add_char(word1, word2[0]), word2)
            )

    def score_function_memo(word1, word2):
        if word1+word2 not in cache:
            save_in_cache(word1, word2, score_function(word1, word2)) 
        return cache[word1+word2]

    return score_function_memo(word1, word2)

# END Q7-8
