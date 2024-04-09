class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count = {}
        for n in hand:
            count[n] = 1 + count.get(n, 0)

        minH = list(count.keys())
        heapq.heapify(minH)
        while minH:
            first = minH[0]
            for i in range(first, first + groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minH[0]:
                        return False
                    heapq.heappop(minH)
        return True



from collections import Counter
import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand_dict = Counter(hand)
        min_heap = list(hand_dict.keys())
        heapq.heapify(min_heap)

        while min_heap:
            first = min_heap[0]

            for i in range(first, first + groupSize):
                if i not in hand_dict:
                    return False
                
                hand_dict[i] -= 1
                if hand_dict[i] == 0:
                    # If i isn't the minimum, there will be another minimum and
                    # i will cause a gap, so we can't complete consecutive numbers.
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)
        
        return True



        



        