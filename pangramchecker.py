#!/usr/bin/env python

#function which checks whether the sentence is pangram or not
#pangram is a sentence that contains all the letters of the English alphabet at least once

#function takes sentence as argument
#the function returns true is sentence is pangram and its occurence

def is_pangram(word):
    
    alphabet_set = set(["a", "b", "c", "d", "e", "f", "g", "h",
                        "i", "j", "k", "l", "m", "n", "o", "p",
                        "q", "r", "s", "t", "u", "v", "w", "x",
                        "y", "z"])

    isPangram = 'No'
    pangramCount = 0

    for x in word.lower():
        if x in alphabet_set:
            alphabet_set.remove(x)
            #remove those alphabets which exists in sentence given 
        
        #if alphabet_sets is equal to null then the given words is pangram

        if not alphabet_set:
            isPangram = 'Yes'
	    pangramCount += 1
            
            #refill alphabet_set to check again 
            alphabet_set = set(["a", "b", "c", "d", "e", "f", "g", "h",
                            "i", "j", "k", "l", "m", "n", "o", "p",
                            "q", "r", "s", "t", "u", "v", "w", "x",
                            "y", "z"])
    
    return isPangram, pangramCount


def main():
    
    test_string = "The quick brown fox jumps over the lazy gdo poiuytrewqasdfghjklmnbvcxz.\
 The quick brown fox jumps over the lazy dog mnbvcxzasdfghjklpoiuytrewq."
    
    isPangram, pangramCount = is_pangram(test_string)
    print (test_string+'\n')


    print (" o Is it a pangram: " + isPangram)
    print (" o Occurence: " + str(pangramCount))


if __name__ == '__main__':
    main()
