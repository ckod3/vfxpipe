import nuke
import os
import inspect
import fxpipe
'''
This will add all subdirectories here to the Nuke Path
'''

curInitFile = inspect.getfile(inspect.currentframe()) # get location of current py file
fileDir = os.path.dirname(curInitFile) # get the dir name of that file

for (path, dirs, files) in os.walk('%s' % (fileDir)):
    if fxpipe.os in path:
        nuke.pluginAddPath(path) # add to the nuke plugin path for each directory found
