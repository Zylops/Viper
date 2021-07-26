class Page:
    def __init__(self, title, body, stylesheets=[], scripts=[]):
        self.title = title
        self.stylesheets = stylesheets
        self.scripts = scripts
        self.body = body
    
    def __str__(self):
        linked_scripts = []
        for script in self.scripts:
            linked_scripts.append(f'<script>{script}</script>')
        linked_scripts = '\n'.join(linked_scripts)
        
        linked_stylesheets = []
        for sheet in self.stylesheets:
            linked_stylesheets.append(f'<link rel="stylesheet" href="{sheet}">')
        linked_stylesheets = '\n'.join(linked_stylesheets)
        
        source = f'<!DOCTYPE html>\n<html>\n<head>\n{linked_scripts}{linked_stylesheets}<title>{self.title}</title>\n</head>\n<body>\n{self.body}\n</body>\n</html>'
        return source
    
    def source(self):
        return str(self)
    
class Body:
    def __init__(self, elements=[]):
        self.elements = elements
    
    def __str__(self):
        source = []
        for element in self.elements:
            source.append(str(element))
        source = '\n'.join(source)
        return source
    
    def source(self):
        return str(self)

class Div:
    def __init__(self, elements=[], id=None, styles=[]):
        self.elements = elements
        self.id = id
        self.styles = styles
    
    def __str__(self):
        source = [f'<div style="{" ".join(self.styles)}" id="{self.id}">']
        for element in self.elements:
            source.append(str(element))
        source.append('</div>')
        source = '\n'.join(source)
        return source
    
    def source(self):
        return str(self)

class Element:
    def __init__(self, classes=[], ids=[]):
        self.classes = ' '.join(classes)
        self.ids = ' '.join(ids)

class Heading(Element):
    def __init__(self, text, level=1, styles=[]):
        self.text = text
        self.level = level
        self.styles = ' '.join(styles)
    
    def __str__(self):
        source = f'<h{self.level} style="{self.styles}">{self.text}</h{self.level}>'
        return source
    
    def source(self):
        return str(self)
    
class Paragraph(Element):
    def __init__(self, text, styles=[]):
        self.text = text
        self.styles = ' '.join(styles)
    
    def __str__(self):
        source = f'<p style="{self.styles}">{self.text}</p>'
        return source
    
    def source(self):
        return str(self)
    
#class="{super.classes}" id="{super.ids}"