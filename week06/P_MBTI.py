def solution(survey, choices):
    answer = ''
    char = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    nums = [0] * 8

    for n in range(len(survey)):
        if choices[n] < 4:
            for c in range(len(char)):
                if char[c] == survey[n][0]:
                    nums[c] += (4 - choices[n])
        elif 4 < choices[n] <= 7:
            for c in range(len(char)):
                if char[c] == survey[n][1]:
                    nums[c] += (choices[n] - 4)

    for i in range(0, len(nums) - 1, 2):
        if nums[i] >= nums[i + 1]:
            answer += char[i]
        else:
            answer += char[i + 1]

    return answer



survey1 = ["AN", "CF", "MJ", "RT", "NA"]
choices1 = [5, 3, 2, 7, 5]

survey2 = ["TR", "RT", "TR"]
choices2 = [7, 1, 3]

print(solution(survey1, choices1))
print(solution(survey2, choices2))