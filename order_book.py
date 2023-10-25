import json
import random
import sqlite3
print("Starting trading engine..!!!")


class Order:

    def __init__(self, order_id, ticker, amount, quantity, side):
        self.order_id = order_id
        self.ticker = ticker
        self.amount = amount
        self.quantity = quantity
        self.side = side


class OrderBook:

    def __init__(self):
        self.buy_book = []
        self.sell_book = []

    def place_order(self, order):
        print("Type of order is", type(order))
        parsed_order = json.dumps(order.__dict__)

        if order.side == 'buy':
            self.buy_book.append(order)
            self.match_orders(order)

        if order.side == 'sell':
            self.sell_book.append(order)
            self.match_orders(order)

    def match_orders(self, order):
        # Sort buy and sell orders by price
        om = order.amount
        self.buy_book.sort(key=lambda order: order[om], reverse=True)
        self.sell_book.sort(key=lambda order: order[om])

        # For buy order
        if order.side == 'buy':
            for sell_order in self.sell_book:
                if order.ticker == sell_order.ticker and order.amount >= sell_order.amount:
                    # Update order quantities
                    sell_order.quantity -= order.quantity
                    # Print order details
                    print(
                        f"Trade: {order.quantity} {order.ticker} at {sell_order.amount}")
                    # Remove orders with zero quantity
                    if sell_order.quantity == 0:
                        self.sell_orders.pop(0)
                else:
                    break

        # For sell order
        if order.side == 'sell':
            for buy_order in self.buy_book:
                if order.ticker == buy_order.ticker and order.amount <= buy_order.amount:
                    # Update order quantities
                    buy_order.quantity -= order.quantity
                    # Print order details
                    print(
                        f"Trade: {order.quantity} {order.ticker} at {buy_order.amount}")
                    # Remove orders with zero quantity
                    if buy_order.quantity == 0:
                        self.buy_orders.pop(0)
                else:
                    break

    def print_order_book(self):

        def prRed(skk): return ("\033[91m {}\033[00m" .format(skk))
        print("SELL ORDERS:")
        for order in self.sell_book:
            print(prRed(json.dumps(order.__dict__)))
        # for order in self.sell_orders:
        #     print(f"Price: {order['price']}, Quantity: {order['quantity']}")

        def prGreen(skk): return ("\033[92m {}\033[00m" .format(skk))
        print("BUY ORDERS:")
        for order in self.buy_book:
            print(prGreen(json.dumps(order.__dict__)))
        # for order in self.buy_orders:
        #     print(f"Price: {order['price']}, Quantity: {order['quantity']}")


if __name__ == "__main__":

    order_book = OrderBook()

    tickers = ['AMZN', 'MSFT', 'ZOHO', 'TCS', 'HDFC', 'BOFA']

    for i in range(1, 5):
        if i % 2 == 0:
            ord_id = str(random.randint(100000, 999999))
            ticker = random.choice(tickers)
            amount = round(random.uniform(100, 400), 2)
            quantity = random.randint(1, 9)
            side = random.choice(['buy', 'sell'])
            order_book.place_order(
                Order(ord_id, ticker, amount, quantity, side))
        else:
            ord_id = str(random.randint(100000, 999999))
            ticker = random.choice(tickers)
            amount = round(random.uniform(100, 400), 2)
            quantity = random.randint(1, 9)
            side = random.choice(['buy', 'sell'])
            order_book.place_order(
                Order(ord_id, ticker, amount, quantity, side))

    # LOGGING ORDER_BOOK IN CONSOLE
    # order_book.print_order_book()
