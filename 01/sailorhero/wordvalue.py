import os
# from collections import Counter

from data import DICTIONARY, LETTER_SCORES
from loguru import logger


def load_words():
    """Load dictionary into a list and return list"""
    file_path =os.path.join(os.path.dirname(__file__),DICTIONARY)
    logger.debug(f'Load dictionary file : {file_path}')
    
    # with open(file_path,'r') as f:
    #     lines = f.readlines()
    # return [line.strip() for line in lines]
    with open(file_path,'r') as f:
        lines = f.read().splitlines()
    return [line.strip() for line in lines]
    

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(letter.upper(),0) for letter in word)

def max_word_value(words = []):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    return max((words or load_words()),key=lambda x:calc_word_value(x))

if __name__ == "__main__":
    words = load_words()
    logger.info(f'load_words finished, load {len(words)} words')
    
    max_word = max_word_value([])
    logger.info((f'The word has max value is {max_word}'))
    
    

