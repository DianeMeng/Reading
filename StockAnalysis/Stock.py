
class Stock:
    date=""
    def __init__(self,date,floor_price,opening_price,ceiling_price,volume,amount,closing_price):
        self.date=date
        self.floor_price = floor_price
        self.opening_price = opening_price
        self.ceiling_price = ceiling_price
        self.volume = volume
        self.amount = amount
        self.closing_price = closing_price

    def __repr__(self):
        return "" + self.date + ","+str(self.floor_price) + ","+str(self.opening_price)+ ","+str(self.ceiling_price)+ "," + str(self.volume)+ ","+str(self.amount)+ ","+ str(self.closing_price)

    def __str__(self):
        return "" + self.date + ","+str(self.floor_price) + ","+str(self.opening_price)+ ","+str(self.ceiling_price)+ "," + str(self.volume)+ ","+str(self.amount)+ ","+ str(self.closing_price)



class Record(Stock):
    date = ''