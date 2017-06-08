import copy
import random
import xml.etree.ElementTree as etree

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

class Graph:
    class Vertex:
        __slots__ = '_element'
        def __init__(self, x):
            self._element = x
        def element(self):
            return self._element
        def __hash__(self): # will allow vertex to be a map/set key 
            return hash(id(self))
        
    class Edge:
        __slots__ = '_origin' , '_destination' , '_element'
        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x
        def endpoints(self):
            return (self._origin, self._destination)
        def opposite(self, v):
            return self._destination if v is self. origin else self. origin
        def element(self):
            return self._element
        def __hash__(self): # will allow edge to be a map/set key 
            return hash((self._origin, self._destination))
    
    def __init__(self, directed = False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing
        
    def is_directed(self):
        return self._incoming is not self._outgoing
    
    def vertex_count(self):
        return len(self._outgoing)
        
    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        # for undirected graphs, make sure not to double-count edges 
        return total if self.is_directed() else total // 2
    
    def edges(self):
        result = set() # avoid double-reporting edges of undirected graph 
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values()) # add edges to resulting set 
        return result
    
    def get_edge(self, u, v):
        return self._outgoing[u].get(v)
    
    def degree(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge
    
    def insert_vertex(self, x=None): 
        v = self.Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {} 
        return v

    def insert_edge(self, u, v, x=None):
        e = self.Edge(u, v, x)
        #print(type(self._outgoing[u]))
        self._outgoing[u][v] = e
        self._incoming[v][u] = e
    
class Map:
    def __init__(self):
        (V,E) = getMap("map.osm")
        self._graph = Graph()
        self._color = {}
        self._small = None
        self._smallest = 3000
        temp = {}
        for i in V:
            temp[i] = self._graph.insert_vertex(i)
        for i in E:
            self._graph.insert_edge(temp[i[0]], temp[i[1]])
        
        #print(self._graph.vertex_count())
        #print(self._graph.edge_count())
        
    def draw(self):
        global pos
        #print(pos)
        scale(float(width)/(maxlon-minlon),float(height)/(maxlat-minlat))
        translate(-minlon,-minlat)
        strokeWeight(0.00001)
        stroke(0,0,0)
        background(255)
        for i in self._graph.edges():
            edge1 = i.endpoints()[0].element()
            edge2 = i.endpoints()[1].element()
            #redc = random.randint(0,255)
            #bluec = random.randint(0,255)
            stroke(0,0,0)
            line(edge1[0],edge1[1],edge2[0],edge2[1])
            
            #print(edge1[0],edge1[1],edge2[0],edge2[1])
            if pos:
                distance1 = dist(pos[0],pos[1],edge1[0],edge1[1])
                distance2 = dist(pos[0],pos[1],edge2[0],edge2[1])
                if distance1 < self._smallest or distance2 < self._smallest:
                    self._small = i
                    self._smallest = distance1 if distance1 < distance2 else distance2

                
        if pos:
            strokeWeight(.0001)
            stroke(0,255,0)
            edge1 = self._small.endpoints()[0].element()
            edge2 = self._small.endpoints()[1].element()
            line(edge1[0],edge1[1],edge2[0],edge2[1])
            x = BFS(self._graph,self._small)
            for i in range(len(x)):
                stroke(255-i,0,i)
                line()
            
            self._smallest = 3000
            
            #print(x)
    
    
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

def mouseClicked():
    global pos
    pos = mouseToScreen(mouseX,mouseY)
    #print(pos)
    
def mouseToScreen(mx,my):
    return (minlon+(mx/float(width))*(maxlon-minlon),
        minlat+(my/float(height))*(maxlat-minlat))

def setup():
    global pos
    size(1000,700)
    global M
    global maxlat
    global minlat
    global maxlon
    global minlon
    maxlat=40.6903
    minlat=40.7061
    maxlon=-73.9728
    minlon=-74.0065
    pos = None
    M = Map()
    
def draw():
    M.draw()
        
    

        



        
