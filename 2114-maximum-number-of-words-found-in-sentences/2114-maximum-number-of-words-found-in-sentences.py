class Solution(object):
    def mostWordsFound(self, sentences):
        return max(sentence.count(' ')+1 for sentence in sentences)
            
         
        