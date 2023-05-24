from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for item in strs:
            chars_t = tuple(sorted(item))
            res[chars_t].append(item)
        return list(res.values())
