import json
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
        if order.side == 'buy':
            self.buy_book.append(order)
        if order.side == 'sell':
            self.sell_book.append(order)

    def match_order(self, amount, side):
        if side == 'buy':
            for sell_order in self.sell_book:
                if amount >= sell_order.amount:
                    continue

        return


if __name__ == "__main__":

    order_book = OrderBook()

    for i in range(1, 100):
        if i % 2 == 0:
            ord_id = f'ord_{i}'
            ticker = 'AMZN'
            amount = 201.32 + i
            quantity = i+1
            side = 'sell'
            order_book.place_order(
                Order(ord_id, ticker, amount, quantity, side))
        else:
            ord_id = f'ord_{i}'
            ticker = 'AMZN'
            amount = 201.32 + i
            quantity = i+1
            side = 'buy'
            order_book.place_order(
                Order(ord_id, ticker, amount, quantity, side))

    # LOGGING ORDER_BOOK IN CONSOLE
    def prRed(skk): return ("\033[91m {}\033[00m" .format(skk))
    print("SELL ORDER")
    for order in order_book.sell_book:
        print(prRed(json.dumps(order.__dict__)))

    def prGreen(skk): return ("\033[92m {}\033[00m" .format(skk))
    print("BUY ORDER")
    for order in order_book.buy_book:
        print(prGreen(json.dumps(order.__dict__)))
