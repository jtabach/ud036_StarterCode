import media
import fresh_tomatoes


# Create movie instances using Movie class from media.py
remember_the_titans = media.Movie("Remember The Titans",
                            "A 2000 American sports film produced by Jerry Bruckheimer and directed by Boaz Yakin",
                            "https://upload.wikimedia.org/wikipedia/en/d/d1/Remember_the_titansposter.jpg",
                            "https://www.youtube.com/watch?v=nPhu9XsRl4M")
miracle_on_ice = media.Movie("Miracle On Ice",
                            "The Miracle on Ice refers to a medal-round game during the men's ice hockey tournament at the 1980 Winter Olympics in Lake Placid, New York, played between the hosting United States, and the defending gold medalists, the Soviet Union.",
                            "https://upload.wikimedia.org/wikipedia/en/b/bd/Sports_Illustrated_Miracle_on_Ice_cover.jpg",
                            "https://www.youtube.com/watch?v=X7xfRXGMrDM")
rocky = media.Movie("Rocky",
                            "Rocky is a 1976 American sports drama film directed by John G. Avildsen and both written by and starring Sylvester Stallone.",
                            "https://upload.wikimedia.org/wikipedia/en/1/18/Rocky_poster.jpg",
                            "https://www.youtube.com/watch?v=7RYpJAUMo2M")
creed = media.Movie("Creed",
                            "In 1998, Adonis Donnie Johnson, the son of an extramarital lover of former heavyweight champion Apollo Creed, is serving time in a Los Angeles youth facility when Creed's widow",
                            "https://upload.wikimedia.org/wikipedia/en/2/24/Creed_poster.jpg",
                            "https://www.youtube.com/watch?v=Uv554B7YHk4")
the_sandlot = media.Movie("The Sandlot",
                            "In the San Fernando Valley during the summer of 1962, Scotty Smalls is the new boy in the neighborhood, seeking desperately to fit in.",
                            "https://upload.wikimedia.org/wikipedia/en/d/d4/Sandlot_poster.jpg",
                            "https://www.youtube.com/watch?v=ec9W8JbFykw")
coach_carter = media.Movie("Coach Carter",
                            "Coach Carter is a 2005 American biographical sports drama film directed by Thomas Carter.",
                            "https://upload.wikimedia.org/wikipedia/en/c/c3/Coach_Carter_poster.JPG",
                            "https://www.youtube.com/watch?v=znyAnWUYf2g")

# Create list of all movie instacnes
movie_list = [remember_the_titans, miracle_on_ice, rocky, creed, the_sandlot, coach_carter]

# use method from fresh_tomatoes to render the movie instances in html
fresh_tomatoes.open_movies_page(movie_list)
