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
import webapp2
import urllib2
import urllib

from google.appengine.api import urlfetch
from google.appengine.ext.webapp import util
from google.appengine.api import mail

class MainHandler(webapp2.RequestHandler):
    def get(self):
    	usn = '1PI13SCS19'
        url = "http://results.vtu.ac.in/vitavi.php"
        http_header = {
                "Host": "results.vtu.ac.in",
                'Connection': 'keep-alive',
                'Content-Length': '155',
                #
                #
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Origin": "http://results.vtu.ac.in",
                "User-Agent" : "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.76 Safari/537.36",
                "Content-type": "application/x-www-form-urlencoded",
                "Referer": "http://results.vtu.ac.in/vitavi.php/",
                #"Accept-Encoding": "gzip,deflate,scdh",
                "Accept-Language": "en-US,en;q=0.8"
                }

        running = True
        count = 0
        while running: #count<=1:
            try:
                req = urllib2.Request(url, urllib.urlencode({"rid": usn, 'submit': 'SUBMIT'}), http_header)
                response = urllib2.urlopen(req, timeout=40)
                the_page = response.read()
               
            except urllib2.HTTPError, error:
                #self.response.out.write("this is a disaster")
                self.response.out.write("Exception Error <br />")
            else:
                if usn in the_page:               
                    #self.response.out.write("this is not a disaster")
                    running = False
                    self.response.out.write(the_page)

                    # send text from gmail account portion of code starts here.
                    body = the_page

                    

                    message = mail.EmailMessage(sender="megamailer64@gmail.com", subject="VTU Results")

                    message.to = "gune30@gmail.com"
                    message.body = """ """
                    message.html = "" + body + ""
                    
                    message.send()
                    self.response.out.write("Email Sent!!")
                    break
                else:
                    self.response.out.write("not match  <br />")
                    running = False
                    break

            count+=1
            #running = False
        self.response.out.write("<br />Attempt no.: ")
        self.response.out.write(count)
        self.response.out.write("<br />")


class MainPage(webapp2.RequestHandler):
    def get(self):
        usn = '1PI13SCS19'
        url = "http://results.vtu.ac.in/vitavi.php"
        http_header = {
                "Host": "results.vtu.ac.in",
                'Connection': 'keep-alive',
                'Content-Length': '155',
                #
                #
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Origin": "http://results.vtu.ac.in",
                "User-Agent" : "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/32.0.1700.76 Safari/537.36",
                "Content-type": "application/x-www-form-urlencoded",
                "Referer": "http://results.vtu.ac.in/vitavi.php/",
                #"Accept-Encoding": "gzip,deflate,scdh",
                "Accept-Language": "en-US,en;q=0.8"
                }

        running = True
        count = 0
        while running: #count<=1:
            try:
                req = urllib2.Request(url, urllib.urlencode({"rid": usn, 'submit': 'SUBMIT'}), http_header)
                response = urllib2.urlopen(req, timeout=40)
                the_page = response.read()
               
            except urllib2.HTTPError, error:
                #self.response.out.write("this is a disaster")
                self.response.out.write("Exception Error <br />")
            else:
                if usn in the_page:               
                    #self.response.out.write("this is not a disaster")
                    running = False
                    self.response.out.write(the_page)

                    # send text from gmail account portion of code starts here.
                    body = the_page

                    

                    message = mail.EmailMessage(sender="megamailer64@gmail.com", subject="VTU Results")

                    message.to = "gune30@gmail.com"
                    message.body = """ """
                    message.html = "" + body + ""
                    
                    message.send()
                    self.response.out.write("Email Sent!!")
                    break
                else:
                    self.response.out.write("not match  <br />")
                    running = False
                    break

            count+=1
            #running = False
        self.response.out.write("<br />Attempt no.: ")
        self.response.out.write(count)
        self.response.out.write("<br />")


app = webapp2.WSGIApplication([
    ('/main/mail', MainHandler), ('/', MainPage)], debug=True)

def main():
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()
