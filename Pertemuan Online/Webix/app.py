import falcon

dataMovie = [
    {'title': "The Shawshank Redemption", 'year': '1994',
        'votes': '678790', 'rating': '9.2', 'rank': 1},
    {'title': "The Godfather", 'year': '1972',
        'votes': '511495', 'rating': '9.2', 'rank': 2},
    {'title': "The Godfather: Part II", 'year': '1974',
        'votes': '319352', 'rating': '9.0', 'rank': 3},
    {'title': "The Good, the Bad and the Ugly", 'year': '1966',
        'votes': '213030', 'rating': '8.9', 'rank': 4}
]


class Movies:
    def on_get(self, req, resp):
        resp.media = dataMovie
        resp.status = falcon.HTTP_200


app = falcon.App()

movies = Movies()

app.add_route('/movies', movies)

# waitress-serve --listen 127.0.0.1:5000 app:app
