class rental():
    def __init__(self,allincome=0, allexpenses=0, allinvestments=0):
        self.income=[]
        self.expenses=[]
        self.investment=[]
        self.allincome=allincome
        self.allexpenses=allexpenses
        self.allinvestments=allinvestments
        
        self.runRoi()
    def incomeZ(self):
        income=int(input("How much will you be charging for rent a month?"))
        self.income.append(income)
        income=int(input("If you are charging for laundry, how much will you be bringing in a month?"))
        self.income.append(income)
        income=int(input("Is there any other income this unit will bring in?"))
        self.income.append(income)
        self.allincome=sum(self.income)
        print(self.allincome)
        self.expenseZ()
    def expenseZ(self):
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
        self.allexpenses=sum(self.expenses)
        print(self.allexpenses)
        self.cashAwncash()
    def cashAwncash(self):
        investement=int(input("What will be your downpayment on the property?"))
        self.investment.append(investement)
        investement=int(input("What will be the closing costs?"))
        self.investment.append(investement)
        investement=int(input("What will your rehab budget be?"))
        self.investment.append(investement)
        investement=int(input("Any other investments?"))
        self.investment.append(investement)
        self.allinvestments=sum(self.investment)
        print(self.allinvestments)
        self.cashCalc()
    def cashCalc(self):
        self.cashFlow=self.allincome-self.allexpenses
        self.totalRoi=((self.cashFlow*12)/self.allinvestments)*100
        print(self.totalRoi)

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
calc=rental()
calc.runRoi()