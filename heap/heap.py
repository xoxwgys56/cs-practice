# implement heap using list


class Heap:
    h: list = []

    def __init__(self):
        pass

    def insert_node(self, number: int) -> None:
        self.h.append(number)
        if len(self.h) > 0:
            self.heapify()

    def get_parent_index(node_index: int) -> int:
        """자신의 상위 노드의 인덱스를 반환."""
        pass

    def heapify(self):
        pass
