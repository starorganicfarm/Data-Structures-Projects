#!/usr/bin/env python
# coding: utf-8

# In[3]:


class PassengerList:
    def __init__(self):
        self.size=int(input("Enter Size of BUS: "))
        self.ary=[None]*self.size
        self.lst=[]
        self.keys=[]
        self.values=[]
        self.items=0
        
    def __hashed(self, k):
        return k % self.size
    
    def Search(self,k):
        if k:
            return (self.ary[(self.__hashed(k))])
        return (None)
    
    def Insert(self,k,v):
        n = 0
        pos = self.__hashed(k)
        self.lst.append(k)
        while(self.ary[pos]!= None):
            if  self.ary[pos] == None:
                break
            pos = (pos+1)%len(self.ary)
            n = n + 1
            if n == self.size:
                break 
        if n == self.size:
            print("xxx--BUS was full of passengers\nNo Place to insert this passenger--xxx\n")
        else:
            self.ary[pos]  = v

    def Delete(self, k):
        n=0
        pos = self.__hashed(k)
        while(n != self.size):
            if self.ary[pos] == None:
                break
            else:
                self.ary[pos] = None
                self.lst.remove(k)
                break
        if n == self.size:
            print("xxx--Passenger not found in the BUS--xxx")
            
    def Seats(self):
        for i in range(len(self.ary)):
            if self.ary[i]!=None:
                self.keys.append(i)
        return self.keys
    
    def Passengers(self):
        for i in self.ary:
            if i!=None:
                self.values.append(i)
        return self.values

    def Entries(self):
        a=self.Seats(),self.Passengers()
        lst=[]
        for i in range(len(self.lst)):
            x=(self.keys[i],self.values[i])
            lst.append(x)
        return lst

    def Size(self):
        size=[]
        for i in self.ary:
            if i!=None:
                size.append(i)
        return len(size)

    def IsEmpty(self):
        if self.ary == [None]*self.size:
            return True 
        return False
                 
    def Display(self):
        print("\n\033[1m" + "PASSENGER LIST" + "\033[0m")
        print("Seats\tPassengers")
        for i in range(self.size):
            print(i, "\t",self.ary[i])
        print("\n")
            

pl=PassengerList()
while(True):
    choice = int(input("Enter your choice!!!\n 1-> Insert\n 2-> Delete\n 3-> Display\n 4-> Searching\n 5-> Seats\n 6-> Passengers\n 7-> Size\n 8-> Entries\n 0-> Exit\n"))
    if choice == 0:
        print("\033[1m" + "Program Ended!!!" + "\033[0m")
        break
    elif choice == 1:
        k = int(input("Enter seat no.: "))
        v = str(input("Enter passenger name: "))
        pl.Insert(k,v)
    elif choice == 2:
        k = int(input("Enter seat no.: "))
        pl.Delete(k)
    elif choice == 3:
        pl.Display()
    elif choice == 4:
        k = int(input("Enter seat no.: "))
        print(pl.Search(k))
    elif choice == 5:
        print("Seats: ",pl.Seats())
    elif choice == 6:
        print("Passengers: ",pl.Passengers())
    elif choice == 7:
        print("Size: ",pl.Size())
    elif choice == 8:
        print("Entries: ",pl.Entries())
    else:
        print("xxx--Enter correct choice--xxx\n")

