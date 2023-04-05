import falcon
import connection


class GetPrice:
    def on_get(self, req, resp):
        query = "SELECT current_date"
        data = connection.select(query)
        resp.media = data
        resp.status = falcon.HTTP_200


app = falcon.App()

getPrice = GetPrice()
print(getPrice)
app.add_route('/getPrice', getPrice)
