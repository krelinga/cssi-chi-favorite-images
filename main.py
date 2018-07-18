# Copyright 2016 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import webapp2
import logging
import jinja2
import os


jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


class AddFavorite(webapp2.RequestHandler):
    def post(self):
        url = self.request.get('url')
        logging.info('server saw a request to add %s to list of favorites' % (url))
        # TODO: add this URL to a list of favorites in data store.


class GetFavorites(webapp2.RequestHandler):
    def get(self):
        template = jinja_env.get_template('templates/favorites.html')
        # TODO: add code to query datastore and get the list of all favorites,
        # and pass that into our template rendering function.
        return self.response.write(template.render())


app = webapp2.WSGIApplication([
    ('/add_favorite', AddFavorite),
    ('/favorites', GetFavorites)
], debug=True)
