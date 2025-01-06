
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = []
        q.append((sr, sc))
        original_color = image[sr][sc]
        while q:
            x,y = q.pop(0)
            if x < 0 or y < 0 or x >= len(image) or y >= len(image[0]):
                continue

            if image[x][y] == original_color and image[x][y] != color:
                image[x][y] = color
                q.append((x-1,y))
                q.append((x,y-1))
                q.append((x, y + 1))
                q.append((x+1,y))
            
        return image
    