class StockPair:
    """Represents a pair of stocks with their correlation coefficient."""
    
    def __init__(self, stock1, stock2, correlation):
        self.stock1 = stock1
        self.stock2 = stock2
        self.correlation = correlation
    
    def __repr__(self):
        return f"StockPair({self.stock1}, {self.stock2}, {self.correlation:.4f})"
