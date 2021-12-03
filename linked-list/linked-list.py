from __future__ import annotations


class Node:
    _number: int
    _next_node: Node

    def __init__(self, number: int) -> None:
        self._number = number
        self._next_node = None

    def set_next_node(self, next_node: Node) -> None:
        self._next_node = next_node

    @property
    def next_node(self) -> Node:
        return self._next_node

    @property
    def number(self) -> int:
        return self._number

    def __str__(self) -> str:
        if self.next_node:
            return f"<Node number={self.number} next_node={self.next_node.number}>"
        else:
            return f"<Node number={self.number} next_node={None}>"


"""
simple linked list

- 중복 값을 허용한다.

아래 코드는 간단한 구현을 위해 예외처리가 대부분 생략되었다.
"""


class LinkedList:
    root_node: Node
    last_node: Node
    size: int

    def __init__(self) -> None:
        self.root_node = None
        self.last_node = None
        self.size = 0

    def insert(self, number: int) -> None:
        if not self.size:
            self.root_node = Node(number)
            self.last_node = self.root_node
        else:
            node = Node(number)
            self.last_node.set_next_node(node)
            self.last_node = node

        self.size += 1

    def remove(self, number: int) -> None:
        current_node = self.root_node
        prev_node = None

        while current_node:
            if current_node.number == number:
                break
            prev_node = current_node
            current_node = current_node.next_node

        if not current_node:
            raise ValueError(f"there is no Node include '{number}'.")
        else:
            next_node = current_node.next_node
            prev_node.set_next_node(next_node)
            del current_node
            print(f"remove Node include '{number}'.")

    def print(self) -> None:
        current_node = self.root_node
        index = 0
        while current_node:
            print(f"{index} Node {current_node.number}")
            index += 1
            current_node = current_node.next_node


if __name__ == "__main__":
    linked_list = LinkedList()

    for number in range(10):
        linked_list.insert(number ** 2)

    linked_list.print()
    linked_list.remove(4)
    linked_list.remove(10)
    linked_list.print()
