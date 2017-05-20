import media
import fresh_tomatoes

remember_the_titans = media.Movie("Remember The Titans",
                            "A 2000 American sports film produced by Jerry Bruckheimer and directed by Boaz Yakin",
                            "https://upload.wikimedia.org/wikipedia/en/d/d1/Remember_the_titansposter.jpg",
                            "https://www.youtube.com/watch?v=nPhu9XsRl4M")
print(remember_the_titans.storyline)

movie_list = [remember_the_titans]

fresh_tomatoes.open_movies_page(movie_list)
