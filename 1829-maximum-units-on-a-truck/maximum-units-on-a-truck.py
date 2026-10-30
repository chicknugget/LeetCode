class Solution:
    def maximumUnits(self, boxTypes: list[list[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        total_units = 0
        
        for boxes, units_per_box in boxTypes:
            take = min(truckSize, boxes)
            total_units += take * units_per_box
            truckSize -= take
            
            if truckSize == 0:
                break
                
        return total_units
