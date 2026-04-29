# Heap: 모든 노드가 특정한 순서를 유지하며 구성된 완전 이진트리 형태의 자료

# 내부 구현 없이 Heap 개념 이해하기
import heapq    # default: Min heap

""" Min Heap """
heap = []

heapq.heappush(heap, 30)
heapq.heappush(heap, 10)
heapq.heappush(heap, 20)

print("현재 heap 상태: ", heap)
# 현재 heap 상태:  [10, 30, 20]
print("가장 작은 값: ", heapq.heappop(heap))
print("남은 힙: ", heap)
# 가장 작은 값:  10     >> 알아서 가장 작은 값 배출
# 남은 힙:  [20, 30]

""" Max Heap """
heap = []
heapq.heappush(heap, -30)
heapq.heappush(heap, -10)
heapq.heappush(heap, -20)
print("현재 heap 상태: ", heap)
# 가장 큰 값:  30
print("가장 큰 값: ", -heapq.heappop(heap))
print("가장 큰 값: ", -heapq.heappop(heap))
print("남은 힙: ", heap)
# 가장 큰 값:  20
# 남은 힙:  [-10]


""" Greedy 알고리즘 """





