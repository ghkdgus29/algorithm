import collections

NOT_VISIT = 5000

s = int(input())

dist = [[NOT_VISIT] * 1001 for _ in range(1001)]

queue = collections.deque([(1, 0)])
dist[1][0] = 0

while queue:
    emo_cnt, clip_cnt = queue.popleft()

    if dist[emo_cnt][emo_cnt] == NOT_VISIT:
        dist[emo_cnt][emo_cnt] = dist[emo_cnt][clip_cnt] + 1
        queue.append((emo_cnt, emo_cnt))

    if emo_cnt + clip_cnt < 1001 and dist[emo_cnt + clip_cnt][clip_cnt] == NOT_VISIT:
        dist[emo_cnt + clip_cnt][clip_cnt] = dist[emo_cnt][clip_cnt] + 1
        queue.append((emo_cnt + clip_cnt, clip_cnt))

    if emo_cnt > 1 and dist[emo_cnt - 1][clip_cnt] == NOT_VISIT:
        dist[emo_cnt - 1][clip_cnt] = dist[emo_cnt][clip_cnt] + 1
        queue.append((emo_cnt - 1, clip_cnt))

print(min(dist[s]))
