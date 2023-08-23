'''I knew exactly what to do but the implementation was difficult. I tried to be clever off the bat by having as few if statements
as possible based on what state we are in but that ended up running into a bunch of errors that were hard to debug. Once I succumbed
to just have 4 different, states it was relatively easy to solve. If I had more time I could probably refactor further but this is
efficient enough.'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        l, r = 0, len(matrix[0]) - 1
        t, b = 0, len(matrix) - 1
        res = []

        state = 0
        while l <= r and t <= b:
            if state == 0:
                for j in range(l, r + 1):
                    res.append(matrix[t][j])
                t += 1
            elif state == 1:
                for i in range(t, b + 1):
                    res.append(matrix[i][r])
                r -= 1
            elif state == 2:
                for j in range(r, l - 1, -1):
                    res.append(matrix[b][j])
                b -= 1
            elif state == 3:
                for i in range(b, t - 1, -1):
                    res.append(matrix[i][l])
                l += 1
                state = -1 

            state += 1
            

        
        return res
