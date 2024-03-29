import string

### DO NOT MODIFY THIS FUNCTION ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print('Loading word list from file...')
    # inFile: file
    in_file = open(file_name, 'r')
    # line: string
    line = in_file.readline()
    # word_list: list of strings
    word_list = line.split()
    print('  ', len(word_list), 'words loaded.')
    in_file.close()
    return word_list

### DO NOT MODIFY THIS FUNCTION ###
def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

### DO NOT MODIFY THIS FUNCTION ###
def get_story_string():
    """
    Returns: a joke in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        upperAlpha = list(string.ascii_uppercase)
        letterDict = {}
        for i in range(len(upperAlpha)):
            letter = upperAlpha[i]
            shiftIndex = i + shift
            if shiftIndex >= len(upperAlpha):
                shiftIndex -= len(upperAlpha)
            shiftLetter = upperAlpha[shiftIndex]
            letterDict[letter] = shiftLetter
            letterDict[letter.lower()] = shiftLetter.lower()
        return letterDict
    
    

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        shiftText = ''
        letterDict = self.build_shift_dict(shift)
        for letter in self.message_text:
            if letter in letterDict:
                shiftText += letterDict[letter]
            else:
                shiftText += letter
        return shiftText
            

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encrypting_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        Hint: consider using the parent class constructor so less 
        code is repeated
        '''
        super().__init__(text)
        self.change_shift(shift)
        
    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encrypting_dict(self):
        '''
        Used to safely access a copy self.encrypting_dict outside of the class
        
        Returns: a COPY of self.encrypting_dict
        '''
        return self.encrypting_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift (ie. self.encrypting_dict and 
        message_text_encrypted).
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encrypting_dict = self.build_shift_dict(shift)
        self.message_text_encrypted = self.apply_shift(shift)
        


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        super().__init__(text)
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)
        self.DEBUG_ON = False
        
    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of you may choose any of those shifts (and their
        corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        (best_shift, best_decode) = (0, self.message_text)
        maxNumWords = 0
        for s in range(26):
            numWords = 0
            decode = self.apply_shift(26 - s)
            if self.DEBUG_ON:
                print(26 - s, decode, self.message_text)
            for word in decode.split():
                if word in self.valid_words:
                    numWords += 1
            if numWords > maxNumWords:
                (best_shift, best_decode) = (26 - s, decode)
                maxNumWords = numWords
                if self.DEBUG_ON:
                    print('maxNumWords:', maxNumWords)
        return (best_shift, best_decode)
    
def decrypt_story():
    story_string = get_story_string()
    ciphertext = CiphertextMessage(story_string)
    return ciphertext.decrypt_message()    
        
        # best_shift = 0
        # max_real_words = 0
        # decrypted_message = ""

        # for shift in range(26):
        #     decrypted_text = self.apply_shift(26 - shift)
        #     words = decrypted_text.split()
        # real_words = 0
        # # real_words = sum(is_word(word.strip(string.punctuation), self.valid_words) for word in words)
        # for word in words:
        #      if is_word(self.valid_words, word.strip(string.punctuation)):
        #         real_words += 1
        # if real_words > max_real_words:
        #     max_real_words = real_words
        #     best_shift = shift
        #     decrypted_message = decrypted_text

        # return best_shift, decrypted_message

#Example test case (PlaintextMessage)
plaintext = PlaintextMessage('hello', 2)
print('Expected Output: jgnnq')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage('jgnnq')
print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())

'6.00.1x is pretty fun'.split(' ')
['6.00.1x', 'is', 'pretty', 'fun']

plaintext = PlaintextMessage('6.00.1x is pretty fun', 5)
# print('Expected Output: ')
print('Actual Output:', plaintext.get_message_text_encrypted())
    
#Example test case (CiphertextMessage)
ciphertext = CiphertextMessage(plaintext.get_message_text_encrypted())
# print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())

story_string = get_story_string()
ciphertext = CiphertextMessage(story_string)
# print('Expected Output:', (24, 'hello'))
print('Actual Output:', ciphertext.decrypt_message())

