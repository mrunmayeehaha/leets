class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        altitude = 0
        i = 0
        while(i < len(gain)):
            altitude = altitude + gain[i]

            if altitude > highest:
                highest = altitude
            i = i + 1
        return highest
