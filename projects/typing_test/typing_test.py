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

# END Q1-5
# Question 6

def score_function(word1, word2):
    """A score_function that computes the edit distance between word1 and word2."""

    if ______________: # Fill in the condition
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6
    
    else:
        add_char = ______________  # Fill in these lines
        remove_char = ______________ 
        substitute_char = ______________ 
        # BEGIN Q6
        "*** YOUR CODE HERE ***"
        # END Q6

KEY_DISTANCES = get_key_distances()

# BEGIN Q7-8
"*** YOUR CODE HERE ***"
# END Q7-8
