import sys  # Last Updated Feb 20, 12:07 pm (Final Submission)



order=3   # In each node maximum 3 keys can be inserted...

order=order-1  # added feb 18

headPtr=None # keeps track of startmost leaf node
prevPtr=None  # keeps track of last pointer assigned
nextPtr=None

class treeNode:
    def __init__(self):

        self.keyLst=[]    # maintains keys in a single node # values are mentioned  in a list
        self.valLst=[]
        self.leafNode=True
        self.parentPtr=None  # stores reference to parent node
        self.leafNext=None  # Pointer to next leaf node
        self.countLst=[] # list to keep track of duplicates  # Feb 18


    def splitNode(self):

        global order
        global headPtr
        global prevPtr
        global nextPtr

        # 2 cases: splitting of leaf node and splitting of internal node

        #print('Inside split node')

        pLst=self.keyLst
        pValLst=self.valLst

        lnode=treeNode()
        rnode=treeNode()

        lnode.parentPtr=self   # Assigns self as parent to left node
        rnode.parentPtr=self   # Assigns self as parent to right node

        ind=(order+1)//2   # ind=4/2 = 2

        if self.leafNode:  # splitting of leaf node
            lnode.keyLst=pLst[:ind]
            lnode.valLst=pValLst[:ind]

            lnode.countLst=self.countLst[:ind]   #Added Feb 19

            rnode.countLst=self.countLst[ind:]  # Added Feb 19


            rnode.keyLst=pLst[ind:]
            rnode.valLst=pValLst[ind:]

            if headPtr==self:
                nextPtr=headPtr.leafNext
                headPtr=lnode
                rnode.leafNext=nextPtr
            else:
                tp=headPtr

                while tp!=self:
                    prevPtr=tp
                    tp=tp.leafNext
                
                nextPtr=tp.leafNext
                prevPtr.leafNext=lnode
                rnode.leafNext=nextPtr
            
            

            lnode.leafNext=rnode  # Added Feb 15 11:20pm
        
        else:  # splitting of internal node

            lnode.keyLst=pLst[:ind]
            lnode.valLst=pValLst[:ind+1]

            rnode.keyLst=pLst[ind+1:]  # Added Feb 15, 3:54 pm
            rnode.valLst=pValLst[ind+1:]

            lnode.leafNode=False   # We need to explicitly set it since by default new node leads to setting this value as True
            rnode.leafNode=False

            
            '''
            for i in lnode.valLst:
                
                print(i.parentPtr.keyLst)
            

            for i in rnode.valLst:
                print(i.parentPtr.keyLst)
            '''

            
            for i in lnode.valLst:  # very important # 
                i.parentPtr=lnode
            

            for i in rnode.valLst:
                i.parentPtr=rnode
            



            
            
        
        self.keyLst=[pLst[ind]]
        self.valLst=[lnode,rnode]   # stores the left ptr and right node ptr references

        #print(self.valLst)

        self.leafNode=False

        return self
    

    def display(self, level):
       

        print('Level is ',level, str(self.keyLst))

        if self.leafNode!=True:
            for item in self.valLst:
                item.display(level+1)

        
    

class BPlusTree:
    def __init__(self):

        self.root=None
        self.temp=self.root
    
    def displayLeaf(self):
        global headPtr
        tp=headPtr

        while tp!=None:
            #print(tp.keyLst)
            tp=tp.leafNext
    
    def range(self,x,y):

        temp1=None
        temp2=None

        x=min(x,y)
        y=max(x,y)

        temp=self.root
        parent=None

        while(temp.leafNode!=True):
            parent=temp
            flag=0
            ls=temp.keyLst
            for i in range(0,len(ls)):
                if x<ls[i]:
                    #print(temp.valLst)
                    temp=temp.valLst[i]    # denotes left ptr  object
                    flag=1
                    break
            
            if flag==1:
                continue
            else:
                index=len(ls)-1
                temp=temp.valLst[i+1]
        
        temp1=temp   # temp1 is allocated
    

        temp=self.root
        parent=None

        while(temp.leafNode!=True):
            parent=temp
            flag=0
            ls=temp.keyLst
            for i in range(0,len(ls)):
                if y<ls[i]:
                    
                    temp=temp.valLst[i]    # denotes left ptr  object
                    flag=1
                    break
            
            if flag==1:
                continue
            else:
                index=len(ls)-1
                temp=temp.valLst[i+1]
        
        temp2=temp  # temp2 is allocated

        tp1=temp1
        countVal=0

        while(tp1!=temp2):
            for k in tp1.keyLst:
                if k>=x:
                    #countVal+=1
                    countVal+=tp1.countLst[tp1.keyLst.index(k)]
            tp1=tp1.leafNext
        
        
        for k in temp2.keyLst:
            if k>=x and k<=y:
                #countVal+=1
                countVal+=temp2.countLst[temp2.keyLst.index(k)]
        
        #print(countVal)  # Prints the count of values within the range
        return countVal


        




    def find(self,val):  #Added Feb 16
        temp=self.root
        parent=None

        while(temp.leafNode!=True):
            parent=temp
            flag=0
            ls=temp.keyLst
            for i in range(0,len(ls)):
                if val<ls[i]:
                    
                    temp=temp.valLst[i]    # denotes left ptr  object
                    flag=1
                    break
            
            if flag==1:
                continue
            else:
                index=len(ls)-1
                temp=temp.valLst[i+1]
        
        if val in temp.keyLst:
            #print('YES')
            return 'YES'
        else:
            #print('NO')
            return 'NO'
    

    def count(self,val):   # for count function
        temp=self.root
        parent=None

        countVal=0

        while(temp.leafNode!=True):
            parent=temp
            flag=0
            ls=temp.keyLst
            for i in range(0,len(ls)):
                if val<ls[i]:
                    #print(temp.valLst)
                    temp=temp.valLst[i]    # denotes left ptr  object
                    flag=1
                    break
            
            if flag==1:
                continue
            else:
                index=len(ls)-1
                temp=temp.valLst[i+1]
        
        if val in temp.keyLst:
            for x in temp.keyLst:
                if x==val:
                    countVal=temp.countLst[temp.keyLst.index(x)]  # Added Feb 19
                    break
            #print(countVal)
            return countVal
        else:
            #print(countVal)
            return countVal

    

    def displayTree(self):
        self.root.display(0)
    
  

    def mergeNode(self,pnode,parent):

        global order

        parentLst=parent.keyLst
        p_item=pnode.keyLst[0]
        flag=0

        for i in range(0,len(parentLst)):
            if p_item<parentLst[i]:

                parent.keyLst=parent.keyLst[:i]+[p_item]+parent.keyLst[i:]

                if i==0:
                    parent.valLst=parent.valLst[:i]+pnode.valLst+parent.valLst[i+1:]
                else:
                    

                    parent.valLst.insert(i+1,pnode.valLst[1])  #Modified Feb 15
                    parent.valLst=parent.valLst[:i]+[pnode.valLst[0]]+parent.valLst[i+1:]   # valLst just stores the objects

                
                flag=1
                break

                    
                
        
        if flag==0:
            index=len(parent.valLst)-1
            parent.keyLst+=[p_item]
            parent.valLst[index]=pnode.valLst[0]
            parent.valLst.append(pnode.valLst[1])  # left and right pointer objects are assigned as required

        
        return parent
    

    def validateNodeOrder(self,node):   #node=temp -> denotes the leaf node at which insertion occurs and the parent of that leaf node already exists

        global order

        while True:
            parNode=node.parentPtr
            #print('parNode is',parNode)

            lst=node.keyLst
            #print(lst) 
        
            pnode=None

            if(len(lst)==order+1):   # condition for overflow
                pnode=node.splitNode()
                parNode=node.parentPtr
                

                if parNode==None:
                    
                    for i in pnode.valLst:
                        i.parentPtr=pnode
                    self.root=pnode
                    pnode.leafNode=False  #Added
                    break
                else:
                    node=self.mergeNode(pnode,parNode)   # returns merged node
                    for i in pnode.valLst:
                        i.parentPtr=node
                   
                    pnode.leafNode=False 
            
            else:
                break

        
       

    
    def insert(self,val):
        global order
        global headPtr
        parent=None


        if self.root==None:  # that is if no key already exists
            
            new_node=treeNode()
            self.root=new_node   # root node is assigned here
            self.root.keyLst.append(val)
            self.root.valLst.append(val)
            self.root.countLst.append(1)  # added Feb 19
            headPtr=self.root   # Added on FEb 16 to keep track of start most pointer
        
        else:  # If root node exists
            temp=self.root
            
            while(temp.leafNode!=True):
                parent=temp
                flag=0
                ls=temp.keyLst
                for i in range(0,len(ls)):
                    if val<ls[i]:
                        #print(temp.valLst)
                        temp=temp.valLst[i]    # denotes left ptr  object
                        flag=1
                        break
                
                if flag==1:
                    continue
                else:
                    index=len(ls)-1
                    temp=temp.valLst[i+1]  # returns right pointer 
            
            lst=temp.keyLst   # After obtaining the leaf node, we now can insert our key in the leaf node
            #print('val is',val)

            flag=0

            prFlag=0

            if val in lst:
                
                indexVal=lst.index(val)
              
                temp.countLst[indexVal]+=1  # count is incremented
                prFlag=1
            
            if prFlag==0:

                for i in range(0,len(lst)):    # inserting key in the leaf list
                    #print('Here',val)
                    if val<lst[i]:
                        temp.keyLst.insert(i,val)
                        temp.valLst.insert(i,val)
                        flag=1
                        #if prFlag==0:
                        temp.countLst.insert(i,1)
                        
                        break

                if flag==0:
                    #print('In here')
                    temp.keyLst.append(val)
                    temp.valLst.append(val)
                    temp.countLst.insert(i+1,1)
                


                if parent==None:   # Splitting and merging of leaf node
                    lst=temp.keyLst
                    pnode=None

                    if(len(lst)==order+1):   # condition for overflow
                        pnode=temp.splitNode()
                        for i in pnode.valLst:
                            i.parentPtr=pnode

                        self.root=pnode
                
                else:    #Splitting and merging of Internal node

                    self.validateNodeOrder(temp)  # temp is the leaf node at which insertion occurs
            
            
        
        






def processQuery(fname):

    bp_obj=BPlusTree()   # object is created

    fin=open(fname,'r')
    fout=open('output.txt','w')

    content=fin.readline()

    while(content!=''):

        content=content.replace('\n','')
        inputLs=content.split()

        if len(inputLs)==0:
            sys.exit('Program terminated.Blank line encountered')


        if inputLs[0].upper()=='INSERT':
            inp=int(inputLs[1])
            bp_obj.insert(inp)
        
        elif inputLs[0].upper()=='FIND':
            inp=int(inputLs[1])
            output_val=bp_obj.find(inp)
            fout.write(output_val+'\n')
        
        elif inputLs[0].upper()=='COUNT':
            inp=int(inputLs[1])
            output_val=bp_obj.count(inp)
            fout.write(str(output_val)+'\n')
        
        elif inputLs[0].upper()=='RANGE':
            #bp_obj.displayTree()
            #print('Leaf is')
            #bp_obj.displayLeaf()
            inp1=int(inputLs[1])
            inp2=int(inputLs[2])

            output_val=bp_obj.range(inp1,inp2)
            fout.write(str(output_val)+'\n')
        
        else:
            fout.write('Invalid operation entered\n')

        content=fin.readline()
    


    #bp_obj.displayTree() # added feb 20

    fin.close()
    fout.close()


        


if __name__ == '__main__':

    fname=sys.argv[1]
    processQuery(fname)
    
