from flask import Flask
import cfscrape
import pickle

app = Flask(__name__)

torrent9home = "http://www.torrent9.biz"
scraper = cfscrape.create_scraper()

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return scraper.get(torrent9home+'/'+path).content

if __name__ == '__main__':
    app.run(host='0.0.0.0')