学习笔记


简单题目
爬楼梯（阿里巴巴、腾讯、字节跳动在半年内面试常考）
位 1 的个数（Facebook、苹果在半年内面试中考过）
2 的幂（谷歌、亚马逊、苹果在半年内面试中考过）
颠倒二进制位（苹果在半年内面试中考过）

中等题目
实现 Trie (前缀树) （亚马逊、微软、谷歌在半年内面试中考过）
朋友圈（亚马逊、Facebook、字节跳动在半年内面试中考过）
岛屿数量（近半年内，亚马逊在面试中考查此题达到 361 次）
被围绕的区域（亚马逊、eBay、谷歌在半年内面试中考过）
有效的数独（亚马逊、苹果、微软在半年内面试中考过）
括号生成（亚马逊、Facebook、字节跳动在半年内面试中考过）
单词接龙（亚马逊、Facebook、谷歌在半年内面试中考过）
最小基因变化（谷歌、Twitter、腾讯在半年内面试中考过）
比特位计数（字节跳动、Facebook、MathWorks 在半年内面试中考过）

困难题目
单词搜索 II （亚马逊、微软、苹果在半年内面试中考过）
N 皇后（亚马逊、苹果、字节跳动在半年内面试中考过）
解数独（亚马逊、华为、微软在半年内面试中考过）
N 皇后 II （亚马逊在半年内面试中考过）




颠倒二进制位  北美的频率比较高



双向BFS 属于困难类型的

```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list) -> list:
        wordList = set(wordList)  # 转换为hash实现O(1)的in判断
        if endWord not in wordList:
            return []
        # 分别为答案、用于剪枝的已访问哈希，前向分支和后向分支，当前的前向分支以及后向分支中的路径和的长度
        # 前向路径分支与后向路径分支的字典结构为{结束词：到达该结束词的路径列表}
        res, visited, forward, backward, _len = [], set(), {beginWord: [[beginWord]]}, {endWord: [[endWord]]}, 2
        while forward:
            if len(forward) > len(backward):  # 始终从路径分支较少的一端做BFS
                forward, backward = backward, forward
            tmp = {}  # 存储新的前向分支
            while forward:
                word, paths = forward.popitem()  # 取出路径结束词以及到达它的所有路径
                visited.add(word)  # 记录已访问
                for i in range(len(word)):
                    for a in 'abcdefghijklmnopqrstuvwxyz':
                        new = word[:i]+a+word[i+1:]  # 对结束词尝试每一位的置换
                        if new in backward:  # 如果在后向分支列表里发现置换后的词，则路径会和
                            if paths[0][0] == beginWord:  # 前向分支是从beginWord开始的，添加路径会和的笛卡尔积
                                res.extend(fPath + bPath[::-1] for fPath in paths for bPath in backward[new])
                            else:  # 后向分支是从endWord开始的，添加路径会和的笛卡尔积
                                res.extend(bPath + fPath[::-1] for fPath in paths for bPath in backward[new])
                        if new in wordList and new not in visited:  # 仅当wordList存在该词且该词还未碰见过才进行BFS
                            tmp[new] = tmp.get(new, []) + [path + [new] for path in paths]
            _len += 1
            if res and _len > len(res[0]):  # res已有答案，且下一次BFS的会和路径长度已超过当前长度，不是最短
                break
            forward = tmp  # 更新前向分支
        return res

```



