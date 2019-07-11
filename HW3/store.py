from random import seed, shuffle, randint
class Store():
    def __init__(self):
        self.inventory=[]
        self.rentedTools=[]
        self.returnedTools=[]
        self.profit=0
    
    def genInventory(self,categoryPrices,numTools):
        for i in range(0,numTools):
            categories=list(categoryPrices.keys())
            randCat=categories[randint(0,len(categories)-1)]
            self.inventory.append(Tool(randCat+" "+str(i),randCat, categoryPrices[randCat]))


    def returns(self,day):
        for rental in list(self.rentedTools):
            if rental.due(day):
                rental.returnedBy()
                self.inventory+=rental.getTools()
                self.returnedTools.append(rental)
                self.rentedTools.remove(rental)
                
    def addRental(self,rental):
        self.rentedTools.append(rental)
        self.profit+=rental.getTotal()

    def numTools(self):
        return len(self.inventory)

    def getTools(self,numberTools):
        tools=[]
        i=0
        while i < numberTools and len(self.inventory)>0:
            index=randint(0,len(self.inventory)-1)
            tools.append(self.inventory.pop(index))
            i+=1
        return tools
    
    def results(self):
        print("{} tools in invetory.\n".format(self.numTools()))
        print("Tool Inventory".center(68)+"\n")
        tools= [tool.getName() for tool in self.inventory]
        print (tools)
        print("Total Income: {}".format(self.profit))
        print("Active Rentals".center(68)+"\n")
        for rental in self.rentedTools:
            print(rental)
        print("Completed Rentals".center(68)+"\n")
        tempSorted=sorted(self.returnedTools,key=lambda x: x.getStartDate(),reverse=False)
        for rental in tempSorted:
            print(rental)
        

class Rent ():
    def __init__(self):
        pass
    def rent (self, customer, store, day):
        raise NotImplementedError

class BusinessRent (Rent):
    def rent(self, customer, store, day):
        tempRental=Rental(store.getTools(3),day,7,customer)
        store.addRental(tempRental)
        customer.addRental(tempRental)

class CasualRent (Rent):
    def __init__(self):
        self.timeMin=1
        self.timeMax=2
        self.toolMin=1
        self.toolMax=2
    def rent (self, customer, store, day):
        duration=randint(self.timeMin,self.timeMax)
        toolCount=randint(self.toolMin,self.toolMax)
        toolCount=min(toolCount,3-customer.getNumoTools())
        tempRental=Rental(store.getTools(toolCount),day,duration,customer)
        store.addRental(tempRental)
        customer.addRental(tempRental)
    
class RegularRent (CasualRent):
    def __init__(self):
        self.timeMin=3
        self.timeMax=5
        self.toolMin=1
        self.toolMax=3

class Tool ():
    def __init__(self,name,category,price):
        self.name=str(name)
        self.price=price
        self.typeoTool=str(category)
    def getPrice(self):
        return self.price
    def getName(self):
        return self.name
    def __str__(self):
        return self.typeoTool.ljust(20)+self.name.ljust(20)+(str(self.price)+".00").rjust(10)

class Customer ():
    def __init__(self,name,rentalType):
        self.rentals=[]
        self.totalTools=0
        self.name=name
        self.nextProject=randint(0,10)
        self.typeoRental=rentalType
    def addRental (self, rental):
        self.rentals.append(rental)
        self.totalTools+=rental.getNumoTool()
    def removeRental (self, rental):
        self.totalTools-=rental.getNumoTool()
        self.rentals.remove(rental)
    def rent(self,store,day):
        self.typeoRental.rent(self,store,day)
    def checkInventory(self,store, day):
        return day==self.nextProject and store.numTools()>0 and self.totalTools<3
    def setNextProject(self,day):
        self.nextProject=day+randint(0,4)
    def visit(self,store,day):
        self.typeoRental.rent(self,store,day)
        self.setNextProject(day)
    def getNumoTools(self):
        return self.totalTools
    def getName(self):
        return self.name
   
class BusinessCustomer (Customer):
    def checkInventory(self,store,day):
        return store.numTools() >=3 and day >= self.nextProject and self.totalTools==0
    def setNextProject(self,day):
        self.nextProject=day+randint(7,12)

        
class Rental ():
    def __init__(self, tools, day, duration, customer):
        self.tools=tools
        self.startDate=day
        self.duration=duration
        self.customer=customer
        self.total=0
        self.calcTotal()
        self.toolCount=len(tools)
    def returnedBy(self):
        self.customer.removeRental(self)
    def calcTotal(self):
        for tool in self.tools:
            self.total+=tool.getPrice()
        self.total=self.total*self.duration
    def due(self, date):
        return self.startDate+self.duration == date
    
    def getStartDate(self):
        return self.startDate

    def getTotal(self):
        return self.total

    def getTools(self):
        return self.tools
    
    def getNumoTool(self):
        return self.toolCount

    def __str__(self):
        result=" Rental ".center(68,"/")+"\n"
        result+="/ Name: {}".format(self.customer.getName()).ljust(36) + "Day: {}".format(self.startDate).center(30)+" /\n"
        result+="/"+"-"*66+"/\n"
        result+="/ Category".ljust(22)+"Tool".ljust(20)+"Rate".rjust(9)+"Days".center(6)+"SubTot".center(10)+"/\n"
        result+="/"+"-"*66+"/\n"
        for tool in self.tools:
            result+="# "+str(tool)+str(self.duration).center(5)+(str(self.duration*tool.getPrice())+".00").center(10)+"/\n"
        result+="/"+" "*66+"/\n"
        result+="/"+" "*46+"Total: ".rjust(10)+(str(self.total)+".00").ljust(10)+"/\n"
        result+="/"*68
        return result

class Simulator():
    def __init__(self):
        self.numoCustomer=10
        self.toolCount=20
        self.categoryPrices={"Painting":25, "Concrete":15, "Plumbing":30, "Woodwork":10, "Yardwork":12}
        self.customerTypes=["Business","Casual","Regular"]
        self.customers=[]
        self.store=None
        self.day=1
    
    def setCustomers(self):
        busRent=BusinessRent()
        regRent=RegularRent()
        casRent=CasualRent()
        for i in range(0,self.numoCustomer):
            randType=self.customerTypes[randint(0,2)]
            if randType == "Business":
                self.customers.append(BusinessCustomer("Customer "+str(i),busRent))
            elif randType == "Regular":
                self.customers.append(Customer("Customer "+str(i),regRent))
            elif randType == "Casual":
                self.customers.append(Customer("Customer "+str(i),casRent))
    
    def setStore(self):
        self.store=Store()
        self.store.genInventory(self.categoryPrices,self.toolCount)
    
    def running(self):
        self.store.returns(self.day)
        shuffle(self.customers)
        for customer in self.customers:
            if customer.checkInventory(self.store,self.day):
                customer.visit(self.store,self.day)
        self.day+=1
        
    def run(self):
        while self.day<=35:
            self.running()

    def results(self):
        self.store.results()


# Main
seed(13)
sim=Simulator()
sim.setCustomers()
sim.setStore()
sim.run()
sim.results()