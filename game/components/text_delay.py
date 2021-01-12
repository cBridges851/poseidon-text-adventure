import time

def text_delay(sentence):
    '''
    Prints out text in a retro games console style.
    Args:
        sentence: string, to print out.
    '''
    for letter in sentence:
        print(letter, sep="", end="", flush=True)
        time.sleep(.01)

    print("")