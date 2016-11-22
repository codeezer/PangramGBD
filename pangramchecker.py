#!/usr/bin/env python


def is_pangram(word):
    whole_alphabet = set(["a", "b", "c", "d", "e", "f", "g", "h",
                        "i", "j", "k", "l", "m", "n", "o", "p",
                        "q", "r", "s", "t", "u", "v", "w", "x",
                        "y", "z"])
    
    alphabet = whole_alphabet
    isPangram = False
    pangramCount = 0

    for x in word.lower():
        if x in alphabet:
            alphabet.remove(x)

        if not alphabet:
            isPangram = True
	    pangramCount += 1
            alphabet = whole_alphabet
    
    return isPangram, pangramCount



if __name__ == '__main__':
    main()
