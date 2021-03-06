#!python
import glob
import os.path
import support
import path_conf
import cherrypy
from cherrypy.lib.static import serve_file
log_path = path_conf.log_path

class Downloadlist:
    def index(self, directory="."):
	directory = log_path
        html = """<html><body><h2>Here are the files in the selected directory:</h2>
<!--<a href="index?directory=%s">Up</a>--!><br />
        """ % os.path.dirname(os.path.abspath(directory))

        for filename in glob.glob(directory + '/*'):
            absPath = os.path.abspath(filename)
            if os.path.isdir(absPath):
                html += '<a href="/index?directory=' + absPath + '">' + os.path.basename(filename) + "</a> <br />"
            else:
                html += '<a href="/download/?filepath=' + absPath + '">' + os.path.basename(filename) + "</a> <br />"

        html += """</body></html>"""
        return html
    index.exposed = True

class Download:

    def index(self, filepath):
        return serve_file(filepath, "application/x-download", "attachment")
    index.exposed = True

#if __name__ == '__main__':
#    root = Downloadlist()
#    root.download = Download()
#    cherrypy.quickstart(root)
