class Solution(object):
    def sortSentence(self, s):
        s =s.split(" ")
        nums =[]
        for i in range(len(s)):
            nums.append(s[i][-1])
        nums.sort()
        print(nums)
        output = ""
        for i in range(len(nums)):
            print(nums[i])
            for j in range(len(s)):
                print(s[j])
                if nums[i] == s[j][-1]:
                    output += s[j][:-1]
                    if s[j][-1] != nums[-1]:
                        output += " "
        return output