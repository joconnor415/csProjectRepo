'''
Created on Feb 2, 2013

@author: jeremiahoconnor
'''
import cPickle as pickle
import sys
import re

### build graph: 
### takes as input a file in the form:
## a b dist time
### where a and b are destinations, dist is the distance between them, and 
### time is the time needed to travel between them and constructs a graph.

### This graph should be represented as an adjacency list, and stored as a 
### dictionary, with the key in the dictionary being the source, and
### the value being a list of edges with that source.  The graph should
### be undirected -- so that each edge (a,b) should appear in the adjecency
### list for a *and* the adjacency list for b.

class graph() :
    def __init__(self, infile=None) :
        self.adjlist = {}
        if infile :
            self.buildGraph(infile)

    ### method to print a graph.
    def __repr__(self) :
        return self.adjlist

    ### helper methods to construct edges and vertices. Use these in buildGraph.
    def createVertex(self, str) :
        name, lat,long = str.split(" ",2)
        lat = lat.split("=")[1]
        long = long.split("=")[1]
        return location(name, lat, long)

    def createEdges(self, str) :
        src, dest, dist, time = str.split(" ",4)
        dist=dist.split("=")[1]
        time=time.split("=")[1]
        e1 = edge(src,dest,dist, time)
        e2 = edge(dest,src,dist, time)
        return e1, e2

### method that takes as input a file name and constructs the graph described 
### above.
    def buildGraph(self, infile) :
        try:
            f= open(infile).readlines()
            vertLine= False
            edgeLine= False
            
            for line in f:
                if line.startswith("## vertices"):
                    vertLine=True
                    continue
                if line.startswith("## edges"):
                    vertLine=False
                    edgeLine=True
                    continue
                
                if vertLine:
                    v= self.createVertex(line)
                    self.adjlist[v]= []
                
                if edgeLine:
                    e= self.createEdges(line)
                    for v in self.adjlist.keys():
                        if (e[0].src== v.name):
                            self.adjlist[v].append(e[0]) 
                        if e[1].src== v.name:
                            self.adjlist[v].append(e[1])

        except(IOError), e:
            print "File not Found", e

### This method should compute Dijskta's algorithm.  It should return a 
### dictionary where the key is the destination vertex, and the value is
### a tuple consisting of the cost of the path an a list of vertices
### that make up the path from the source to the destination

    def dijkstra(self, start) :
        dist_dict={} #distance dictionary
        prev_dict= {} #previous dictionary
        vis_dict= {} #visited dictionary of boolean
        fringe=self.adjlist.copy()
        for v in self.adjlist.keys():
            dist_dict[v]= sys.maxint #dictionary of distance in kms
            prev_dict[v]= None #dictionary of previous nodes
            vis_dict[v]= False #boolean dictionary of visited nodes
        dist_dict[start] = 0
        
        while len(fringe) != 0:
            
            smallest=sys.maxint
            min_vert= None
            
            for key in dist_dict.keys():
                
                if dist_dict[key]<smallest and vis_dict[key] == False:
                    min_vert= key
                    smallest= dist_dict[key]
                    
            if (min_vert is None):
                break
            
            neigbor_list= fringe[min_vert]
        
            for neighbor in neigbor_list:
                
                distance= float(neighbor.distance.translate(None, "km"))
                
                if (distance + float(dist_dict[min_vert])) < float(dist_dict[location(neighbor.dest)]):

                    dist_dict[location(neighbor.dest)]= (distance + dist_dict[min_vert])
                    prev_dict[location(neighbor.dest)]= min_vert
           
            del fringe[min_vert]     
            vis_dict[min_vert]=True
        
        #construct the shortest path
        ret_dict= {}
        for neighbor in dist_dict.keys():
            target=neighbor
            l=[]
            while prev_dict:
                l.append(target)
                if target==start:
                    break
                target=prev_dict[target]
            l.reverse()
            ret_dict[neighbor]= "Length of Path: " + str(dist_dict[neighbor]), "Verticies that form Path: " + str(l)

        return ret_dict
    
### classes representing locations and edges

class location() :
    def __init__(self, name, lat=None, longitude=None) :
        self.name = name
        self.lat = lat
        self.longitude = longitude
    def __hash__(self) :
        return hash(self.name)
    def __eq__(self, other) :
        return self.name == other.name
    def __repr__(self) :
        return self.name
    

class edge() :
    def __init__(self, src, dest, distance, time) :
        self.src = src
        self.dest = dest
        self.distance = distance
        self.time = time

#--pfile=dijk_pick.txt -dijkstra=6 vert.txt
### usage: buildGraph {--pfile=outfile} {-p} infile
### if --pfile=outfile is provided, write a pickled version of the graph 
### to outfile. Otherwise, print it to standard output.

def main():
    arg_list= (sys.argv)
    outfile=""
    infile= arg_list[-1]
    gr= graph(infile)

    loc= ""
    for x in arg_list:
        if x.startswith("--pfile"):
            outfile= x[8:]
        if x.startswith("-dijkstra"):
            loc=x[10:] 
            ret_dict= gr.dijkstra(location(loc))
        
    if outfile!="":
        f2= open (outfile, 'w')
        pickle.dump(gr, f2)
        f2.close()
    else:
        print ret_dict
        

if __name__ == '__main__' : main()

