class Rating:
    def __init__(self, user_id, movie_id, rating, timestamp):
        self.user_id = user_id
        self.movie_id = movie_id
        self.rating = rating
        self.timestamp = timestamp
     
    def __str__(self):
        return f"Rating(user_id={self.user_id}, movie_id={self.movie_id}, timestamp={self.timestamp})"
