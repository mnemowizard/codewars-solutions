import math

class Vertex:
    def __init__(self):
        self._links = []
        self.W = False
        self.D = math.inf
        self.path = [[], []]

    @property
    def links(self):
        return self._links

class Link:
    def __init__(self, v1, v2):
        self._v1 = v1
        self._v2 = v2
        self._dist = 1

    @property
    def v1(self):
        return self._v1
    @property
    def v2(self):
        return self._v2
    @property
    def dist(self):
        return self._dist

class LinkedGraph:
    def __init__(self):
        self._links = []
        self._vertex = []

    def add_vertex(self, v):
        if v not in self._vertex:
            self._vertex.append(v)

    def add_link(self, link):
        t = tuple(filter(lambda x: (id(x.v1) == id(link.v1) and id(x.v2) == id(link.v2)) or \
                            (id(x.v1) == id(link.v2) and id(x.v2) == id(link.v1)) , self._links))

        if len(t) == 0:
            self._links.append(link)
            self.add_vertex(link.v1)
            self.add_vertex(link.v2)
            link.v1.links.append(link)
            link.v2.links.append(link)

    def find_path(self, v_start, v_end):
        v_start.D = 0
        v_start.path = [[v_start], []]
        vertexes = self._vertex[:]
        cont = True
        while cont:
            m = vertexes[0].D
            current_vertex = vertexes[0]
            for vertex in vertexes:
                if vertex.D < m and not vertex.W:
                    m = vertex.D
                    current_vertex = vertex
            current_vertex.W = True
            for neighbor in vertexes:
                if neighbor == current_vertex:
                    continue

                for link in neighbor.links:
                    if (link.v1 == current_vertex and link.v2 == neighbor) or (link.v1 == neighbor and link.v2 == current_vertex):
                        new_D = current_vertex.D + link.dist
                        if new_D < neighbor.D:
                            neighbor.D = new_D
                            if neighbor.path[0] and neighbor == neighbor.path[0][-1]:
                                neighbor.path[0] = current_vertex.path[0][:] + [neighbor]
                                neighbor.path[1] = current_vertex.path[1][:] + [link]
                            else:
                                neighbor.path[0] += current_vertex.path[0] + [neighbor]
                                neighbor.path[1] += current_vertex.path[1] + [link]
            vertexes.remove(current_vertex)
            cont = list(filter(lambda vertex: not vertex.W, self._vertex))

        for vertex in vertexes:
            vertex.W = False
            vertex.D = math.inf
            vertex.path = [[], []]
        return v_end.path[0], v_end.path[1]


class Station(Vertex):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class LinkMetro(Link):
    def __init__(self, v1, v2, dist):
        super().__init__(v1, v2)
        self._dist = dist


map_metro = LinkedGraph()
v1 = Station("Сретенский бульвар")
v2 = Station("Тургеневская")
v3 = Station("Чистые пруды")
v4 = Station("Лубянка")
v5 = Station("Кузнецкий мост")
v6 = Station("Китай-город 1")
v7 = Station("Китай-город 2")

map_metro.add_link(LinkMetro(v1, v2, 10))
map_metro.add_link(LinkMetro(v2, v3, 12))
map_metro.add_link(LinkMetro(v1, v3, 15))

map_metro.add_link(LinkMetro(v4, v5, 23))
map_metro.add_link(LinkMetro(v6, v7, 200))

map_metro.add_link(LinkMetro(v2, v7, 50))
map_metro.add_link(LinkMetro(v3, v4, 33))
map_metro.add_link(LinkMetro(v5, v6, 30))

path = map_metro.find_path(v1, v6)
print(f'Оптимальный Маршрут с {v1} до {v6} : {path[0]}')
print(f'Длинна пути {sum([x.dist for x in path[1]])} км')
