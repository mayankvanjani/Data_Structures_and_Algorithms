import copy
import xml.etree.ElementTree as etree

class Graph():
    class Vertex():
        def __init__(self,label=None):
            self._label = label
        def element(self):
            return self._label
        def hash(self):#because vertex will be key value
            return hash(self._label)

    class Edge():
        def __init__(self,fro,to,label=None): #from and to should be vertices
            self._from = 0
            self._to = 0
            self._label = label
        def endpoints(self):
            return (self._to,self._from)
        def opposite(self,u): #opposite takes edge and one endpt and returns other endpt
            return self._to if u is self._from else self._from

    def __init__(self):#2 dict if directed graph
        self._out = {}

    def add_vertex(self,label=None):
        newv = self.Vertex(label)
        self._out[newv] = {}
        return newv

    def add_edge(self,u,v,label=None):
        newe = self.Edge(u,v,label)
        self._out[u][v] = newe
        self._out[v][u] = newe
        return newe

    def incident_edges(self,v):
        return self._out[v].values() #edges of v
    def verticies(self):
        return self._out.keys()
    def get_edge(self,u,v):
        return self._out[u][v]
    def edges(self):
        S = Set()#fixes duplicates of each edge
        for v in self.verticies():
            S.add(self.incident_edges(v))
        return S

    def degree(self,v):
        #num of edges out of vertex
        pass
    def edge_count(self,v):
        total = sum(len(self._from[v])
        pass
    def vertex_count(self):
        #size of main dictionary
        pass


#DEPTH FIRST
def reachfrom(G,v,rv=None): #take graph and vertex, return list where you can reach
    ''' #rv as a list is a waste of time
    if rv == None:
        rv = []

    if not v in rv: #base
        rv.append(v)
        for e in G.incident_edges(v): #returns edges of v
            G.reachfrom(G,e.opposite(v),rv)
    '''
    if rv == None:
        rv = {v:None} #add yourself, no steps

    for e in G.incident_edges(e):
        dv = e.opposite(v)
        if not dv in rv:
            rv[dv] = v
            reachfrom(G,dv,rv)
    return rv

def _getpath(v,rv):
    p = []
    while v:
        p.append(v)
        v = rv[v]
    return p

def pathfromto(G,u,v):
    rv = reachfrom(G,u)
    path = _getpath(v,rv)
    return reversed(path)


#BREDTH FIRST
def BFS(G,v,rv=None): #shortest path rv
    if rv == None:
        rv = {v:None}

    g = [v] #group
    ng = [] #next group
    while g:
        for v in g:
            for e in G.incident_edges(v):
                dv = e.opposite(v)
                if not dv in rv:
                    ng.append(dv)
                    rv[dv] = v
        g = ng
        ng = []
    return rv

def shortpathfromto(G,u,v):
    rv = BFS(G,u)
    path = _getpath(v,rv)
    return reversed(path)


def getMap(file):
    """This loads the map and returns a pair (V,E)
    V contains the coordinates of the veritcies
    E contains pairs of coordinates of the verticies"""
    G=open(file)
    root = etree.parse(G).getroot()
    v={}
    for child in root:
        if (child.tag=="node"):
            v[child.attrib["id"]]=(float(child.attrib["lon"]),float(child.attrib["lat"]))
    e=[]
    for child in root:
        if (child.tag=="way"):
            a=[]
            for gc in child:
                if gc.tag=="nd":
                    a.append(v[gc.attrib["ref"]])
            for i in range(len(a)-1):
                e.append((a[i],a[i+1]))
    return list(v.values()),e

class Map():
    def __init__(self, data):
        self._graph = Graph()
        for i in data[0]:
            self._graph.add_vertex(i)        
        for i in data[1]:
            try:
                self._graph.add_edge(i[0],i[1])
                print("works")
            except KeyError:
                pass
        
        
#If you call it with
(V,E)=getMap("map.osm")
print(V[0])
print(E[0])

M = Map((V,E))
#print(M._graph._out)