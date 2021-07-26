from main import *
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    h1 = Heading(title='Welcome!', styles=['color: red;', 'text-align:center;'])
    coolparagraph = Paragraph('This is a very cool website.', styles=['color: red;', 'text-align:center;'])
    headerdiv = Div(id='header', elements=[h1, coolparagraph], styles=['background-color:blue;', 'height:69px;'])
    page = Page('Welcome!', body=Body(elements=[headerdiv]))
    print(page.source())
    return page.source()

app.run()
