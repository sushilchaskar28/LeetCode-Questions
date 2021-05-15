def isWordFound(word,uniq,wordDict):
	if word in wordDict: return wordDict[word]
	for i in range(1,len(word)):
		pre = word[:i]
		suf = word[i:]
		if pre in uniq:
			if suf in uniq or isWordFound(suf,uniq,wordDict):
				wordDict[word]=True
				return True
	wordDict[word]=False
	return False
        

def findAllConcatenatedWordsInADict(words):
	uniq =set(words)
	wordDict={}
	return [word for word in words if isWordFound(word,uniq,wordDict)]
	
print(findAllConcatenatedWordsInADict(['cat','cats','dog','catdogs']))