class stack:

    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if len(self.__data) == 0:
            return None
        return self.__data.pop()

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.__data) > 0:
            return self.pop()
        else:
            raise StopIteration

    def get_stack(self):
        return self.__data


class queue:

    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if len(self.__data) == 0:
            return None
        return self.__data.pop(0)

    def __iter__(self):
        return self

    def __next__(self):
        if len(self.__data) > 0:
            return self.pop()
        else:
            raise StopIteration

    def get_stack(self):
        return self.__data


if __name__ == '__main__':
    st = stack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    print(st.pop())
    for i in st:
        print(i)

    q = queue()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    print(q.pop())
    for i in q:
        print(i)
