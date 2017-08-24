import webbrowser


class Movie:
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title,
                 movie_storyline,
                 movie_poster_image,
                 movie_trailer_url,
                 movie_rating,
                 movie_genres,
                 movie_actors):
        """Create a new instance of a movie.

                title: Movie title.
                storyline: Movie storyline
                rating: Rating out of 10.
                poster_image_url: URL of the movie poster.
                trailer_youtube_url: URL of the trailer on YouTube.
                genres: List of genres as strings.
                actors: List of actors as string.
                """
        self.title = movie_title
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.poster_image_url = movie_poster_image
        self.trailer_youtube_url = movie_trailer_url
        self.genres = movie_genres
        self.actors = movie_actors

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def genres_list(self):
        """Get a comma separated string of genres."""
        list = ""
        for genre in self.genres:
            list += genre + ", "

        return list.rstrip(", ")

    def actors_list(self):
        """Get a comma separated string of actors."""
        list = ""
        for actor in self.actors:
            list += actor.name + ", "

        return list.rstrip(", ")

class Actors:
    """This class provides a way to store information about actors"""

    def __init__(self, actor_name, actor_image):
        self.movie_actor = actor_name
        self.movie_actor_image = actor_image
