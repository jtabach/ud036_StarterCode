import webbrowser

# class Movie takes in a title, storyline, image, and video url
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        # define instance variable
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # instance method for showing movie trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
