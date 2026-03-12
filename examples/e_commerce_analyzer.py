from linqex import Enumerable

class ECommerceAnalyzer:
    """
    Analyzes raw e-commerce order data to extract actionable business metrics
    without loading intermediate lists into memory.
    """
    
    def __init__(self, orders: list[dict]):
        self._orders = Enumerable(orders)

    def get_top_spending_customers(self, top_n: int = 3) -> list[dict]:
        """
        Groups orders by customer, calculates their total lifetime spend,
        and returns the top N highest spenders.
        """
        return (self._orders
            # 1. Group all orders by customer ID
            .group_by(lambda order: order["customer_id"])
            
            # 2. For each group (customer), calculate total spend
            .select(lambda group: {
                "customer_id": group.key,
                "total_spend": group.sum(lambda order: order["total_amount"]),
                "order_count": group.count()
            })
            
            # 3. Sort descending by spend to find the whales
            .order_by_descending(lambda stat: stat["total_spend"])
            
            # 4. Take only the top N
            .take(top_n)
            
            # 5. Terminal operation: Execute the pipeline
            .to_list())

    def get_all_purchased_product_ids(self) -> set[str]:
        """
        Flattens the nested lists of items inside each order into a single 
        distinct set of product IDs.
        """
        return (self._orders
            # Extract the list of items from each order and flatten them into one stream
            .select_many(lambda order: order["items"])
            # Extract just the product ID from each item
            .select(lambda item: item["product_id"])
            # Terminal operation: Create a unique set
            .to_set())

if __name__ == "__main__":
    raw_orders = [
        {"customer_id": "C1", "total_amount": 150.0, "items": [{"product_id": "P1"}, {"product_id": "P2"}]},
        {"customer_id": "C2", "total_amount": 80.0,  "items": [{"product_id": "P3"}]},
        {"customer_id": "C1", "total_amount": 300.0, "items": [{"product_id": "P4"}]},
        {"customer_id": "C3", "total_amount": 500.0, "items": [{"product_id": "P1"}, {"product_id": "P5"}]}
    ]

    analyzer = ECommerceAnalyzer(raw_orders)
    
    print("Top Spenders:")
    for spender in analyzer.get_top_spending_customers(top_n=2):
        print(f"Customer {spender['customer_id']}: ${spender['total_spend']} across {spender['order_count']} orders")

    print("\nUnique Products Sold:")
    print(analyzer.get_all_purchased_product_ids())
