class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            sw = ''.join(sorted(word))
            if sw not in hashmap:
                hashmap[sw] = [word]
            else:
                hashmap.get(sw).append(word)
        return hashmap.values()