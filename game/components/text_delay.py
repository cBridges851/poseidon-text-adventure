import time

def text_delay(sentence):
    '''
        Prints out text in a retro games console style.  
        Args:
            sentence: string, to print out.
    '''
    for letter in sentence:
        # Prints a letter with no separator and ending, while clearing 
        # the internal buffer
        print(letter, sep="", end="", flush=True)
        # Pausing before the next output
        time.sleep(.01)

    # Print new line after a sentence
    print("")