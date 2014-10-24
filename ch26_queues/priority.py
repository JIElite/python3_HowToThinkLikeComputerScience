
class PriorityQueue:
    ''' in this class, we use compound structure "list"
    to do the implamentation '''
    def __init__(self):
        self.items = []

    def is_empty(self):
        ''' if a list is empty , not list is return True '''
        return not self.items

    def insert(self, item):
        self.items.append(item)

    def remove(self):
        maxi = 0
        # in this for-loop we need to traverse all elems.
        # so it cost O(n)
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        # del can use to remove element in the list
        # by access the index. the elements behind the removed elem
        # will reorder in the lst
        del self.items[maxi]
        return item



