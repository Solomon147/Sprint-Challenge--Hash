#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    ht = {}
    #hashtable = ht[length]
    route = [None] * length
    
    """
    YOUR CODE HERE
    """
       # iterate over each ticket
    for ticket in tickets:
        # put the ticket.source as key - starting airport
        # put ticket.destination as the value - next airport
        ht[ticket.source] = ticket.destination
    # set the current_destination, to start off the list
    current_destination = ht["NONE"]
    # set an index
    i = 0
    while current_destination != "NONE":
        route[i] = current_destination
        current_destination = ht[current_destination]
        # move on to the next iteration
        i += 1
    route[i] = "NONE"
    print(ht)
    print(route)
    return route
