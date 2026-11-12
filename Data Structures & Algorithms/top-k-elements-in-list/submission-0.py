class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = {}

        for num in nums:
            if num in new_dict:
                new_dict[num] += 1
            else:
                new_dict[num] = 1

        result = []

        for i in range(k):
            most_frequent = max(new_dict, key=new_dict.get)
            result.append(most_frequent)
            del new_dict[most_frequent]

        return result



        