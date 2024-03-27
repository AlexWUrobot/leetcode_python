# https://leetcode.com/discuss/interview-question/1471459/Amazon-OA
def password(word):
  vowel=0
  consonent=0
  res=0
  for l in word:
    if l=='a' or l=='e' or l=='i' or l=='o' or l=='u':
      vowel+=1
    else:
      consonent+=1
    if vowel>=1 and consonent>=1:
      res+=1
      vowel=0
      consonent=0
  return res

word='thisisbeautiful'
word1='hackerrank'
word2='aeiou'
print(password(word))
print(password(word1))
print(password(word2))
