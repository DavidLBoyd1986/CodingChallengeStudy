import string
from random import randrange


def guess_phrase(target_phrase):
    possible_guesses = string.ascii_lowercase + " "
    guessed_phrase = ""
    for position in range(len(target_phrase)):
        guessed_phrase += possible_guesses[randrange(len(possible_guesses))]
    return guessed_phrase


def score_phrase(target_phrase, guessed_phrase):
    score = 0
    for position in range(len(target_phrase)):
        if guessed_phrase[position] == target_phrase[position]:
            score += 1
    return score


def run_phrase_guess_tests():
    target_phrase = "methinks it is like a weasel"
    score = 0
    best_score = 0
    best_phrase = ""
    test_number = 1
    while score != len(target_phrase):
        guessed_phrase = guess_phrase(target_phrase)
        score = score_phrase(target_phrase, guessed_phrase)
        if score > best_score:
            best_score = score
            best_phrase = guessed_phrase
        if test_number % 100000 == 0:
            print("Best score by test " + str(test_number) + ": " + str(best_score)
                  + " with phrase: " + best_phrase)
        test_number += 1
    print("The tests are over. It took " + str(test_number) + " tries before the phrase was randomly guessed")


def guess_phrase_remember_correct(target_phrase, remembered):
    possible_guesses = string.ascii_lowercase + " "
    guessed_phrase = ""
    for position in range(len(target_phrase)):
        if position in remembered:
            guessed_phrase += remembered.get(position)
        else:
            guessed_phrase += possible_guesses[randrange(len(possible_guesses))]
    return guessed_phrase


def score_phrase_remember_correct(target_phrase, guessed_phrase, remembered):
    score = 0
    for position in range(len(target_phrase)):
        if position in remembered.keys():
            score += 1
            continue
        if guessed_phrase[position] == target_phrase[position]:
            score += 1
            remembered[position] = target_phrase[position]
    return score


def run_phrase_guess_tests_remember_correct():
    target_phrase = "methinks it is like a weasel"
    remembered = {}
    score = 0
    best_score = 0
    test_number = 1
    while score != len(target_phrase):
        guessed_phrase = guess_phrase_remember_correct(target_phrase, remembered)
        print(guessed_phrase)
        score = score_phrase_remember_correct(target_phrase, guessed_phrase, remembered)
        if score > best_score:
            best_score = score
        if test_number % 1000000 == 0:
            print("Best score by test " + str(test_number) + ": " + str(best_score))
        test_number += 1
    print("The tests are over. It took " + str(test_number) + " tries before the phrase was randomly guessed")

#run_phrase_guess_tests()

run_phrase_guess_tests_remember_correct()
