#!/usr/bin/python
# coding: utf-8


from __future__ import unicode_literals
from __future__ import print_function
import os
from http import server
from CGIHTTPServer import CGIHTTPRequestHandler


class RequestHandler(CGIHTTPRequestHandler):

    have_fork = False
    have_popen2 = False
    have_popen3 = False

    def is_cgi(self):
        """
        Every python script will be called (from Jens)
        """

        base, filename = os.path.split(self.path)

        if ".py" in filename:
            if "?" in filename:
                os.environ["SCRIPT_FILENAME"] = filename.split("?", 1)[0]
            else:
                os.environ["SCRIPT_FILENAME"] = filename

            os.environ['DOCUMENT_ROOT'] = os.getcwd()
            self.cgi_info = base, filename
            return True


http_server = server.HTTPServer(("", 8080), RequestHandler)
print("The server listens on http://localhost:8080")
http_server.serve_forever()
