class OrderBook:
    def __init__(self):
        # Initialize empty order book lists for buy and sell orders
        self.buy_orders = []
        self.sell_orders = []

    def place_buy_order(self, symbol, price, quantity):
        # Add the buy order to the buy_orders list
        self.buy_orders.append(
            {'symbol': symbol, 'price': price, 'quantity': quantity})
        self.match_orders()

    def place_sell_order(self, symbol, price, quantity):
        # Add the sell order to the sell_orders list
        self.sell_orders.append(
            {'symbol': symbol, 'price': price, 'quantity': quantity})
        self.match_orders()

    def match_orders(self):
        # Sort buy and sell orders by price
        self.buy_orders.sort(key=lambda order: order['amount'], reverse=True)
        self.sell_orders.sort(key=lambda order: order['amount'])

        # Match buy and sell orders
        while self.buy_orders and self.sell_orders:
            buy_order = self.buy_orders[0]
            sell_order = self.sell_orders[0]

            if buy_order['price'] >= sell_order['price']:
                # Execute the trade
                quantity = min(buy_order['quantity'], sell_order['quantity'])
                print(
                    f"Trade: {quantity} {buy_order['symbol']} at {sell_order['price']}")

                # Update order quantities
                buy_order['quantity'] -= quantity
                sell_order['quantity'] -= quantity

                # Remove orders with zero quantity
                if buy_order['quantity'] == 0:
                    self.buy_orders.pop(0)
                if sell_order['quantity'] == 0:
                    self.sell_orders.pop(0)
            else:
                break

    def print_order_book(self):
        print("Buy Orders:")
        for order in self.buy_orders:
            print(f"Price: {order['price']}, Quantity: {order['quantity']}")
        print("Sell Orders:")
        for order in self.sell_orders:
            print(f"Price: {order['price']}, Quantity: {order['quantity']}")


# Example usage
order_book = OrderBook()

order_book.place_buy_order('AAPL', 150, 10)
order_book.place_sell_order('AAPL', 160, 5)
order_book.place_buy_order('AAPL', 155, 8)
order_book.place_sell_order('AAPL', 145, 12)

order_book.print_order_book()
