from sUTLHaxePython2.sUTL import sUTL

def main():
    decl = {
      "transform-t": 1
    }
     
    source = {
      "y": 3
    }
       
    s = sUTL()

    def compilelib():
        libs = [[
          {
              "name": "six",
              "transform-t": {
                  "x": 6
              }
          }
        ]]
     
        libr = s.compilelib([decl], libs)
        lib = libr["lib"]
        
        return lib

    def run(shx, thx, lhx, hhx):
        return s.evaluatehx(shx, thx, lhx, hhx)

    lib = compilelib()
    
    import cProfile

    p = cProfile.Profile()
    
    p.enable()
    rhx = p.runcall(run, s._toHx(source), s._toHx(decl["transform-t"]), s._toHx(lib), s._toHx(0))
    p.disable()

    r = s._fromHx(rhx)

    p.print_stats()
 
    print r

main()