'''
Created on Feb 21, 2013

@author: jeremiahoconnor
'''
import math
import sys
class puzzleState():
    
    def __init__(self, width, state, par_ind=-1, parent=None, g_value=0):
        self.state=state
        self.width=width
        self.parent=parent
        self.g_value=g_value
        self.parent_move= par_ind
    
    def get_parent(self):
        return self.parent
    
    def get_state(self):
        return self.state
    
    def get_width(self):
        return self.width
    
    def get_g_value(self):
        return self.g_value
    
    def get_zero_index(self):
        return self.state.index(0)
    
    def is_Goal(self):
        return range(len(self.state)) == self.state
    
    def __eq__(self,other): 
        if (self.state== other.state):
            return True
        else:
            return False
        
    def __hash__(self):
        return hash(tuple(self.state))
    
    #heuristic function
    def h(self, heuristicTable):
        sum=0
        for i, tile in enumerate(self.state):
            sum+= heuristicTable[tile][i]
        return sum
            
    #check if the 0 tile is a corner tile
    def isCornerTile(self, tileInd, width, puzzle):
        #top right
        if (tileInd==0):
            return True
        #top left
        if (tileInd==(0+width-1)):
            return True
        #bottom right
        if (tileInd== (len(puzzle)-1)):
            return True
        #bottom left
        if (tileInd== ((len(puzzle))-(width))):
            return True
        return False
    
    #boolean check if 0 is side tile
    def isSideTile(self, tileInd, width, puzzle):
        if (not (self.isCornerTile(tileInd, width, puzzle))):
            if (tileInd%width==0):
                return True
            if ((tileInd-(width-1))%width==0):
                return True
            if ((tileInd>0) and (tileInd < width-1)):
                return True
            if tileInd<len(puzzle)-1 and tileInd > len(puzzle)-width:
                return True
        return False
    
    #boolean check if 0 is center tile
    def isCenterTile(self, tileInd, width, puzzle):
        if (not (self.isCornerTile(tileInd, width, puzzle)) and not (self.isSideTile(tileInd, width, puzzle))):
            return True
        return False
    
    #get move index list
    def get_move_ind_list(self):
        moveList=[]
        if self.isCornerTile(self.get_zero_index(), self.get_width(), self.get_state()):
            if (self.get_zero_index()==0):
                #left corner
                moveList.append(self.get_zero_index()+1)
                moveList.append(self.get_zero_index()+self.get_width())
                #right corner
            if (self.get_zero_index()==(self.get_width()-1)):
                moveList.append(self.get_zero_index()-1)
                moveList.append(self.get_zero_index()+self.get_width())
                
            if (self.get_zero_index() == ((len(self.get_state()))-(self.get_width()))):
                #bottom left
                moveList.append(self.get_zero_index() + 1)
                moveList.append(self.get_zero_index()-self.get_width())
                
            if (self.get_zero_index()== (len(self.get_state())-1)):
                #bottom right
                moveList.append(self.get_zero_index()-1)
                moveList.append(self.get_zero_index()-self.get_width())
                
        if self.isSideTile (self.get_zero_index(), self.get_width(), self.get_state()):
            
                #side tile left side
            if (self.get_zero_index() % self.get_width()==0):
                #up
                moveList.append(self.get_zero_index()-self.get_width())
                #right
                moveList.append(self.get_zero_index()+1)
                #down
                moveList.append(self.get_zero_index()+self.get_width())
                
                #side tile right side
            if ((self.get_zero_index()-(self.get_width()-1)) % self.get_width()==0):
                #up
                moveList.append(self.get_zero_index()-self.get_width())
                #left
                moveList.append(self.get_zero_index()-1)
                #down
                moveList.append(self.get_zero_index()+self.get_width())
             
                #side tile top side
            if(self.get_zero_index() > 0 and self.get_zero_index() < self.get_width() -1):
                #down
                moveList.append(self.get_zero_index() + self.get_width())
                #left
                moveList.append(self.get_zero_index()-1)
                #right
                moveList.append(self.get_zero_index()+1)
            
                #side tile bottom side
            if (self.get_zero_index() < len(self.get_state())-1 and self.get_zero_index() > len(self.get_state())-self.get_width()):
                #up 
                moveList.append(self.get_zero_index()-self.get_width())
                #left
                moveList.append(self.get_zero_index()-1)
                #right
                moveList.append(self.get_zero_index()+1)
        
        if self.isCenterTile(self.get_zero_index(), self.get_width(), self.get_state()):
            #right
            moveList.append(self.get_zero_index()+1)
            #left
            moveList.append(self.get_zero_index()-1)
            #up
            moveList.append(self.get_zero_index()-self.get_width())
            #down
            moveList.append(self.get_zero_index()+self.get_width())
        return moveList
    
    #make move
    def takeMove(self, moves_list):
        moves_list= []
        moves= self.get_move_ind_list()
        for move in moves:
            currState= self.get_state()[:]
            puzzle=puzzleState(self.get_width(), currState , self.get_state()[move], self, g_value= self.g_value+1)
            puzzle.get_state()[self.get_zero_index()], puzzle.get_state()[move]= puzzle.get_state()[move], puzzle.get_state()[self.get_zero_index()]
            puzzle.parent= self
            puzzle.parent_move=self.get_state()[move]
            moves_list.append(puzzle)
        return moves_list

#build manhattan table
def manhattanTable(w,h):
    manhattan_val_list= []
    row_col= w*h
    for i in range(row_col):
        new_l=[]
        for j in range (row_col):
            if (i==0):
                new_l.append(0)
            else:
                calc_init_row= j/w
                calc_goal_row= i/w
                calc_init_col= j%w
                calc_goal_col= i%w
                row_diff= math.fabs(calc_init_row-calc_goal_row)
                col_diff= math.fabs(calc_init_col- calc_goal_col)
                new_l.append(row_diff+col_diff)
        manhattan_val_list.append(new_l)
    return manhattan_val_list

#uniform cost search
def ucs(w,h,pieces):
    return best_first(w,h,pieces)

#astar search
def astar(w, h, pieces):
    heuristicTable= manhattanTable(w,h)
    #greedy and h are the same output, no g_value
    return best_first(w, h, pieces, lambda state: state.g_value + state.h(heuristicTable))

#greedy search
def greedy(w, h, pieces):
    heuristicTable= manhattanTable(w,h)
    return best_first(w, h, pieces, lambda state: state.h(heuristicTable))

#best-first search, bulk function for ucs, astar, greedy functions
def best_first (w, h, pieces, func=None):
    puzzle= puzzleState(w, pieces, None, None)
    closed_list= set()
    open_list = []
    open_set= set()
    open_list.append(puzzle)
    open_set.add(puzzle)
    node=None
    solution_list=[]
    move_generator_list= []
    success= False
    while open_list:
        if (success):
            break
        if len(open_list)==0:
            return False
        #ucs
        if func is None:
            node= open_list.pop(0)
            open_set.remove(node)
        #astar, greedy
        else:
            #turn queue into priority queue
            node= sorted(open_list, key=func)[0]
            open_list.remove(node)
            open_set.remove(node)
        #print node.get_state()
        closed_list.add(node)
        move_generator_list+= (node.get_move_ind_list())
        for move in node.takeMove(node.get_move_ind_list()):
            if move not in open_set and move not in closed_list:
                
                if move.is_Goal():
                    node= move
                    success= True
                    break;
                open_list.append(move)
                open_set.add(move)
    #build move list
    while node.parent!=None:
        solution_list.append(node.parent_move)
        node = node.parent
        
    tot_num_states_expanded= len(closed_list)
    tot_num_states_generated= len(move_generator_list)
    num_of_moves= len(solution_list)
    solution_list.reverse()
    return (tot_num_states_expanded, tot_num_states_generated), num_of_moves,  solution_list

#bulk function depth_limit 
def dls (init, limit, func=None):
    open_list= []
    open_set= set()
    #closed_list= []
    closed_dict= {}
    #closed_set= set()
    node=None
    move_array= []
    move_l=[]
    success= False
    open_list.append(init)
    open_set.add(init)
    closed_len= 0
    min_limit= sys.maxint
    while open_list:
        if (success):
            break
        node= open_list.pop()
        open_set.discard(node)
        if node.is_Goal():
            return node
            
        else:
            #closed_list.append(node)
            #closed_set.add(node)
            closed_dict[node]= node.g_value
  
            if (func(node) <= limit):
                move_l+= (node.get_move_ind_list())
                for move in node.takeMove(node.get_move_ind_list()):
                    if move not in open_set and move not in closed_dict:
                        if move.is_Goal():
                            node= move
                            success= True
                            while node.parent!=None:
                                move_array.append(node.parent_move)
                                node = node.parent
                            #closed_len= len(closed_list)
                            closed_len= len(closed_dict)
                            move_array.reverse()
                            return ((closed_len, len(move_l)), len(move_array),  move_array), min_limit
                        open_list.insert(0, move)
                        open_set.add(move)
                    
                    else:
                        #if move in closed_set:
                        if move in closed_dict:
                            #close_move= closed_list[closed_list.index(move)]
                            close_move_g = closed_dict.get(move)
                            if close_move_g > move.g_value:
                                #closed_list.remove(close_move);
                                del closed_dict[move]
                                #closed_set.remove(close_move)
                                open_list.append(move)
                                open_set.add(move)
            else:
             
                if (func(node)< min_limit):
                    min_limit= func(node)
                continue
    #otherwise no solution
    
    return ((closed_len, len(move_l)), len(move_array),  None), min_limit

#iterative deepening
def ids (w, h, pieces):
    tupList=[]
    puzzle= puzzleState(w, pieces, None, None)
    depth= 0
    while True:
        result= dls(puzzle, depth, lambda state: state.g_value)
        tupList.append(result[0][0])
        if (result[0][2]==None):
            #increase the depth
            depth= depth+1
        else:
            
            return (tupList,result[0][1], result[0][2])

#iterative deepening astar
def idastar(w, h, pieces):
    tupList= []
    puzzle= puzzleState(w, pieces, None, None)
    heuristicTable= manhattanTable(w,h)
    depth= puzzle.h(heuristicTable)
    while True:
      
        result= dls(puzzle, depth, lambda state: state.g_value + state.h(heuristicTable))
        tupList.append(result[0][0])
        if result[0][2]==None:
            depth= result[1]
            continue
        #tupList.append(result[0])
        return  (tupList,result[0][1], result[0][2])
        
def main():

    print "ucs: ", ucs(3,3,[3,5,1,6,8,4,7,0,2])
#    ((2420, 6698), 13, [8, 4, 2, 8, 4, 5, 1, 2, 5, 4, 7, 6, 3])
    
    print "ids: ", ids(3,3,[1,3,2,5,4,6,7,8,0])
#    ([(1, 3), (4, 11), (12, 35), (36, 99), (100, 291), (292, 803), (804, 2339), (1048, 2876)], 7, [5, 8, 7, 6, 3, 4, 1])    
    print "astar: ", astar(4,4,[7,6,5,4,3,2,1,0,8,9,10,11,12,13,14,15])
    
    #print "ids", ids(3,3,[1,3,2,5,4,6,7,8,0])
    #print "idastar", idastar(4,4,[7,6,5,4,3,2,1,0,8,9,10,11,12,13,14,15])
    #((1296, 3979), 28, [1, 2, 3, 7, 6, 5, 4, 1, 2, 3, 7, 6, 5, 4, 1, 2, 3, 7, 6, 5, 4, 1, 2, 3, 7, 6, 5, 4])

    #print "idastar", idastar(4,4,[7,6,5,4,3,2,1,0,8,9,10,11,12,13,14,15])
#    ([(5, 2), (230, 82), (4376, 1545), (65718, 23093), (250366, 88130)], 28, [1, 2, 3, 7, 6, 5, 4, 1, 2, 3, 7, 6, 5, 4, 1, 2, 3, 7, 6, 5, 4, 1, 2, 3, 7, 6, 5, 4])
    

    
    #20
    print "ucs: ", ucs(3,3,[1,3,2,5,4,6,7,8,0])
    print "greedy: ", greedy(3,3,[1,3,2,5,4,6,7,8,0])
    print "astar: ", astar(3,3,[1,3,2,5,4,6,7,8,0])
    print "ids: ", ids(3,3,[1,3,2,5,4,6,7,8,0])
    print "idastar: ", idastar(3,3,[1,3,2,5,4,6,7,8,0])
                               
    #8
#    print "Big Cases: "
#    print "ucs: ", ucs(3,3,[1,3,2,5,4,6,7,8,0])
#    print "greedy: ", greedy(3,3,[1,2,5,4,0,8,3,6,7])
#    print "astar: ", astar(3,3,[1,2,5,4,0,8,3,6,7])
#    print "ids: ", ids(3,3,[1,2,5,4,0,8,3,6,7])
#    print "idastar: ", idastar(3,3,[1,2,5,4,0,8,3,6,7])

    #28
#    print "ucs: ", ucs(4,4,[7,6,5,4,3,2,1,0,8,9,10,11,12,13,14,15])
#    print "greedy: ", greedy(4,4,[7,6,5,4,3,2,1,0,8,9,10,11,12,13,14,15])
#    print "astar: ", astar(4,4,[7,6,5,4,3,2,1,0,8,9,10,11,12,13,14,15])
#    print "ids: ", ids(4,4,[7,6,5,4,3,2,1,0,8,9,10,11,12,13,14,15])
    #print "idastar: ", idastar(4,4,[7,6,5,4,3,2,1,0,8,9,10,11,12,13,14,15])
    
    #15
#    print "ucs: ", ucs(3,2,[5,4,3,2,1,0])
#    print "greedy: ", greedy(3,2,[5,4,3,2,1,0])
#    print "astar: ", astar(3,2,[5,4,3,2,1,0])
#    print "ids: ", ids(3,2,[5,4,3,2,1,0])
#    print "idastar: ", idastar(3,2,[5,4,3,2,1,0])
    
    
    
#    print "ucs: ", ucs(3,3,[3,5,1,6,8,4,7,0,2])
#    print "greedy", greedy(2,2,[3,2,1,0])
##    print "greedy: ", greedy(3,3,[3,5,1,6,8,4,7,0,2])
##    print "astar: ", astar(2,2,[3,2,1,0])
#    print "astar: ", astar(3,3,[1,2,5,4,0,8,3,6,7])
#    print "ids: ", ids(3,3,[1,4,2,6,3,0,7,8,5])
#    print "idastar", idastar(2,2,[3,2,1,0])
#    print "idastar", idastar(3,3,[1,4,2,6,3,0,7,8,5])
#    print "idastar", ids(4,4,[7,6,5,4,3,2,1,0,8,9,10,11,12,13,14,15])
    
if __name__ == '__main__': main()

    
    