import random, string

class Stock:
    def __init__(self,name,symbol,price):
        self.name=name
        self.symbol=symbol
        self.price=price
        self.previous_price = price

    def updatePrice(self):
        self.previous_price = self.price
        self.price += random.uniform(-50, 50)
        self.price = round(self.price, 2)

def  createStocks(num_stocks):
    stocks = []
    used_names = set()
    used_symbols = set()

    for i in range(num_stocks):
        while True: #Loop to check that we don't have duplicates stocks
            name = ''.join(random.choices(string.ascii_uppercase, k=5))
            symbol = ''.join(random.choices(string.ascii_uppercase, k=3))
            if name not in used_names and symbol not in used_symbols:
                used_names.add(name)
                used_symbols.add(symbol)
                break

        price = round(random.uniform(10, 500), 2)
        stocks.append(Stock(name, symbol, price))
    return stocks

def displayStockMarket(stocks):
    print("Stock Market:")
    for stock in stocks:
        print(f"{stock.name} ({stock.symbol}): {stock.price} €")
    print()

#Trading Strategy
def buySignal(stock):
    return (stock.price - stock.previous_price) / stock.previous_price * 100 >= 25

def sellSignal(stock):
    return (stock.previous_price - stock.price) / stock.previous_price * 100 >= 10

#Testing
def testTradingStrategy(stocks, initial_balance, num_days):
    balance = initial_balance
    portfolio = {}
    
    for day in range(num_days):
        print(f"Day {day + 1}:")
        
        #Randomly updating stocks
        num_stocks_to_update = random.randint(1, len(stocks))
        stocks_to_update = random.sample(stocks, num_stocks_to_update)
        for stock in stocks_to_update:
            stock.updatePrice()

        #Searching all stocks to buy or to sell
        for stock in stocks:
            if buySignal(stock) and balance >= stock.price:
                balance -= stock.price
                if stock.symbol in portfolio:
                    portfolio[stock.symbol] += 1
                else:
                    portfolio[stock.symbol] = 1
                print(f"Bought 1 share of {stock.symbol} at ${stock.price}")
            elif sellSignal(stock) and stock.symbol in portfolio and portfolio[stock.symbol] > 0:
                balance += stock.price
                portfolio[stock.symbol] -= 1
                print(f"Sold 1 share of {stock.symbol} at ${stock.price}")
        
        displayStockMarket(stocks)
    
    print("\nFinal Balance and Portfolio:")
    print(f"Balance: ${round(balance,2)}")
    print("Portfolio:")
    flag = False

    for symbol in portfolio:
        num = portfolio[symbol]
        if num > 0:
            print(f"{symbol}: {num} shares")
            flag = True

    if not flag:
        print("Portofolio is Empty")


#Main
num_stocks = 10
initial_balance = 15000
num_days = 20

stocks = createStocks(num_stocks)
displayStockMarket(stocks)
testTradingStrategy(stocks, initial_balance, num_days)