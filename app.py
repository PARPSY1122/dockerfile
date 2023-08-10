from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Ghattamaneni Mahesh Babu is an Indian actor, producer, media personality, and philanthropist who works mainly in Telugu cinema. Wikipedia
Born: 9 August 1975 (age 48 years), Chennai
Upcoming movie: Guntur Kaaram
Spouse: Namrata Shirodkar (m. 2005)
Height: 1.83 m!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
