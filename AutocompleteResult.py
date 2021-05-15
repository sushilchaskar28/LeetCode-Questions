class Trie:
    def __init__(self):
        self.children={}
        self.isW=False

class Solution:
    def __init__(self):
        self.trie=Trie()
    def buildTrie(self,words):
        for word in words: 
            cur = self.trie
            for char in word:
                if char not in cur.children: cur.children[char]=Trie()
                cur=cur.children[char]
            cur.isW=True
            
    def autoComplete(self,prefix):
        cur = self.trie
        for char in prefix:
            if char not in cur.children: return []
            cur = cur.children[char]
        return self.dfs(cur,prefix)
    
    def dfs(self,cur,word):
        arr=[]
        if cur.isW:
            arr+=[word]
        for child in cur.children:
            arr+= self.dfs(cur.children[child],word+child)
        return arr
        
s = Solution()
s.buildTrie(['dog','dark','cat','dodr','dodge'])
print(s.autoComplete('dod'))
