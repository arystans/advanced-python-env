items = input().split()
freq = {}
for item in items:
    if item in freq:
        freq[item] += 1
    else:
        freq[item] = 1
print("Purchase frequency:")
for k in freq:
    print(k, freq[k])
max_item = None
max_count = 0
for k in freq:
    if freq[k] > max_count:
        max_count = freq[k]
        max_item = k
print("\nMost popular item:", max_item)
print("\nPurchased once:")
for k in freq:
    if freq[k] == 1:
        print(k, end=" ")
sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)
print("\nSorted by frequency :")
for item, count in sorted_items:
    print(item, count)

