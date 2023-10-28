import json
import random
import sqlite3
print("Starting trading engine..!!!")


class OrderBook:

    def __init__(self):
        self.buy_book = []
        self.sell_book = []

    def place_order(self, ord_id, ticker, amount, quantity, side):
        # print("Type of order is", type(order))
        # parsed_order = json.dumps(order.__dict__)
        order = {"ord_id": ord_id, "ticker": ticker,
                 "amount": amount, "quantity": quantity, "side": side}

        if side == 'buy':
            self.buy_book.append(order)
        elif side == 'sell':
            self.sell_book.append(order)
        self.match_orders(order)

    def match_orders(self, order):
        # TODO: This order tracking system automatically matches for the execution
        # TODO: of the best possible pair of orders in the system. The best pair
        # TODO: is made up of the highest bid, and the lowest ask orders.
        # print("Order from match_order", order)

        self.buy_book = sorted(
            self.buy_book, key=lambda order: order["amount"], reverse=True)
        self.sell_book = sorted(
            self.sell_book, key=lambda order: order["amount"])

        # For buy order
        if order["side"] == 'buy':
            for sell_order in self.sell_book:
                if order["ticker"] == sell_order["ticker"] and order["amount"] >= sell_order["amount"]:
                    if sell_order["quantity"] >= order["quantity"]:
                        # Update order quantities
                        sell_order["quantity"] -= order["quantity"]
                        # Print order details
                        print("trade executed")
                        # print(
                        #     f"Trade: {order.quantity} {order.ticker} at {sell_order.amount}")

                    # Remove orders with zero quantity
                    if sell_order["quantity"] == 0:
                        self.sell_book.pop(0)
                else:
                    break

        # For sell order
        if order["side"] == 'sell':
            for buy_order in self.buy_book:
                if order["ticker"] == buy_order["ticker"] and order["amount"] <= buy_order["amount"]:
                    if buy_order["quantity"] <= order["quantity"]:
                        # Update order quantities
                        buy_order["quantity"] -= order["quantity"]
                        # Print order details
                        print("trade executed")
                        # print(
                        #     f"Trade: {order.quantity} {order.ticker} at {buy_order.amount}")

                    # Remove orders with zero quantity
                    if buy_order["quantity"] == 0:
                        self.buy_book.pop(0)
                else:
                    break

    def print_order_book(self):

        def prRed(skk): return ("\033[91m {}\033[00m" .format(skk))
        print("SELL ORDERS:")
        for order in self.sell_book:
            print(prRed(json.dumps(order)))
        # for order in self.sell_orders:
        #     print(f"Price: {order['price']}, Quantity: {order['quantity']}")

        def prGreen(skk): return ("\033[92m {}\033[00m" .format(skk))
        print("BUY ORDERS:")
        for order in self.buy_book:
            print(prGreen(json.dumps(order)))
        # for order in self.buy_orders:
        #     print(f"Price: {order['price']}, Quantity: {order['quantity']}")


if __name__ == "__main__":

    order_book = OrderBook()

    tickers = ['AMZN', 'MSFT', 'ZOHO', 'TCS', 'HDFC', 'BOFA']

    # ord_id = str(random.randint(100000, 999999))
    # ticker = 'AMZN'
    # amount = 360
    # quantity = 6
    # side = 'buy'
    # order_book.place_order(ord_id, ticker, amount, quantity, side)

    # ord_id = str(random.randint(100000, 999999))
    # ticker = 'AMZN'
    # amount = 360
    # quantity = 6
    # side = 'sell'
    # order_book.place_order(ord_id, ticker, amount, quantity, side)

    for i in range(0, 20):
        if i % 2 == 0:
            ord_id = str(random.randint(100000, 999999))
            ticker = random.choice(tickers)
            amount = round(random.uniform(100, 400), 2)
            quantity = random.randint(1, 9)
            side = random.choice(['buy', 'sell'])
            order_book.place_order(
                ord_id, ticker, amount, quantity, side)
        else:
            ord_id = str(random.randint(100000, 999999))
            ticker = random.choice(tickers)
            amount = round(random.uniform(100, 400), 2)
            quantity = random.randint(1, 9)
            side = random.choice(['buy', 'sell'])
            order_book.place_order(
                ord_id, ticker, amount, quantity, side)

    # LOGGING ORDER_BOOK IN CONSOLE
    order_book.print_order_book()
