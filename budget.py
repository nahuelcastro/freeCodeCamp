class Category:

    Category = ''
    ledger = list()
    funds = 0


    def __init__(self, name):
        self.name = name

    def __str__(self):
        mask_t = '******************************' # 30 *
        mask_a = '       ' # 7 whitespaces
        mask_d = '                       ' # 23 whitespaces
        res = ''
        enter = '\n'

        med = (30 - len(self.name)) // 2
        title = mask_t[0: med] + self.name + mask_t[ med + len(self.name) - 1 : 30]
        res += title + enter; 

        total = 0
        for i in range(len(self.ledger)):
            d = self.ledger[i]['description']
            if len(d) > 23:
                res_desc = d[0:23]
            else:
                res_desc = d + mask_d[len(d):23]
            
            a = self.ledger[i]['amount']
            sa = str("{:.2f}".format(a))
            if len(sa) > 7:
                res_amount = sa[len(sa)-7:len(sa)]
            else:   
                res_amount = mask_a[0 : 7 - len(sa)] + sa 
            
            res += res_desc + res_amount + enter
            
            total += a;
        
        res += 'Total: ' + str("{:.2f}".format(total))
        return res;

        




    
    def check_funds(self, amount):
        return self.funds >= amount

    def get_balance(self):
        return self.funds

    def deposit(self, amount, description = ''):
        d = dict()
        d['amount'] = amount
        d['description'] = description
        self.ledger.append(d)
        self.funds += amount


    def withdraw(self, amount, description = ''):
        if(self.check_funds(amount)):
            d = dict()
            d['amount'] = amount * (-1)
            d['description'] = description
            self.ledger.append(d)
            self.funds -= amount
            return True
        return False
        

    def transfer(self, amount, category):
        
        description = 'Transfer to ' + category.name
        w = self.withdraw(amount, description)

        description = 'Transfer from ' + self.name
        if(w): category.deposit(amount)

        return w
        


    
def create_spend_chart(l):
    return 0;


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

    

