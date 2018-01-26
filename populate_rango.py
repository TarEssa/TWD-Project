import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():

    python_pages =[
        {"title":"Official Python Tutorial",
         "url":"http://docs.python.org/2/tutorial/",
         "veiws": 11 },

        {"title":"How to Think like a Computer Scientist",
         "url":"http://www.greenteapress.com/thinkpython/",
         "veiws": 12},

        {"title":"Learn Python in 10 Minutes",
         "url":"http://www.korokithakis.net/tutorials/python/",
         "veiws": 13}
        ]

    django_pages =[
        {"title":"Official Django Tutorial",
         "url":"http://docs.djangoproject.com/en/1.9/intro/tutorial01/",
         "veiws": 14},

        {"title":"Django Rocks",
         "url":"http://www.djangorocks.com/",
         "veiws": 15},

        {"title":"How to Tango with Django",
         "url":"http://www.tangowithdjango.com/",
         "veiws": 16}
        ]

    other_pages =[
        {"title":"Bottle",
         "url":"http://bottlepy.org/docs/dev/",
         "veiws": 17},

        {"title":"Flask",
         "url":"http://flask.pocoo.org",
         "veiws": 9000}
        ]

    cats = {"Python":{"pages": python_pages,"views":128, "likes":64},
            "Django":{"pages": django_pages,"views":64, "likes":32},
            "Other Frameworks":{"pages": other_pages,"views":32, "likes":16},
            }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data.get("views" , 0), cat_data.get("likes", 0))
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"])
                
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print("- {0} - {1}".format(str(c), str(p)))

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.views = views
    c.save()
    return c


if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()








            
