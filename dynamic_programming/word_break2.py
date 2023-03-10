"""
Problem:
    'Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.' 
 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.


- LeetCode(https://leetcode.com/problems/word-break-ii/)




"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_lists=[]
        for i in range(len(s)):
            substr=s[len(s)-1-i:]
            word_lists.append([])
            for word in wordDict:
                if word == substr[0:len(word)]:
                    if len(substr)==len(word):
                        word_lists[i].append(word)
                    else:
                        for j in range(len(word_lists[i-len(word)])):
                            word_lists[i].append(word+" "+word_lists[i-len(word)][j])
        return word_lists.pop()


"""
Typical dp problem. The problem could be divided into subproblems of finding all possible sentences for every possible substring of s using the word dictionary given.
Two approaces seem possible: 1. Top-down, 2. Bottom-up. For Top-down, recursion could be used with memoization. For Bottom-up, looping with a 2D list could be used. 
The above solution is a Bottom-up approach.
For bottom-up approach, we could visit each position in the string from the end. For each position, we could find all words that can be formed from the substring starting from the current position. We add each word found to sentences that have previously been identified to be able to start from the end of the word. This corresponds to lines 11,12:

'
for j in range(len(word_lists[i-len(word)])):
    word_lists[i].append(word+" "+word_lists[i-len(word)][j])
'

This way, we can guarantee that word_lists[i] contains all the possible sentences that starts from i, and this will give us the answer to the problem at the last index

"""
