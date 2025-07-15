def takeAttendance(records: list[int]) -> int:
    res = 0
    print(list(range(len(records) - 1)))
    for i in range(len(records) + 1):
        res = res ^ i ^ records[i - 1]
    res ^= records[len(records) - 1]
    print(res)


takeAttendance([0, 1, 2, 3, 5])
