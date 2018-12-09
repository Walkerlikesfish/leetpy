import json
from collections import deque

class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        visited_states = set()
        deadends = set(deadends)

        def filter_state(cur_state):
            """Check if the state is legimate
            """
            cur_state_str = ''.join(cur_state)
            if cur_state_str in deadends or cur_state_str in visited_states:
                return None
            visited_states.add(cur_state_str)
            return cur_state_str

        def move_one_step(cur_state):
            """Given state, output 8 possible one-step after states

            :attributes:
                cur_state: string, current state

            :return: List[string] (len()=8)
            """
            result = []
            for ind_c, c in enumerate(cur_state):
                c_int = int(c)
                forward_one = str((c_int + 1) % 10)
                backward_one = str((c_int - 1) % 10)
                new_state = list(cur_state)
                new_state[ind_c] = forward_one
                if filter_state(new_state):
                    result.append(''.join(new_state))
                new_state[ind_c] = backward_one
                if filter_state(new_state):
                    result.append(''.join(new_state))
            return result

        q = deque()
        init_state = ['0'] * 4
        if filter_state(init_state):
            q.append('0000')
        cnt_level = 0

        while q:
            number_of_states = len(q)
            cnt_level += 1
            # iterate through current stage
            for i in range(number_of_states):
                cur_state = q.popleft()
                if cur_state == target:
                    return cnt_level - 1
                generated_states = move_one_step(cur_state)
                # print generated_states
                q.extend(generated_states)

        return -1


def stringToString(input):
    return json.loads(input)


def stringToInt2dArray(input):
    return json.loads(input)


def intToString(input):
    if input is None:
        input = 0
    return str(input)


def stringToStringArray(input):
    return json.loads(input)


def main():
    import sys
    while True:
        try:
            line = sys.stdin.readline().rstrip('\n')
            deadends = stringToStringArray(line)
            line = sys.stdin.readline().rstrip('\n')
            target = stringToString(line)

            ret = Solution().openLock(deadends, target)

            out = intToString(ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    main()