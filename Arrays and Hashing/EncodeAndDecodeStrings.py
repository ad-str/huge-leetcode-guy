class Solution:
    """
    @param: strs: a list of strings
    @return: encodes a list of strings to a single string.
    """
    def encode(self, strs):
        '''My original idea was to generate an escape character like colon in case we enounter a colon
        inside the words. This would require looping over the characters in the word as well which is
        extra code. This method condenses the code to just use the length of the word instead of an escape
        character. While it may be the same amount of time as my original method, it is neater.'''
        wordString = ""
        for word in strs:
            wordString += str(len(word)) + word
        return wordString


    """
    @param: str: A string
    @return: dcodes a single string to a list of strings
    """
    def decode(self, str):
        '''I may have needed some help with the encode function but this one is all me'''
        if str == "": return ""

        wordList = []

        wordLength = int(str[0])
        word = ""
        for i in range(1, len(str)):
            if wordLength == 0:
                wordList.append(word)
                word = ""
                wordLength = int(str[i])
                continue

            word += str[i]
            wordLength -= 1

        wordList.append(word) # add the last word
        return wordList
        

if __name__ == "__main__":
    solution = Solution() 

    encoded = solution.encode(["we", "say", "a3#bcd", "yes"])
    print(encoded)
    result = solution.decode(encoded)
    print(result)
