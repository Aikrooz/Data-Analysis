corpus=[
  "Hello Racheal and Micah ",
  "Precious just Got better Glory to GOd",
  "Daddy is the MAn of the house which is The best thing",
  "MUmmy the chairlady ,MY director and her Personal Assistant",
  "MIcah Our BIble scholar the Doctor of the house"
]

split_character=set()

for text in corpus:
  for word in text:
    char=word
    split_character.add(char)

print(sorted(split_character))

splitted_words = {}

for words in corpus:
  words = words.split()
  for word in words:
    if word:
      char_list=list(word)
      word_tuple=tuple(char_list)
      if word_tuple not in splitted_words:
        splitted_words[word_tuple] =0
      splitted_words[word_tuple]+=1

print(splitted_words)





import collections

def get_pair_stats(splits):
  pair_stats = collections.defaultdict(int)
  for word_tuple, count in splits.items():
    symbols = list(word_tuple)
    for i in range(len(symbols) - 1):
      pair = (symbols[i], symbols[i + 1])
      pair_stats[pair] += count
  return pair_stats

def merge_pair(pair_to_merge,splits):
  new_splits = {}
  first,second=pair_to_merge
  merged_token=first +second
  for word_tuple,freq in splits.items():
    symbols=list(word)
    new_symbols=[]
    i=0
    while i < len(symbols):
      if i<len(symbols) -1 and symbols[i]==first and symbols[i+1]==second:
        new_symbols.append(merged_token)
        i+=2
      else:
        new_symbols.append(symbols[i])
        i +=1
      new_splits[tuple(new_symbols)]=freq
    return new_splits

