class rental():
    def __init__(self,calculations=1):
        self.l={}
        self.calculations=calculations
    def runRoi(self):
        self.active=True
        while self.active:
            self.intro=input(
                "\nWould you like to start the calculation? ('Yes' or 'No')")
            if self.intro=="yes":
                print("Let's get started!")
                self.incomeZ()
            else:
                self.active=False
    def incomeZ(self):
        self.incomes=[]
        total=0
        income=int(input("How much will you be charging for rent a month?"))
        self.incomes.append(income)
        income=int(input("If you are charging for laundry, how much will you be bringing in a month?"))
        self.incomes.append(income)
        income=int(input("Is there any other income this unit will bring in?"))
        self.incomes.append(income)
        sum(self.incomes)
        self.expenseZ
    def expenseZ(self):
        self.expenses=[]
        total=0
        expense=int(input("How much taxes will you be paying a month?"))
        self.expenses.append(expense)
        expense=int(input("How much will you be paying for insurance a month?"))
        self.expenses.append(expense)
        expense=int(input("How much will you be paying in utilities a month?"))
        self.expenses.append(expense)
        expense=int(input("How much HOA fees will you be paying a month?"))
        self.expenses.append(expense)
        expense=int(input("How much are you spending in lawn care a month?"))
        self.expenses.append(expense)
        expense=int(input("How much are you setting aside a month in case of vacancy?(5% of month's rent)"))
        self.expenses.append(expense)
        expense=int(input("How much are you spending on repairs a month?"))
        self.expenses.append(expense)
        expense=int(input("How much a month are you setting aside on capital expenditures?"))
        self.expenses.append(expense)
        expense=int(input("How much a month are you spending on property management?(Should be 10% of rent)"))
        self.expenses.append(expense)
        expense=int(input("How much is your monthly mortgage?"))
        self.expenses.append(expense)
        sum(self.expenses)     
        self.cashflow
    def cashflow(self):
        return
    
    def cashAwncash(self):
        return
    
    def cROI(self):
        return