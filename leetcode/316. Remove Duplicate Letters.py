# greedy, medium
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_appearance = {}
        for i, c in enumerate(s):
            last_appearance[c] = i

        answer = []
        answer_set = set()
        for i, c in enumerate(s):
            if c in answer_set:
                continue

            # if the element at the top of the stack is larger than the current element AND appears later too,
            # there is no reason to keep it, let's remove it.
            while answer and answer[-1] > c and last_appearance[answer[-1]] > i:
                value = answer[-1]
                answer.pop()
                answer_set.remove(value)

            answer.append(c)
            answer_set.add(c)

        return ''.join(answer)