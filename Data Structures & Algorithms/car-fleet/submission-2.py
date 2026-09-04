class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        the stack stores the times of the cars that have not been popped (i.e. they will not collide with another car)
        we can see if a car will collide with the formula time = (target - position) / speed
        if time is less than the car in front of it, then they will collide at some point
        always pop the car behind because its speed will change, while the speed of the car in front will NEVER change
        """
        
        cars = [[p, s] for p, s in zip(position, speed)]

        stack = []

        for p, s in reversed(sorted(cars)): # reversing because the car in front can not be affected by the cars behind
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop() # new car is popped if it collides
        return len(stack)

