class Tree():

    #for numchildren, use the len of children list
    def children(self,p):
        #node = self._validate_position(p)
        node = p._node
        for cn in node._children:
            #yield self._make_position(cn)
            yield self.Position(cn,self)

    
