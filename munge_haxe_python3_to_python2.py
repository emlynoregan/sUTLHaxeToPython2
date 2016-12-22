import fileinput
import sys
from pkg_resources import replace
import re

'''
This code is the worst thing in the world. You've never seen such a wtf.
What it does is to mangle the code that Haxe produces for sUTL for Python3, so that it works under Python2.
The proper approach would be to change the generator for Haxe Python so that it generates code that works for 
both Python2 and Python3, or to make a separate Python2 generator. But that can wait for another day.
This code is stupidly brittle, but at least there's a decent test suite which will break if something breaks 
this (eg: if a new version of Haxe's python generator generates slightly different code).
'''

def main():
    sys.stdout.writelines(["from __future__ import unicode_literals\n"])
    sys.stdout.writelines(["from __future__ import division\n"])
    sys.stdout.writelines(["from util2 import Util2\n"])
    sys.stdout.writelines(["str = unicode\n"])
    
    for line in fileinput.input():
        outline = fixline(line)
        sys.stdout.writelines([outline])

g_classname = None
def fixline(aInLine):
    global g_classname
    
    retval = aInLine
    
    if retval[:6] == "class ":
        m = re.search("\(([^\)]+)\)", retval)
        if m:
            g_classname = m.group(1)
            

    if retval[:3] == "\t\t\t": # at least three
        if "nonlocal" in retval:
            retval = ""
        retval = retval.replace("_g_val", "_g_val[0]")
        retval = retval.replace("_g_head", "_g_head[0]")
    elif retval[:2] == "\t\t": # exactly 2
        if "_g_head = " in retval or "_g_val = " in retval:
            arr = retval.split(" = ")
            retval = "%s = [%s]\n" % (arr[0], arr[1].strip())
        else:
            retval = retval.replace("_g_head", "_g_head[0]")
    
    #retval = retval.replace("print", "xprint")
    retval = retval.replace(".print(", ".xprint(")
    retval = retval.replace("def print(", "def xprint(")
    
    retval = retval.replace("super().__init__()", "%s.__init__(self)" % g_classname)
    retval = retval.replace("super().__init__(message)", "%s.__init__(self, message)" % g_classname)
        
    retval = retval.replace("python_lib_Sys.stdout.buffer.write", "python_lib_Sys.stdout.write")
    retval = retval.replace("return str(o)", "return unicode(o)")
    retval = retval.replace("python_Boot.toString1(s,\"\")", "unicode(python_Boot.toString1(s,\"\"))")
    retval = retval.replace("haxe_Log.trace = haxe_unit_TestRunner.customTrace", "#haxe_Log.trace = haxe_unit_TestRunner.customTrace")
    retval = retval.replace("haxe_Log.trace = old", "#haxe_Log.trace = old")
    retval = retval.replace("o.__delattr__(field)", "del o.__dict__[field]")
    retval = retval.replace("class Util2", "class SlowUtil2")
    retval = retval.replace("Util2._hx_class = Util2", "")


    if "def unhandleKeywords" in retval:
#         retval = "%s\t\treturn unicode(name)\n" % retval
        retval = "%s\t\tname = unicode(name)\n" % retval

    if "_hx_local_0 = len(field)" in retval:
        retval = "%s\t\tif hasattr(o,field):\n\t\t\treturn getattr(o,field)\n" % retval
#     if "def field(o,field):" in retval:
#         if g_classname == "python_Boot":
#             retval = "%s\t\tXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n" % retval
#         else:
#             print g_classname

    return retval
    
if __name__ == "__main__":
    main()