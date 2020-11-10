class Album:

    def __init__(self, title, artist, amount_units, ideal_units, cost, sell_price, genre, label, id = None):
        self.title = title
        self.artist = artist
        self.amount_units = amount_units
        self.ideal_units = ideal_units
        self.cost = cost
        self.sell_price = sell_price
        self.genre = genre
        self.label = label
        self.id = id

    def markup(self, album):
        markup = ((self.sell_price - self.cost) / self.cost) * 100
        return markup