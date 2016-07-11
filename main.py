import media
import generate_page

# create 9 media.Movie objects
shawshank_redemption = media.Movie("The Shawshank Redemption",
                                   "Two imprisoned men bond over a number of y"
                                   "ears, finding solace and eventual redempti"
                                   "on through acts of common decency.",
                                   "http://ia.media-imdb.com/images/M/MV5BODU4"
                                   "MjU4NjIwNl5BMl5BanBnXkFtZTgwMDU2MjEyMDE@._"
                                   "V1_UX182_CR0,0,182,268_AL_.jpg",
                                   "https://www.youtube.com/watch?v=6hB3S9bIac"
                                   "o")
godfather = media.Movie("The Godfather",
                        "The aging patriarch of an organized crime dynasty tra"
                        "nsfers control of his clandestine empire to his reluc"
                        "tant son.",
                        "http://ia.media-imdb.com/images/M/MV5BMjEyMjcyNDI4MF5"
                        "BMl5BanBnXkFtZTcwMDA5Mzg3OA@@._V1_UX182_CR0,0,182,268"
                        "_AL_.jpg",
                        "https://www.youtube.com/watch?v=sY1S34973zA")
godfather2 = media.Movie("The Godfather: Part II",
                         "The early life and career of Vito Corleone in 1920s "
                         "New York is portrayed while his son, Michael, expand"
                         "s and tightens his grip on his crime syndicate stret"
                         "ching from Lake Tahoe, Nevada to pre-revolution 1958"
                         " Cuba.",
                         "http://ia.media-imdb.com/images/M/MV5BNDc2NTM3MzU1Nl"
                         "5BMl5BanBnXkFtZTcwMTA5Mzg3OA@@._V1_UX182_CR0,0,182,2"
                         "68_AL_.jpg",
                         "https://www.youtube.com/watch?v=qJr92K_hKl0")
dark_knight = media.Movie("The Dark Knight",
                          "When the menace known as the Joker wreaks havoc and"
                          " chaos on the people of Gotham, the caped crusader "
                          "must come to terms with one of the greatest psychol"
                          "ogical tests of his ability to fight injustice.",
                          "http://ia.media-imdb.com/images/M/MV5BMTMxNTMwODM0N"
                          "F5BMl5BanBnXkFtZTcwODAyMTk2Mw@@._V1_UX182_CR0,0,182"
                          ",268_AL_.jpg",
                          "https://www.youtube.com/watch?v=_PZpmTj1Q8Q")
schindlers_list = media.Movie("Schindler's List",
                              "In Poland during World War II, Oskar Schindler "
                              "gradually becomes concerned for his Jewish work"
                              "force after witnessing their persecution by the"
                              " Nazis.",
                              "http://ia.media-imdb.com/images/M/MV5BMzMwMTM4M"
                              "DU2N15BMl5BanBnXkFtZTgwMzQ0MjMxMDE@._V1_UX182_C"
                              "R0,0,182,268_AL_.jpg",
                              "https://www.youtube.com/watch?v=JdRGC-w9syA")
angry_men = media.Movie("12 Angry Men",
                        "A jury holdout attempts to prevent a miscarriage of j"
                        "ustice by forcing his colleagues to reconsider the ev"
                        "idence.",
                        "http://ia.media-imdb.com/images/M/MV5BODQwOTc5MDM2N15"
                        "BMl5BanBnXkFtZTcwODQxNTEzNA@@._V1_UX182_CR0,0,182,268"
                        "_AL_.jpg",
                        "https://www.youtube.com/watch?v=fSG38tk6TpI")
pulp_fiction = media.Movie("Pulp Fiction",
                           "The lives of two mob hit men, a boxer, a gangster'"
                           "s wife, and a pair of diner bandits intertwine in "
                           "four tales of violence and redemption.",
                           "http://ia.media-imdb.com/images/M/MV5BMTkxMTA5OTAz"
                           "Ml5BMl5BanBnXkFtZTgwNjA5MDc3NjE@._V1_UX182_CR0,0,1"
                           "82,268_AL_.jpg",
                           "https://www.youtube.com/watch?v=ewlwcEBTvcg")
lord_rings = media.Movie("The Lord of the Rings: The Return of the King",
                         "Hobbits Frodo and Sam reach Mordor in their quest to"
                         " destroy the `one ring', while Aragorn leads the for"
                         "ces of good against Sauron's evil army at the stone "
                         "city of Minas Tirith.",
                         "http://ia.media-imdb.com/images/M/MV5BMjE4MjA1NTAyMV"
                         "5BMl5BanBnXkFtZTcwNzM1NDQyMQ@@._V1_UX182_CR0,0,182,2"
                         "68_AL_.jpg",
                         "https://www.youtube.com/watch?v=y2rYRu8UW8M")
good_bad_ugly = media.Movie("The Good, the Bad and the Ugly",
                            "A bounty hunting scam joins two men in an uneasy "
                            "alliance against a third in a race to find a fort"
                            "une in gold buried in a remote cemetery.",
                            "http://ia.media-imdb.com/images/M/MV5BOTQ5NDI3MTI"
                            "4MF5BMl5BanBnXkFtZTgwNDQ4ODE5MDE@._V1_UX182_CR0,0"
                            ",182,268_AL_.jpg",
                            "https://www.youtube.com/watch?v=WCN5JJY_wiA")

# create a list
movie_list = [shawshank_redemption, godfather, godfather2, dark_knight,
              schindlers_list, angry_men, pulp_fiction, lord_rings,
              good_bad_ugly]
# pass list as the argument and generate html page
generate_page.open_movies_page(movie_list)
