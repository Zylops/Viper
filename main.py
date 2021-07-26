#Add docstrings to all the functions and classes.
#TODO: Add a bunch more tags, should be easy.
#TODO: While adding new tags remember to add a style argument so users can add css to every module.

class Page:
    def __init__(self, title, body, stylesheets=[], scripts=[]):
        self.title = title
        self.stylesheets = stylesheets
        self.scripts = scripts
        self.body = body
    
    def __str__(self):
        linked_scripts = []
        for script in self.scripts: #Loops through all scripts and adds them to the list with their tags
            linked_scripts.append(f'<script>{script}</script>')
        linked_scripts = '\n'.join(linked_scripts) #Joins list with all tags by newline 
        
        linked_stylesheets = []
        for sheet in self.stylesheets: #Loops through all stylesheets and adds them to the list with their tags we then join to make the style tag
            linked_stylesheets.append(f'<link rel="stylesheet" href="{sheet}">')
        linked_stylesheets = '\n'.join(linked_stylesheets) #Joins list with all tags by newline 
        
        # Actually generates source code with all the tags and widgets
        source = f'<!DOCTYPE html>\n<html>\n<head>\n{linked_scripts}{linked_stylesheets}<title>{self.title}</title>\n</head>\n<body>\n{self.body}\n</body>\n</html>'
        return source
    
    def __doc__():
        return 'A page class, that generates the entire page source code and stores all modules in body while initiated!'
    
    def source(self): #Repeating myself because sometimes referencing the instance does not return the __str__
        return str(self)
    
class Body:
    def __init__(self, modules=[]):
        self.modules = modules
    
    def __str__(self):
        source = []
        for module in self.modules: #Loops through every module to be put in the body and adds its source code to a list
            source.append(str(module))
        source = '\n'.join(source) #Joins all the module source codes by newline
        return source
    
    def __doc__():
        return 'A body class, to compile all provided the modules into one body tag!'
    
    def source(self):
        return str(self)

class Div: #Basically the same as the body class except it for divs 
    def __init__(self, modules=[], id=None, styles=[]):
        self.modules = modules
        self.id = id
        self.styles = styles
    
    def __str__(self):
        source = [f'<div style="{" ".join(self.styles)}" id="{self.id}">'] #Creates the div tag with its styles and id
        for module in self.modules: #Loops through every module in the div and adds its source code to the list
            source.append(str(module))
        source.append('</div>') #Ends div tag 
        source = '\n'.join(source) #Joins all the module source codes by newline
        return source
    
    def __doc__():
        return 'A div class to combine modules into a block, like the Body class.'
    
    def source(self):
        return str(self)

class Heading:
    def __init__(self, text, level=1, styles=[]):
        self.text = text
        self.level = level
        self.styles = ' '.join(styles) #joins a list of styles with a space for the style="" tag
    
    def __str__(self):
        source = f'<h{self.level} style="{self.styles}">{self.text}</h{self.level}>' #Creates the heading tag with its level (h1 , h2, h3, etc), styles and text
        return source
    
    def source(self):
        return str(self)
    
class Paragraph:
    def __init__(self, text, styles=[]):
        self.text = text
        self.styles = ' '.join(styles) #joins a list of styles with a space for the style="" tag
    
    def __str__(self):
        source = f'<p style="{self.styles}">{self.text}</p>'#Creates the paragraph tag with its styles and text
        return source
    
    def source(self):
        return str(self)
    
class Link:
    def __init__(self, url, text, styles=[]):
        self.url = url
        self.text = text
        self.styles = ' '.join(styles) #joins a list of styles with a space for the style="" tag

    def __str__(self):
        source = f'<a href="{self.url}" style="{self.styles}">{self.text}</a>'
        return source
    
    def source(self):
        return str(self)