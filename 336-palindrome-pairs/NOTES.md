```
class Solution:
def palindromePairs(self, words: List[str]) -> List[List[int]]:
output = []
for i, w1 in enumerate(words):
for j, w2 in enumerate(words):
if i == j:
continue
if self.isPalendrome(w1+w2):
output.append([i,j])
return output
​
​
def isPalendrome(self, word: str) -> bool:
if self.isPossiblePalendrome(word):
left = 0
right = len(word) - 1
while left < right:
if word[left] != word[right]:
return False
left += 1
right -= 1
return True
​
​
def isPossiblePalendrome(self, word: str) -> bool:
bitmap_count = 0
for i, char in enumerate(word):
bitmap_count ^= 1<<(ord(char)-96)
if bitmap_count & bitmap_count - 1 == 0:
return True
```