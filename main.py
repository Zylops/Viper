#TODO: While adding new tags remember to add a style argument so users can add css to every module.

from jinja2 import Environment, FileSystemLoader, select_autoescape
env = Environment(
    loader = FileSystemLoader("modules"),
    autoescape=select_autoescape()
)

class Page:
    
    def __init__(self, title, body, stylesheets=[], scripts=[]):
        self.title = title
        self.stylesheets = stylesheets
        self.scripts = scripts
        self.body = body
    
    def __str__(self):
        page_module = env.get_template("page.html")
        # Actually generates source code with all the tags and widgets
        source = page_module.render(scripts=self.scripts, stylesheets=self.stylesheets, title=self.title, body=self.body)
        return source
    
    def __doc__():
        return 'A page class, that generates the entire page source code and stores all modules in body while initiated!'
    
    def source(self): #Repeating myself because sometimes referencing the instance does not return the __str__
        return str(self)
    
class Body:
    def __init__(self, modules=[]):
        self.modules = modules
    
    def __str__(self):
        body_module = env.get_template("body.html")
        source = body_module.render(modules=self.modules)
        return source
    
    def __doc__():
        return 'A body class, to compile all provided the modules into one body tag!'
    
    def source(self):
        return str(self)

class Div: #Basically the same as the body class except it for divs 
    def __init__(self, modules=[], id=None, styles=[]):
        self.modules = modules
        self.id = id
        self.styles = ' '.join(styles)
    
    def __str__(self):
        div_module = env.get_template("div.html")
        source = div_module.render(modules=self.modules, id=self.id, styles=self.styles)
        return source
    
    def __doc__():
        return 'A div class to combine modules into a block, like the Body class.'
    
    def source(self):
        return str(self)

class Module:
    def __init__(self, styles=[], id=None, classes=[]):
        self.styles = ' '.join(styles)
        self.id = id
        self.classes = ' '.join(classes)

class Heading(Module):
    def __init__(self, text, level=1, styles=[], id=None, classes=[]):
        self.text = text
        self.level = level
        self.properties = Module(styles, id, classes)
    
    def __str__(self):
        heading_module = env.get_template("heading.html")
        source = heading_module.render(text=self.text, level=self.level, properties=self.properties)
        return source
    
    def source(self):
        return str(self)
    
class Paragraph:
    def __init__(self, text, styles=[], id=None, classes=[]):
        self.text = text
        self.properties = Module(styles, id, classes)
    
    def __str__(self):
        paragraph_module = env.get_template("paragraph.html")
        source = paragraph_module.render(text=self.text, properties=self.properties)
        return source
    
    def source(self):
        return str(self)
    
class Link:
    def __init__(self, url, text, styles=[], id=None, classes=[]):
        self.url = url
        self.text = text
        self.properties = Module(styles, id, classes)

    def __str__(self):
        link_module = env.get_template("link.html")
        source = link_module.render(url=self.url, text=self.text, properties=self.properties)
        return source
    
    def source(self):
        return str(self)
    
class Image:
    def __init__(self, url, alt='', styles=[], id=None, classes=[]):
        self.url = url
        self.alt = alt
        self.properties = Module(styles, id, classes)
    
    def __str__(self):
        image_module = env.get_template("image.html")
        source = image_module.render(url=self.url, alt=self.alt, properties=self.properties)
        return source
    
    def source(self):
        return str(self)
    
class Table:
    def __init__(self, headers, rows, styles=[], id=None, classes=[]):
        self.headers = headers
        self.rows = rows
        self.properties = Module(styles, id, classes)
        
    def __str__(self):
        table_module = env.get_template("table.html")
        source = table_module.render(headers=self.headers, rows=self.rows, properties=self.properties)
        return source
    
    def source(self):
        return str(self)

class HorizontalLine():
    def __str__(self):
        return '<hr>'
    
    def source(self):
        return str(self)

class LineBreak():
    def __str__(self):
        return '<br>'
    
    def source(self):
        return str(self)