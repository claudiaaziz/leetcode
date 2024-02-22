class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and trust == []: return 1

        trust_dict = {}
        for person, trusted in trust:
            if trusted in trust_dict:
                trust_dict[trusted].append(person)
            else:
                trust_dict[trusted] = [person]
    
        person = trust_dict.keys()
        trusted_people = [person for sub_arr in trust_dict.values() for person in sub_arr]

        for one_person in person:
            if one_person not in trusted_people and len(trust_dict[one_person]) == n - 1:
                return one_person

        return -1
