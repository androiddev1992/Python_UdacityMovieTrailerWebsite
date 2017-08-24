import movie
import fresh_tomatoes

# Create Actor instances
ellen_degeneres = movie.Actors("Ellen DeGeneres", "http://static.tvgcdn.net/mediabin/showcards/celebs/d-f/thumbs/ellen-degeneres_sc_768x1024.png")
alexander_gould = movie.Actors("Alexander Gould", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk1NTY1OTgyMV5BMl5BanBnXkFtZTcwMTE2NjE0Nw@@._V1_UY317_CR4,0,214,317_AL_.jpg")
albert_brooks = movie.Actors("Albert Brooks", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTM4MzEwMTMxN15BMl5BanBnXkFtZTcwNTQwMTc2NQ@@._V1_UY317_CR4,0,214,317_AL_.jpg")

tom_hanks = movie.Actors("Tom Hanks", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2MjMwNDA3Nl5BMl5BanBnXkFtZTcwMTA2NDY3NQ@@._V1_UY317_CR2,0,214,317_AL_.jpg")
tim_allen = movie.Actors("Tim Allen", "https://upload.wikimedia.org/wikipedia/commons/f/ff/Tim_Allen_cropped.jpg")

zoe_saldana = movie.Actors("Zoe Saldana", "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA4NDk1NTA1OV5BMl5BanBnXkFtZTcwMTIzMjQ4Ng@@._V1_UY1200_CR121,0,630,1200_AL_.jpg")
sam_worthington = movie.Actors("Sam Worthington", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTc5NTMyMjIwMV5BMl5BanBnXkFtZTcwNTMyNjYwMw@@._V1_UY317_CR6,0,214,317_AL_.jpg")

brad_bird = movie.Actors("Brad Bird", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTk5Mzg1ODcyNV5BMl5BanBnXkFtZTcwMjU1ODkyMw@@._V1_UY317_CR13,0,214,317_AL_.jpg")
patton_oswalt = movie.Actors("Patton Oswalt", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTA1OTM4MDg2NzNeQTJeQWpwZ15BbWU3MDk0NDA2MTM@._V1_UY317_CR1,0,214,317_AL_.jpg")

robin_williams = movie.Actors("Robin Williams", "https://images-na.ssl-images-amazon.com/images/M/MV5BNTYzMjc2Mjg4MF5BMl5BanBnXkFtZTcwODc1OTQwNw@@._V1_UX214_CR0,0,214,317_AL_.jpg")
evan_mcgregor = movie.Actors("Ewan McGregor", "https://images-na.ssl-images-amazon.com/images/M/MV5BMTg1MjQ0MDg0Nl5BMl5BanBnXkFtZTcwNjYyNjI5Mg@@._V1_UX214_CR0,0,214,317_AL_.jpg")

robert_downey = movie.Actors("Robert Downey Jr.", "https://images-na.ssl-images-amazon.com/images/M/MV5BNzg1MTUyNDYxOF5BMl5BanBnXkFtZTgwNTQ4MTE2MjE@._V1_UX214_CR0,0,214,317_AL_.jpg")
chris_evans = movie.Actors("Chris Evans", "https://pbs.twimg.com/profile_images/605082381528096769/gt_sJRot.png")
chris_hemsworth = movie.Actors("Chris Hemsworth", "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3d/Hemsworth_TFF_%28cropped%29.jpg/170px-Hemsworth_TFF_%28cropped%29.jpg")
scarlet_johansson = movie.Actors("Scarlet Johansson", "https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/Goldene_Kamera_2012_-_Scarlett_Johansson_3_%28cropped%29.JPG/170px-Goldene_Kamera_2012_-_Scarlett_Johansson_3_%28cropped%29.JPG")


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

fresh_tomatoes.open_movies_page(movies)