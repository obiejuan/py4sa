#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
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
#




import wsgiref.handlers


from google.appengine.ext import webapp


class MainHandler(webapp.RequestHandler):

  def get(self):
    self.response.out.write("""
    <html>
    <title>Python For Unix and Linux System Administration</title>
    <p>
    <b>Python For Unix and Linux System Administration<b>
    </p>
    <p>
    <b>Book URL:  <a href="http://oreilly.com/catalog/9780596515829/">http://oreilly.com/catalog/9780596515829/</a></b>
    </p>
    <p>
    <b>Book Table of Contents:  <a href="http://code.noahgift.com/toc_py4sa.pdf">PY4SA TOC</a></b>
    </p>
    <p>
    <b>Book Source Code: <a href="http://examples.oreilly.com/9780596515829/code/">http://examples.oreilly.com/9780596515829/code/</a></b>
    </p>
    <p>
    <b>Book Virtual Machine: <a href="http://examples.oreilly.com/9780596515829/vm/">http://examples.oreilly.com/9780596515829/vm/</a></b>
    </p>
    <p>
    <b>Book Google Code Project: <a href="http://code.google.com/p/py4sa/">http://code.google.com/p/py4sa/</a></b>
    </p>
    <p>
    <b>Downloadable Zip of All Code: <a href="http://py4sa.googlecode.com/files/py4sa_code_08262008_rc1.zip">http://py4sa.googlecode.com/files/py4sa_code_08262008_rc1.zip</a></b>
    </p>
    <p>
    <b>Virtual Machine Instructions: <a href="http://www.livingubuntu.com/?p=89">http://www.livingubuntu.com/?p=89</a></b>
    </p>
	<!--comment-->
    </html>""")


def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)


if __name__ == '__main__':
  main()
