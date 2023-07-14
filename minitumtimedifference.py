def findMinDifference(timePoints) -> int:
    t_arr = []
    for i in range(len(timePoints)):
        if timePoints[i].split(":")[0] != "00":
            h_t = int(timePoints[i].split(":")[0])

            m_t = int(timePoints[i].split(":")[1])

        else:
            h_t = 0
            m_t = int(timePoints[i].split(":")[1])
        print(h_t)
        if h_t == 0 and m_t == 0:
            t_arr.append(1440)
        elif 23 - h_t <= 11:
            t_arr.append((23 - h_t) * 60 + (60 - m_t))
        else:
            t_arr.append(h_t * 60 + m_t)

    t_arr.sort()
    print(t_arr)
    min_d = t_arr[1] - t_arr[0]
    for i in range(len(t_arr) - 1):
        min_d = min(min_d, t_arr[i + 1] - t_arr[i])

    print(min_d)

findMinDifference(["05:31","22:08","00:35"])