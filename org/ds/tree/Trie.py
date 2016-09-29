'''
Created on Jul 26, 2016

@author: Dushyant Sapra
'''

class Trie:
    def __init__(self, isEndOfWord):
        self.charMap = {};
        self.isEndOfWord = isEndOfWord;

    def insert(self, word):
        if word[0] in self.charMap:
            if len(word) == 1:
                self.charMap[word[0]].isEndOfWord = True;
            else:
                self.charMap[word[0]].insert(word[1:]);
        else:
            if len(word) == 1:
                self.charMap[word[0]] = Trie(True);
            else:
                self.charMap[word[0]] = Trie(False);
                self.charMap[word[0]].insert(word[1:]);

    def prefixBasedSearch(self, prefix):
        if prefix[0] in self.charMap:
            if len(prefix) == 1:
                return True;
            else:
                return self.charMap[prefix[0]].prefixBasedSearch(prefix[1:]);
        else:
            return False;

    def wholeWordBasedSearch(self, word):
        if word[0] in self.charMap:
            if len(word) == 1:
                if self.charMap[word[0]].isEndOfWord:
                    return True;
                else:
                    return False;
            else:
                return self.charMap[word[0]].wholeWordBasedSearch(word[1:]);
        else:
            return False;

#     Here 1 For Carrying Delete Operation on Recursive Nodes
#     2 Means Delete Done, Return same recursively.
#     3 Means Word is not Present, Return same recursively.
    def deleteWord(self, word):
        if word[0] in self.charMap:
            if len(word) == 1:
                if self.charMap[word[0]].isEndOfWord:
                    if len(self.charMap[word[0]].charMap) == 0:
                        del self.charMap[word[0]];
                        if self.isEndOfWord:
                            return 2;
                        else:
                            return 1;
                    else:
                        self.charMap[word[0]].isEndOfWord = False;
                        return 2;
                else:
                    return 3;
            else:
                result = self.charMap[word[0]].deleteWord(word[1:]);
                if result == 1:
                    del self.charMap[word[0]];
                    if self.isEndOfWord:
                        return 2;
                    else:
                        return 1;
                else:
                    return result;
        else:
            return 3;

    def deletePrefixBased(self, prefix):
        if prefix[0] in self.charMap:
            if len(prefix) == 1:
                del self.charMap[prefix[0]];
                if len(self.charMap) == 0:
                    return 1;
                else:
                    return 2;
            else:
                result = self.charMap[prefix[0]].deletePrefixBased(prefix[1:]);
                if result == 1:
                    del self.charMap[prefix[0]];
                    if len(self.charMap) == 0:
                        return 1;
                    else:
                        return 2;
                else:
                    return result;
        else:
            return 3;

#     pending
    def countWordWithPrefix(self, prefix):
        print();

trie = Trie(False);
trie.insert("abcd");
trie.insert("abc");
trie.insert("aec");
trie.insert("alm");
trie.insert("adf");
trie.insert("abed");
trie.insert("lmn");


isPresent = trie.wholeWordBasedSearch("abcd");
print(isPresent)

isPresent = trie.prefixBasedSearch("abc");
print(isPresent)


"""result = trie.deleteWord("abcd");
if result == 1 or result == 2:
    print("Deleted");
else:
    print("Word Not Present");


isPresent = trie.wholeWordBasedSearch("abcd");
print(isPresent);

isPresent = trie.wholeWordBasedSearch("abc");
print(isPresent);"""


result = trie.deletePrefixBased("l");
if result == 1 or result == 2:
    print("Deleted");
else:
    print("No Word with given Prefix",);

isPresent = trie.wholeWordBasedSearch("abcd");
print("abcd is %d", isPresent);

isPresent = trie.wholeWordBasedSearch("abc");
print("abc is %d", isPresent);

isPresent = trie.wholeWordBasedSearch("aec");
print("aec is %d", isPresent);

isPresent = trie.wholeWordBasedSearch("alm");
print("alm is %d", isPresent);

isPresent = trie.wholeWordBasedSearch("adf");
print("adf is %d", isPresent);

isPresent = trie.wholeWordBasedSearch("lmn");
print("lmn is %d", isPresent);