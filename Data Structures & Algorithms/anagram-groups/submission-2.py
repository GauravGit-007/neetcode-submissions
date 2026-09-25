class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        signature_bucket = {}

        for word in range(len(strs)):
            signature = ''.join(sorted(strs[word]))

    
            if signature not in signature_bucket:
                signature_bucket[signature]=[]
            signature_bucket[signature].append(strs[word])

        return list(signature_bucket.values())




    

        