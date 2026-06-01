class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            alive = True
            while stack and a < 0 and stack[-1] > 0 and alive:
                if abs(a) > stack[-1]:
                    stack.pop()
                elif abs(a) < stack[-1]:
                    alive = False
                else:
                    stack.pop()
                    alive = False
            if alive:
                stack.append(a)


        return stack



                

