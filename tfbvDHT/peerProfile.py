class PeerProfile:
    '''
        Data structures:
        
        myAddress: tuple( getLocalIPAddress(), int(port) )

        fingerTable: { key = getHashIndex((getLocalIPAddress(), int(port))) : value = str(getLocalIPAddress():port), ... }

        successor: str( getLocalIPAddress() + ":" + port )
        successorTwo: str( getLocalIPAddress() + ":" + port )

    '''

    def __init__(self, _myAddr,_fingerTable, _successor, _successorTwo):
        self.fingerTable = _fingerTable
        self.successor = _successor
        self.successorTwo = _successorTwo
        self.myAddress = _myAddr
        self.locked = False

    def myAddrString(self):
        ''' Return my address in form (string: "ip:port"). '''

        return self.myAddress[0]+":"+str(self.myAddress[1])

    def serialize(self):
        ''' Return a string version of all details of the class. '''

        inf = ''
        inf += "Address: " + self.myAddrString() + "\n"

        for f in self.fingerTable:
                inf += str(f) + ": "
                inf += self.fingerTable[f] + "\n"

        inf += "Successor: " + self.successor + "\n"
        inf += "Successor2: " + self.successorTwo + "\n"
        return inf
