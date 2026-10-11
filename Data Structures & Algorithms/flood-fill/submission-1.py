class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        row, col = len(image), len(image[0])
        
        originalColor = image[sr][sc]
        if originalColor == color:
            return image

        def helper(image, r, c, color):
            if min(r, c) < 0 or r == row or c == col or image[r][c] != originalColor:
                return
            image[r][c] = color

            helper(image, r+1, c, color)
            helper(image, r-1, c, color)
            helper(image, r, c+1, color)
            helper(image, r, c-1, color)
        helper(image, sr, sc, color)
        return image