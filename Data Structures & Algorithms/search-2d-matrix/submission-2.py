class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low=0
        m=len(matrix)
        n=len(matrix[0])
        high=m*n-1

        while low<=high:
            mid=(low+high)//2
            row   =  mid//n
            col   =  mid%n
            value =  matrix[row][col]

            if    value > target:
                high=mid-1
            elif  value < target:
                low=mid+1
            elif value == target:
                return True
        return False

    # only ye figure out karna tha normal low ,high ko 2d array mein se nikalna fir,unse mid nikalna jo ki normal hai ,and then this mid ko wapas 2d array mein  convert karna for comparison 

        