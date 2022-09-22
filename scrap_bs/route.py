import controller.scrapy

def routes(app):
    app.add_url_rule('/',methods=['GET'],view_func=controller.scrapy.scrapy_get)