import falcon

dataMhs = [
    {'nama': 'Evan', 'nim': '672020273'},
    {'nama': 'Tivani', 'nim': '672020123'}
]


class Mahasiswa:
    # GET
    def on_get(self, req, resp):
        nama = req.params.get('nama', None)
        resp.status = falcon.HTTP_200
        # resp.media = dataMhs  # content type di hapus jika hanya menjalankan object

        resp.content_type = falcon.MEDIA_TEXT
        resp.text = f"Nama Saya {nama}"
        # resp.text = (
        #     '\nTwo things awe me most, the starry sky '
        #     'above me and the moral law within me.\n'
        #     '\n'
        #     '    ~ Immanuel Kant\n\n'
        # )

    def on_post(self, req, resp):
        result = req.media
        nama = result.get('nama')
        nim = result.get('nim')
        resp.status = falcon.HTTP_200
        resp.content_type = falcon.MEDIA_TEXT
        resp.text = f"Nama Saya {nama} Dengan Nim {nim}"


app = falcon.App()

mahasiswa = Mahasiswa()

app.add_route('/mahasiswa', mahasiswa)
