# 留给读者练习，如果实在想不出，在第 5 章栈里 stack.py 会有实现


# NOTE：注意这里是第三章 double_link_list.py 里的内容，为了使文件自包含，我直接拷贝过来的

class Node(object):

    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next


class CircularDoubleLinkedList(object):
    """循环双端链表 ADT
    多了个循环其实就是把 root 的 prev 指向 tail 节点，串起来
    """

    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def headnode(self):
        return self.root.next

    def tailnode(self):
        return self.root.prev

    def append(self, value):    # O(1), 你发现一般不用 for 循环的就是 O(1)，有限个步骤
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value=value)
        tailnode = self.tailnode() or self.root

        tailnode.next = node
        node.prev = tailnode
        node.next = self.root
        self.root.prev = node
        self.length += 1

    def appendleft(self, value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('LinkedList is Full')
        node = Node(value=value)
        if self.root.next is self.root:   # empty
            node.next = self.root
            node.prev = self.root
            self.root.next = node
            self.root.prev = node
        else:
            node.prev = self.root
            headnode = self.root.next
            node.next = headnode
            headnode.prev = node
            self.root.next = node
        self.length += 1

    def remove(self, node):      # O(1)，传入node 而不是 value 我们就能实现 O(1) 删除
        """remove
        :param node  # 在 lru_cache 里实际上根据key 保存了整个node:
        """
        if node is self.root:
            return
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self.length -= 1
        return node.value

    def iter_node(self):
        if self.root.next is self.root:
            return
        curnode = self.root.next
        while curnode.next is not self.root:
            yield curnode
            curnode = curnode.next
        yield curnode

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node_reverse(self):
        """相比单链表独有的反序遍历"""
        if self.root.prev is self.root:
            return
        curnode = self.root.prev
        while curnode.prev is not self.root:
            yield curnode
            curnode = curnode.prev
        yield curnode

######################################################
# 下边是 deque 实现
######################################################

class Deque(object):
    def __init__(self, maxsize=None):
        self.maxsize = maxsize
        self._item_double_link_list = CircularDoubleLinkedList()

    def __len__(self):
        return len(self._item_double_link_list)

    def pophead(self):             # O(1)
        """从队头取数据"""
        node = self._item_double_link_list.headnode()
        return self._item_double_link_list.remove(node)

    def poptail(self):
        """从队尾取数据"""
        node = self._item_double_link_list.tailnode()
        return self._item_double_link_list.remove(node)

    def pushtail(self, value):
        """从队尾加数据"""
        return self._item_double_link_list.append(value)

    def pushhead(self, value):
        """从队头加数据"""
        return self._item_double_link_list.appendleft(value)

def testDeque():
    q = Deque()
    q.pushtail(1)
    q.pushtail(2)
    q.pushhead(3)
    q.pushhead(4)
    assert q.pophead() == 4
    assert q.poptail() == 2
    assert q.poptail() == 1
    assert q.poptail() == 3
    assert len(q) == 0

if __name__ == '__main__':
    testDeque()
