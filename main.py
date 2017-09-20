import movie
import fresh_tomatoes

# Create Actor instances
ellen_degeneres = movie.Actors("Ellen DeGeneres", "https://goo.gl/RPA7Xu")
alexander_gould = movie.Actors("Alexander Gould", "https://goo.gl/mnzv2a")
albert_brooks = movie.Actors("Albert Brooks", "https://goo.gl/SHCnnc")

tom_hanks = movie.Actors("Tom Hanks", "https://goo.gl/EKP1Dy")
tim_allen = movie.Actors("Tim Allen", "https://goo.gl/tDi8ry")

zoe_saldana = movie.Actors("Zoe Saldana", "https://goo.gl/Dh6b47")
sam_worthington = movie.Actors("Sam Worthington", "https://goo.gl/6JNDT3")

brad_bird = movie.Actors("Brad Bird", "https://goo.gl/uqKDaJ")
patton_oswalt = movie.Actors("Patton Oswalt", "https://goo.gl/KGmzmR")

robin_williams = movie.Actors("Robin Williams", "https://goo.gl/3dCXWD")
evan_mcgregor = movie.Actors("Ewan McGregor", "https://goo.gl/4MQTRQ")

robert_downey = movie.Actors("Robert Downey Jr.", "https://goo.gl/7C7ykn")
chris_evans = movie.Actors("Chris Evans", "https://goo.gl/wmkqUc")
chris_hemsworth = movie.Actors("Chris Hemsworth", "https://goo.gl/QNp1B7")
scarlet_johansson = movie.Actors("Scarlet Johansson", "https://goo.gl/tSSsgZ")


# Create Movie instances
toy_story = movie.Movie("Toy Story",
                        "Story of a boy and his toys",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        8.3,
                        ["Drama", "Action", "Adventure"],
                        [tom_hanks, tim_allen])

avatar = movie.Movie("Avatar",
                     "A marine on alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/a/a1/Avatar-video-game-cover.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY",
                     7.8,
                     ["Drama", "Action", "Adventure"],
                     [zoe_saldana, sam_worthington])

finding_nemo = movie.Movie("Finding Nemo",
                   "Story of dad and a son",
                   "https://upload.wikimedia.org/wikipedia/en/7/71/Finding_Nemo_Coverart.png",
                   "https://www.youtube.com/watch?v=wZdpNglLbt8",
                   8.1,
                   ["Drama", "Action", "Adventure"],
                   [ellen_degeneres, alexander_gould, albert_brooks])


robots = movie.Movie("Robots",
                     "A robot's story",
                     "https://upload.wikimedia.org/wikipedia/en/f/f2/Robots2005Poster.jpg",
                     "https://www.youtube.com/watch?v=p9X16KPOgFI",
                     6.3,
                     ["Drama", "Action", "Adventure"],
                     [evan_mcgregor, robin_williams])

avengers = movie.Movie("The Avengers",
                       "Super Hero Adventures",
                       "https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
                       "https://www.youtube.com/watch?v=eOrNdBpGMv8",
                       8.1,
                       ["Action", "Superhero", "Fictional"],
                       [robert_downey, chris_hemsworth, chris_evans, scarlet_johansson])

ratatouille = movie.Movie("Ratatouille",
                          "Story about a rat aspiring to become chef",
                          "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk",
                          8.0,
                          ["Drama", "Action", "Adventure"],
                          [brad_bird, patton_oswalt])


movies = [toy_story, avatar, finding_nemo, ratatouille, robots, avengers]

# This function call with open a page of movies
fresh_tomatoes.open_movies_page(movies)