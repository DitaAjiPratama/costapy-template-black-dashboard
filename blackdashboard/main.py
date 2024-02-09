from core   import html

static = [
    {
        'name':'/blackdashboard/css',
        'value':{
            'tools.staticdir.on'    : True ,
            'tools.staticdir.dir'   : './templates/blackdashboard/static/css' ,
        }
    },
    {
        'name':'/blackdashboard/demo',
        'value':{
            'tools.staticdir.on'    : True ,
            'tools.staticdir.dir'   : './templates/blackdashboard/static/demo' ,
        }
    },
    {
        'name':'/blackdashboard/fonts',
        'value':{
            'tools.staticdir.on'    : True ,
            'tools.staticdir.dir'   : './templates/blackdashboard/static/fonts' ,
        }
    },
    {
        'name':'/blackdashboard/img',
        'value':{
            'tools.staticdir.on'    : True ,
            'tools.staticdir.dir'   : './templates/blackdashboard/static/img' ,
        }
    },
    {
        'name':'/blackdashboard/js',
        'value':{
            'tools.staticdir.on'    : True ,
            'tools.staticdir.dir'   : './templates/blackdashboard/static/js' ,
        }
    },
    {
        'name':'/blackdashboard/scss',
        'value':{
            'tools.staticdir.on'    : True ,
            'tools.staticdir.dir'   : './templates/blackdashboard/static/scss' ,
        }
    },
]

def main(dir, page):

    html_template   = html.main.get_html("templates/blackdashboard/html")
    html_page       = html.main.get_html(dir)
    params_list = {
        "template"  : html_template ["template.html"    ]   ,
        "navbar"    : html_template ["navbar.html"      ]   ,
        "sidebar"   : html_template ["sidebar.html"     ]   ,
        "footer"    : html_template ["footer.html"      ]   ,
        "container" : html_page     [ page+".html"      ]
    }
    return params_list
