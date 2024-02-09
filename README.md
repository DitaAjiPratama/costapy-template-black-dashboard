# CostaPy Template - Black Dashboard
Dashboard template from [Creative Tim](https://www.creative-tim.com/product/black-dashboard#) that has been designed for CostaPy

## Usage

- Put the folder in your templates directory
- Add to handler

        import templates.blackdashboard.main as blackdashboard

        kwargs["mako"] = {
          "website" : blackdashboard.main(directory.page["public"], "dashboard") # page_directory, file_name
        }

- Define a necessary variable on your modules function

        title           = "CostaPy"
        baseurl         = "http://localhost"

        menu_icon       = "fa fa-user-tie"
        menu_name       = "Dashboard"
        profile_picture = "http://localhost/profile/1.jpg"
        profile_name    = "John Smith"
        logout          = "http://localhost/logout"

        color           = "blue"              # blue | green | orange | red
        logo            = "http://localhost/logo.png"
        user_roles      = ["member"]          # A roles that user have
        active_page     = "Dashboard"         # Current active page name

        copyright       = "Dita Aji Pratama"  # Copyright on the footer

- Config a navbar menu on your modules function

        navbar_menu = [
          {
            "name"  :"Home",
            "href"  :"/"
          },
          {
            "name"  :"Dashboard",
            "href"  :"#"
          },
          {
            "name"  :"CostaPy Website",
            "href"  :"https://costapy.ditaajipratama.com"
          }
        ]

        profile_menu = [
          {
            "name"  :"Profile",
            "href"  :"/profile"
          },
          {
            "name"  :"Setting",
            "href"  :"/setting"
          }
        ]

- Config a sidebar menu on your modules function

        sidebar_menu = [
          {
            "icon"  :"fa fa-home",
            "name"  :"Dashboard",
            "href"  :"/",
            "roles" :["member", "admin"]
          },
          {
            "icon"  :"fa fa-users",
            "name"  :"Users",
            "href"  :"/users",
            "roles" :["admin"]
          }
        ]

- Config a footer menu on your modules function

        footer_menu = [
          {
            "name"  :"CostaPy Website",
            "href"  :"https://costapy.ditaajipratama.com"
          }
        ]

- Set a template on your modules function

        from mako.template import Template

        interface = Template(params["mako"]["website"]['template']).render(
          title     = title,
          baseurl   = baseurl,
          navbar    = Template(params["mako"]["website"]['navbar']).render(
            title           = title,
            baseurl         = baseurl,
            menu_icon       = menu_icon,
            menu_name       = menu_name,
            menu            = navbar_menu,
            profile_picture = profile_picture,
            profile_name    = profile_name,
            profile_menu    = profile_menu,
            logout          = logout
          ),
          sidebar   = Template(params["mako"]["website"]['sidebar']).render(
            color           = color,
            logo            = logo,
            title           = title,
            user_roles      = user_roles,
            active_page     = active_page,
            menu            = sidebar_menu
          ),
          footer    = Template(params["mako"]["website"]['footer']).render(
            copyright       = copyright,
            menu            = footer_menu,
          ),
          container = Template(params["mako"]["website"]['container']).render(
            # your container content here
          )
        )
