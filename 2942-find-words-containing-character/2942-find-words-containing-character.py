class Solution(object):
    def findWordsContaining(self, words, x):
        indices = []
        for i in range(0, len(words), 1):
            if x in words[i]:
                indices.append(i)
        return indices
                
        