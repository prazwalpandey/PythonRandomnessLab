import sys

from itertools import permutations
from collections import Counter
import load_dictionary


def main():
    name = "tmvoordle"
    name = name.lower()

    word_list_ini = load_dictionary.load("2of4brif.txt")
    trigrams_filtered = load_dictionary.load("least-likely_trigrams.txt")

    word_list = prep_words(name, word_list_ini)
    filtered_cv_map_words = cv_map_words(word_list)
    filter1 = cv_map_filter(name, filtered_cv_map_words)
    filter2 = trigram_filter(filter1, trigrams_filtered)
    filter3 = diagram_filter(filter2)
    view_by_letter(name, filter3)


def prep_words(name, word_list_ini):
    """This function returns the word list with as many letters as in the name."""
    print(f"length of initial Word List = {len(word_list_ini)}")
    print("Initial filter")
    len_name = len(name)
    word_list = [word for word in word_list_ini if len(word) == len_name]
    print(f"Length of new Word List ={len(word_list)}")
    return word_list


def cv_map_words(word_list):
    """Map Letters in words to consonants & vowels."""
    vowels = "aeiou"
    cv_mapped_words = []
    for word in word_list:
        temp = ""
        for letter in word:
            if letter in vowels:
                temp += "v"
            else:
                temp += "c"
        cv_mapped_words.append(temp)
    # determine number of UNIQUE c-v patterns
    total = len(set(cv_mapped_words))
    # target fraction to eliminate
    target = 0.5
    n = int(total * target)
    filtered_cv_map = set()
    count_pruned = Counter(cv_mapped_words).most_common(total - n)
    for pattern, count in count_pruned:
        filtered_cv_map.add(pattern)
    print(f"Length Filter CV Map = {len(filtered_cv_map)}")
    return filtered_cv_map


def cv_map_filter(name, filtered_cv_map):
    """
    This is the first primary filter where we match the POS of permutted words to filtered CV map
    """
    perms = {"".join(letter) for letter in permutations(name)}
    print(f"Length of initial permutations sets = {len(perms)}")
    vowels = "aeiou"
    filter1 = set()
    for word in perms:
        temp = ""
        for letter in word:
            if letter in vowels:
                temp += "v"
            else:
                temp += "c"
        if temp in filtered_cv_map:
            filter1.add(word)

    print(f"Choices after filter_1 = {len(filter1)}")
    return filter1


def trigram_filter(filter1, trigrams_filtered):
    """Remove unlikely trigrams from permutations."""
    filtered = set()
    for candidate in filter1:
        for trigram in trigrams_filtered:
            trigram = trigram.lower()
            if trigram in candidate:
                filtered.add(candidate)

    filter2 = filter1 - filtered
    print(f"Length of Choices after filter_2 = {len(filter2)}")
    return filter2


def diagram_filter(filter2):
    """Remove unlikely digrams from permutations."""
    filtered = set()
    rejects = [
        "dt",
        "lr",
        "md",
        "ml",
        "mr",
        "mt",
        "mv",
        "td",
        "tv",
        "vl",
        "vm",
        "vr",
        "vt",
    ]
    first_pair_rejects = ["ld", "lm", "lt", "lv", "rd", "rl", "rm", "rt", "tl", "tm"]
    for candidate in filter2:
        for r in rejects:
            if r in candidate:
                filtered.add(candidate)
        for fr in first_pair_rejects:
            if candidate.startswith(fr):
                filtered.add(candidate)
    filter3 = filter2 - filtered
    print(f"Length of choices after filter_3 = {len(filter3)}")
    if "voldemort" in filter3:
        print("Voldemort Found!", file=sys.stderr)
    return filter3


def view_by_letter(name, filter3):
    """Filter to anagrams starting with input letter."""
    print(f"Remaining Letters ={name}")
    first = input("select a starting letteror press Enter to see all: ")
    subset = []
    for candidate in filter3:
        if candidate.startswith(first.lower()):
            subset.append(candidate)
    print(*sorted(subset), sep="\t")
    print(f"Number of choices starting with the letter {first} = {len(subset)}")
    try_again = input("Try Again? (Press Enter else any other key to exit.)")
    if try_again.lower() == "":
        view_by_letter(name, filter3)
    else:
        sys.exit()


if __name__ == "__main__":
    main()
