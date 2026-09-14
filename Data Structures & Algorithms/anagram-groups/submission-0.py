class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # an anagram will have same length and sorted pattern
        # how to check length/ sort each string in a list
        # return the results as list of strings with sublist [[],[],...]
        result = defaultdict(list)
        for s in strs:
            sorted_strs = ''.join(sorted(s))
            result[sorted_strs].append(s)
        return list(result.values())



    