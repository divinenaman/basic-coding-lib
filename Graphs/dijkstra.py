def djk(adglist,n,s):
    adg = {}
    visited = [True for _ in range(n)]
    dist = [sys.maxsize for _ in range(n)]
    pg = []

    dist[s] = 0
    heapq.heappush(pq,[s])

    while len(pq):
        curr_i = heapq.heappop(pq)
        visited[curr_i] = True
        adj = adglist[curr_i]

        for i in adj:
            if visited[i] == False:
                new_dist = dist[curr_i] + 1
                if new_dist < dist[i]:
                    dist[i] = new_dist
                    heapq.heappush(pq,[i])
                    adg[i] = [curr_i]

    return adg;