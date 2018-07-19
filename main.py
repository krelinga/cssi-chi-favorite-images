import webapp2
import logging
import jinja2
import os


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class AddFavoriteHandler(webapp2.RequestHandler):
    def post(self):
        url = self.request.get('url')
        logging.info('server saw a request to add %s to list of favorites' % (url))
        # TODO: add this URL to a list of favorites in data store.


class ListFavoritesHandler(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/favorites.html')
        # TODO: add code to query datastore and get the list of all favorites,
        # and pass that into our template rendering function.
        return self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/add_favorite', AddFavoriteHandler),
    ('/list_favorites', ListFavoritesHandler)
], debug=True)
