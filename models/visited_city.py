class Visited_city:
    def __init__(self, user, city, is_visited, notes, id = None):
        self.user = user
        self.city = city
        self.is_visited = is_visited
        self.notes = notes
        self.id = id

    def mark_as_visited(self):
        self.is_visited = True
