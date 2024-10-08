## 链表
from typing import Optional


class SingleListNode:
    """定义链表的节点"""

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def print_linkedlist_2_list(head):
    """输出链表为列表的形式"""
    res = []
    current = head
    while current:
        res.append(current.val)
        current = current.next

    return res


def removeElements(head: Optional[SingleListNode], target) -> Optional[SingleListNode]:
    """删除链表节点：创建虚拟头节点"""
    dummy_head = SingleListNode(next=head)
    current = dummy_head

    while current.next:
        if current.next.val == target:
            current.next = current.next.next
        else:
            current = current.next
    return dummy_head.next  # 返回要删除虚拟头节点


def array_2_linkedlist(arr: list):
    """将列表转换为链表"""
    if not arr:
        return None
    head = SingleListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = SingleListNode(val)
        current = current.next

    return head


class SingleLinkedList:
    """设计单链表"""

    def __init__(self):
        self.dummy_head = SingleListNode()
        self.size = 0

    def get(self, index: int) -> int:
        """获取第index个节点的数值"""
        if index < 0 or index >= self.size:
            return -1

        current = self.dummy_head.next  # 因为获取的数值是从实际节点开始的
        for _ in range(index):
            current = current.next

        return current.val

    def addAtHead(self, val: int) -> None:
        """在链表的最前面插入一个节点"""
        self.dummy_head.next = SingleListNode(val, self.dummy_head.next)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """在链表的最后面插入一个节点"""
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = SingleListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """在链表第index个节点前面插入一个节点"""
        if index < 0 or index > self.size:  # 如果index=length，说明是要加末尾直接添加
            return

        current = self.dummy_head

        for _ in range(index):
            current = current.next
        current.next = SingleListNode(val, current.next)
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """删除链表的第index个节点"""
        if index < 0 or index >= self.size:
            return

        current = self.dummy_head
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        self.size -= 1

    def reverselist(self, head: Optional[SingleListNode]) -> Optional[SingleListNode]:
        """
        反转单链表
        示例: 输入: 1->2->3->4->5->NULL 输出: 5->4->3->2->1->NULL
        """


class DoubleListNode:
    """定义双链表"""

    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int):
        if index < 0 or index >= self.size:
            return -1

        if index < self.size // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.size - index - 1):
                current = current.prev

        return current.val

    def addAtHead(self, val: int) -> None:
        # 创建新节点。val是传入的节点值；新节点将成为链表的第一个节点，不会有前驱节点；新节点插入到最前面后，新的节点的next需要指向当前的头节点
        new_node = DoubleListNode(val, prev=None, next=self.head)
        if self.head:
            self.head.prev = new_node
        else:  # 如果链表为空，也就是说，当前插入的新节点将是链表中唯一的节点，它既是头节点也是尾节点。
            self.tail = new_node
        self.head = new_node  # 无论链表是否为空，插入新节点后，新节点都要成为链表的头节点。
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = DoubleListNode(val, prev=self.tail, next=None)
        if self.tail:
            self.tail.next = new_node
        else:
            self.tail = new_node
        self.tail = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            if index < self.size // 2:
                current = self.head
                for _ in range(index - 1):
                    current = current.next
            else:
                current = self.tail
                for i in range(self.size - index):
                    current = current.prev

            new_node = DoubleListNode(val, prev=current, next=current.next)
            current.next.prev = new_node
            current.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.head = self.head.next
            # 检查头节点是否存在，如果存在，则将它的前节点设为None
            if self.head:
                self.head.prev = None
            # 如果链表在删除后变为空
            else:
                self.tail = None

        elif index == self.size - 1:  # 如果删除的是尾节点
            self.tail = self.tail.prev
            # 检查新的尾节点是否存在
            if self.tail:
                self.tail.next = None
            else:
                self.head = None

        else:
            if index < self.size // 2:
                current = self.head
                for _ in range(index):
                    current = current.next
            else:
                current = self.tail
                for i in range(self.size - index - 1):
                    current = current.prev
            current.prev.next = current.next  # 将其前一个节点的prev指向下一个节点
            current.next.prev = current.prev  # 将其下一个节点的prev指向前一个节点

        self.size -= 1


def reverseList(head):
    """翻转链表：双指针"""
    cur = head
    prev = None  # 初始化cur的prev指向的是null

    while cur:
        temp = cur.next  # 先保存cur的下一个节点，因为接下来要改变cur->next
        cur.next = prev  # 反转
        # 更新pre, cur指针，先移动prev
        prev = cur
        cur = temp
    return prev  # prev变成新链表的头节点


def swapPairs(head):
    """两两交换链表中的节点
    假设初始链表为 null -> 1 -> 2 -> 3 -> 4 -> 5，预期输出：null <- 2 <- 1 <- 4 <- 3 <- 5
    """
    dummy_head = SingleListNode(next=head)
    current = dummy_head

    # 必须有cur的下一个和下下个才能交换，否则说明已经交换结束了。链表为偶数个时，current.next为空；为奇数个时，current.next.next为空
    while current.next and current.next.next:
        # 防止节点修改
        temp = current.next  # 初始头节点，1
        temp1 = current.next.next.next  # 下一个起始交换节点，3
        print(f"temp:{temp}, temp1:{temp1}")

        # 开始翻转
        current.next = current.next.next  # current的下一个节点指向2
        current.next.next = temp  # 2指向1
        temp.next = temp1  # 1指向3
        # 目前的链表为 null -> 2 -> 1 -> 3 -> 4 -> 5

        # 往后移动两位，接下来对后面两个节点进行交换
        current = current.next.next  # 虚拟头节点移动到节点1

    return dummy_head.next


if __name__ == '__main__':
    # head1 = array_2_linkedlist([1, 2, 6, 3, 4, 5, 6])
    # listnode = removeElements(head=head1, target=6)
    # print(print_linkedlist_2_list(listnode))

    # obj = DoubleLinkedList()
    # obj.addAtHead(3)
    # obj.addAtTail(4)
    # obj.addAtIndex(1, 7)
    # obj.deleteAtIndex(2)
    # print(obj.get(1))

    head2 = array_2_linkedlist([1, 2, 6, 3, 4])
    trans = swapPairs(head2)
    print(print_linkedlist_2_list(trans))
