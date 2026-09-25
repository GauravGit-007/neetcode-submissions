class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        signature_bucket = {}

        for i in range(len(strs)):
            signature = ''.join(sorted(strs[i]))

    
            if signature not in signature_bucket:
                signature_bucket[signature]=[]
            signature_bucket[signature].append(strs[i])

        return list(signature_bucket.values())




    

        