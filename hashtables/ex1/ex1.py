#from hashtable import (HashTable,
                        #put,
                        #delete,
                        #get,
                        #resize)





#def get_indices_of_item_weights(weights, length, limit):

    #"""
    #YOUR CODE HERE
    #"""
    #ht = HashTable(16)
    #for i in range(length):
        #y = get(ht, limit - weight[i])
        #if (y is not None):
            #return (i, y)
        #else:
            #put(ht, weights[i], i)
        #return None
    
    
#def print_answer(answer):
    #if answer is not None:
        #print(str(answer[0] + " " + answer[1]))
    #else:
        #print("None")
    

def get_indices_of_item_weights(weights, length, limit):
    
    ht = {}
# Enumerate
    for i, w in enumerate(weights):
        ht[w] = i
# Enumerate 
    for i, w in enumerate(weights):
        r = ht.get(limit - w, None)
        if r:
            return [ r, i ]
    return None