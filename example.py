from main import *
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    logo = Image(url='https://i.imgur.com/5JwgpaU.png', styles=['height:81px; width:144px;'])
    heading = Heading('Welcome to Viper!', classes=['animate__animated', 'animate__pulse'])
    about = Paragraph('This is an example page with all available modules used. This page will be updated for new modules (if any). Thanks for checking it out! Have fun modulating!')
    gitlink = Link(url='https://github.com/Zylops/Viper', text='View on GitHub!')
    developers = Table(headers=['Authors'], rows=['Zylops', '0xPiyush'])
    
    header = Div(id='header', styles=['padding:20px;', 'text-align:center;', 'height:100%;'], modules=[logo, LineBreak(), heading, HorizontalLine()])
    content = Div(id='content', styles=['padding:5px;', 'text-align:center;', 'height:100%;'], modules=[about, gitlink, developers])
    stylesheets = ['https://www.w3schools.com/w3css/4/w3.css', 'https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css']
    
    page = Page(title='Viper!', body=Body(modules=[header, content]), stylesheets=stylesheets)
    
    return page.source()

app.run(debug=True)
