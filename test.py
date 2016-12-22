from sUTLHaxePython2.sUTL import sUTL
import json

def main():
    s = sUTL()

    libs = [[
      {
          "name": "six",
          "transform-t": {
              "x": 6
          }
      }
    ]]
 
    source = {
      "y": 3
    }
   
    decl = {
      "transform-t": {
        "x": [{"&": "six"}, "^@"]
      },
      "requires": ["six"]
    }
 
    libr = s.compilelib([decl], libs)
    lib = libr["lib"]
 
    result = s.evaluate(source, decl["transform-t"], lib, 0)

    def slow():
        with open("sUTL_core.dist.json") as f:
            lcoredist = json.load(f)

        source = {
          "x": 1,
          "y": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1, 2, 3, 4, 5, 6, 7, 8, 9, 10,1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        }
       
        decl = {
          "transform-t": {
            "&": "addmaps",
            "map1": "^@",
            "map2": {
                "x": 3,
                "z": 4
            }
          },
          "requires": ["addmaps"]
        }
        
        llib = s.compilelib([decl], [lcoredist])
        
        result = s.evaluate(source, decl["transform-t"], llib["lib"], 0)
        
        print result

    import cProfile

    p = cProfile.Profile()
    
    p.enable()
    p.runcall(slow)
    p.disable()
    p.print_stats()
 
    print result

# def main():
#   s = Sutl()
# 
#   v = s.ExampleString()
#   print type(v)
#   print v  
# 
#   v = s.ExampleInt()
#   print type(v)
#   print v  
# 
#   v = s.ExampleFloat()
#   print type(v)
#   print v  
# 
#   v = s.ExampleBool()
#   print type(v)
#   print v  
# 
#   v = s.ExampleNull()
#   print type(v)
#   print v  
# 
#   v = s.ExampleArray()
#   print type(v)
#   print v  
# 
#   v = s.ExampleDict()
#   print type(v)
#   print type(v.x)
#   print v  
# 
#   def isObject(obj):
#     return isinstance(obj, dict)
# 
#   def isArray(obj):
#     return isinstance(obj, list)
# 
#   def convertToAnon(aObj):
#     if isObject(aObj):
#     convDict = {key: convertToAnon(aObj[key]) for key in aObj}
#     return _hx_AnonObject(convDict)
#     elif isArray(aObj):
#     return [convertToAnon(litem) for litem in aObj]
#     elif isinstance(aObj, str):
#     return unicode(aObj)
#     else:
#     return aObj
# 
#   def convertFromAnon(aObj):
#     if isinstance(aObj, _hx_AnonObject):
#     retval = dict(aObj.__dict__)
#         retval = {key: convertFromAnon(retval[key]) for key in retval}
#     return retval
#     elif isArray(aObj):
#     return [convertFromAnon(litem) for litem in aObj]
#     else:
#     return aObj
# 
#   libs = [[
#     {
#         "name": "six",
#         "transform-t": 6
#     }
#   ]]
# 
#   libsconv = convertToAnon(libs)
# 
#   source = {
#     "y": 3
#   }
#   
#   sourceconv = convertToAnon(source)
# 
#   decl = {
#     "transform-t": {
#       "x": [{"&": "six"}, "^@"]
#     },
#     "requires": ["six"]
#   }
# 
#   declconv = convertToAnon(decl)
# 
#   print declconv
# 
#   libr = s.compilelib([declconv], libsconv)
#   lib = libr.lib
#   print convertFromAnon(libsconv)
#   print convertFromAnon(lib)
# 
#   result = s.evaluate(sourceconv, getattr(declconv, "transform-t"), lib, 0)
# 
#   print result
#   print convertFromAnon(result)


main()