# Add at the count index and maintain an indication for ending word
#O(1) space

class ReverseString:

    def __init__(self, string):
        self.s = "*" + string # String saved
        self.count = 0
        # self.go = False
        self.appendWords()
        return 
        
    def getLastWord(self):
        self.s = self.s.strip()
        ptr = len(self.s) - 1
        while(self.s[ptr] != " "):
            ptr -= 1
        lastWord = self.s[ptr+1:]
        self.s = self.s[:ptr].strip()
        return lastWord
        
    def appendWords(self):
        # The loop
        while(1):
            word = self.getLastWord()
            if word[0] == "*":
                self.s = self.s[:self.count] + " " + word[1:]
                break
            self.s = self.s[:self.count] + word + " " + self.s[self.count:]
            self.count = len(word) + self.count + 1
        print(self.s)
        # The loop
        return

STRING = "the sky is blue"
ReverseString(STRING)
