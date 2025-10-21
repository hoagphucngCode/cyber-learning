# word_count.py
from collections import Counter

# Mở file sample.txt
with open("sample.txt", "r") as f:
    text = f.read()

# Đếm dòng và từ
lines = text.strip().split("\n")
words = text.split()

print(f"Total lines: {len(lines)}")
print(f"Total words: {len(words)}")

# Đếm tần suất từ
counter = Counter(word.strip('.,!?').lower() for word in words)
common = counter.most_common(3)
print("\nTop 3 most frequent words:")
for word, count in common:
    print(f"{word}: {count}")

