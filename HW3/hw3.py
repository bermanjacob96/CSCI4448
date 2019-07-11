class Store():
    def __init__(self):
        self._inventory=[]
        self._activeRentals=[]
        self._completeRentals=[]
        self._totalIncome=0
    
    def generate_inventory(self,categoryPrices,numTools):
        '''Generate a random selection of tools in the provided categories with the specified price'''
        for i in range(0,numTools):
            categories=list(categoryPrices.keys())
            randCat=categories[randint(0,len(categories)-1)]
            self._inventory.append(Tool(randCat+" "+str(i),randCat, categoryPrices[randCat]))


    def return_rentals(self,day):
        '''Process rental returns that are due back today. Return tools to inventory. '''
        for rental in list(self._activeRentals):
            if rental.check_due(day):
                rental.returned_by_tool_elves()
                self._inventory+=rental.get_tools()
                self._completeRentals.append(rental)
                self._activeRentals.remove(rental)
                
    def add_rental(self,rental):
        '''Take new rental record and file it in active rentals and take payment. '''
        self._activeRentals.append(rental)
        self._totalIncome+=rental.get_total()

    def get_inventory_count(self):
        ''' Return number of tools in inventory. '''
        return len(self._inventory)

    def get_some_tools(self,numberTools):
        ''' Randomly select the requested number of tools from inventory and return them. '''
        tools=[]
        i=0
        while i < numberTools and len(self._inventory)>0:
            index=randint(0,len(self._inventory)-1)
            tools.append(self._inventory.pop(index))
            i+=1
        return tools
    
    def print_results(self):
        '''Print Inventory, Financial and Rental Records. '''
        print("{} tools in invetory.\n".format(self.get_inventory_count()))
        print("Tool Inventory".center(68)+"\n")
        tools= [tool.get_name() for tool in self._inventory]
        print (tools)
        print("Total Income: {}".format(self._totalIncome))
        print("Active Rentals".center(68)+"\n")
        for rental in self._activeRentals:
            print(rental)
        print("Completed Rentals".center(68)+"\n")
        tempSorted=sorted(self._completeRentals,key=lambda x: x.get_start_date(),reverse=False)
        for rental in tempSorted:
            print(rental)