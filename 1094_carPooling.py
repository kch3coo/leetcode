class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        curr_seat = 0
        road_map = [0] * 1001
        for i in range(len(trips)):
            numPassengersi = trips[i][0]
            road_map[trips[i][1]] += numPassengersi
            road_map[trips[i][2]] -= numPassengersi
        
        for i in range(len(road_map)):
            curr_seat += road_map[i]
            if curr_seat > capacity:
                return False
            
        return True