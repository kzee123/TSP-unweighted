import random
from random import randint
from math import floor
graph1 = {
    "quetta":["sariab","ziarat","dikhan","zhob","karachi", "lahore","pindi"],
    "sariab":["quetta","ziarat","dikhan","zhob","karachi", "lahore","pindi"],
    "ziarat":["quetta","sariab","dikhan","zhob","karachi", "lahore","pindi"],
    "zhob":["quetta","sariab","ziarat","dikhan","karachi","lahore","pindi"],
    "dikhan":["quetta","sariab","ziarat","zhob","karachi","lahore","pindi"],
    "karachi":["quetta","sariab","ziarat","zhob","dikhan","lahore","pindi"],
    "lahore":["quetta","sariab","ziarat","zhob","dikhan","karachi","pindi"],
    "pindi":["quetta","lahore","sariab","ziarat","zhob","dikhan","karachi"]
}
# a sample graph

class MyQUEUE: # just an implementation of a queue

    def __init__(self):
        self.holder = []

    def enqueue(self,val):
        self.holder.append(val)

    def dequeue(self):
        val = None
        try:
            val = self.holder[0]
            if len(self.holder) == 1:
                self.holder = []
            else:
                self.holder = self.holder[1:]   
        except:
            pass

        return val  

    def IsEmpty(self):
        result = False
        if len(self.holder) == 0:
            result = True
        return result


path_queue = MyQUEUE() # now we make a queue


def BFS(graph,start,end,q):

    temp_path = [start]

    q.enqueue(temp_path)
    path = []
    while q.IsEmpty() == False:
        tmp_path = q.dequeue()
        last_node = tmp_path[len(tmp_path)-1]
        #print (tmp_path)
        if last_node == end:
            path.append(tmp_path)
        for link_node in graph[last_node]:
            if link_node not in tmp_path:
                #new_path = []
                new_path = tmp_path + [link_node]
                q.enqueue(new_path)
    return path
#goal state = the list containing the path should have all the citiesand all the cities are being explored without any repetition
#fitness is represented by number of cities in chromosomes, in the start of the algorithm, the chromosome has 0 cities so it's fitness value is 0



def chkelements(list1):
    for i in goal:
        if i not in list1:
            list1.insert(2,i)
    return list1



def mutate(list1,x):
    copy = list1[x:len(graph1)-1]
    random.shuffle(copy)
    list1[x:len(graph1)-1] = copy
    return list1

goal = ["quetta","sariab","ziarat","dikhan","zhob","karachi","pindi","lahore"]
def gentsp(graph):
    path = BFS(graph,"quetta","lahore",path_queue)

    all_path = []
    for i in path:
        if len(i) == len(goal):
            all_path.append(i)
    #print(all_path)
    pi =  random.choice(all_path)
    test = all_path

    test.remove(pi)

    pj = random.choice(test)
    print("Parents:")
    print(pi)
    print(pj)

    print("Start")
    
    c1 = []
    c2 = []
    while 1:
        
        #print("all paths:")
        #for i in all_path:
            #print (i)
        #print("parents: ")


        

        len1 = floor(len(pi)/2)

        x = 0

        while x<len1:
            c1.append(pi[x])
            x+=1

        len2 = floor(len(pj)/2)

        x = len2
        while x<len(pj):
            c1.append(pj[x])
            x+=1

        len3 = floor(len(pj)/2)

        x = 0

        while x<len3:
            c2.append(pj[x])
            x+=1

        x = floor(len(pi)/2)

        while x<len(pi):
            c2.append(pi[x])
            x+=1
        #print("/n")
        c1 = list(dict.fromkeys(c1))
        c2 = list(dict.fromkeys(c2))
        #print(" ")
        #print("Childs:")
        #print(c1)
        #print(c2)
        c1 = chkelements(c1)
        c2 = chkelements(c2)  
       


        if len(c1) == len(graph) and len(c2) == len(graph):
            print ("Childs")
            print(c1)
            print(c2)
            x = 1
            y = 1
            while 1:
                if c1[x] == goal[x]:
                    print( x, "Mutation to c1")
                    x+=1
                if c2[y] == goal[y]:
                    print( y, "Mutation to c2")
                    y+=1
               
                c1 = mutate(c1,x)
                c2 = mutate(c2,y)
                if c1 == goal or c2 == goal:
                    print ("completed")
                    print (c1)
                    print (c2)
                    break
            break
        continue


path = BFS(graph1,"quetta","lahore",path_queue)
print("All paths : ")
for i in path:
   print (i)
gentsp(graph1)