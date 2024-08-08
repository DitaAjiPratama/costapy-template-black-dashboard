from core   import html

static = [
    {
        "route":"/templates/blackdashboard/css/<filepath>",
        "root":"./templates/blackdashboard/static/css"
    },
    {
        "route":"/templates/blackdashboard/demo/<filepath>",
        "root":"./templates/blackdashboard/static/demo"
    },
    {
        "route":"/templates/blackdashboard/fonts/<filepath>",
        "root":"./templates/blackdashboard/static/fonts"
    },
    {
        "route":"/templates/blackdashboard/img/<filepath>",
        "root":"./templates/blackdashboard/static/img"
    },
    {
        "route":"/templates/blackdashboard/js/<filepath>",
        "root":"./templates/blackdashboard/static/js"
    },
    {
        "route":"/templates/blackdashboard/scss/<filepath>",
        "root":"./templates/blackdashboard/static/scss"
    }
]

def main(dir, page):
    html_template   = html.main.get_html("templates/blackdashboard/html")
    html_page       = html.main.get_html(dir)
    params_list = {
        "index"     : html_template ["index.html"       ]   ,
        "navbar"    : html_template ["navbar.html"      ]   ,
        "sidebar"   : html_template ["sidebar.html"     ]   ,
        "footer"    : html_template ["footer.html"      ]   ,
        "container" : html_page     [f"{page}.html"     ]
    }
    return params_list
