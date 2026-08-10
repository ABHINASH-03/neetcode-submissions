class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), reverse=True)

        stack = []

        for pos, spd in cars:
            time = (target - pos) / spd

            # If this car takes longer, it cannot catch
            # the fleet ahead, so it forms a new fleet.
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)