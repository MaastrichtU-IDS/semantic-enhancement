from rdflib import ConjunctiveGraph, Literal, XSD,Graph
import re
import sys, getopt

#from textblob import TextBlob
#from langdetect import  detect


#detect datatypes :string, date, boolean(case insensitive), float


def main(argv):
    workdir="/data/"
    inputfile='input2.nq'
    outputfile="output2.nq"

    try:
      opts, args = getopt.getopt(argv,"hi:o:",["inputfile="])
    except getopt.GetoptError:
      print ('test.py --inputfile <inputfile>')
      sys.exit(2)
    for opt, arg in opts:
      if opt in ("-i", "--inputfile"):
         inputfile = arg
    # print ('Input file is "', inputfile)
    inputdata=inputfile.split('.')
    # TODO: change all this to take the absolute full path as arg (e.g.: /data/input.nq)
    input_full_path=workdir + inputfile

    data=inputdata[0]
    datatype=inputdata[1]
    if(datatype == "nq"):
        g = ConjunctiveGraph(identifier="http://kraken/graph/data/"+ data)
        g.default_context.parse(input_full_path, format='nquads')
    else:
        g = Graph() #for n3
        if datatype == "nt":
            g.default_context.parse(input_full_path,format='nt')
        elif datatype == "ttl":
            g.default_context.parse(input_full_path,format='n3')

    patternstring1 = re.compile("^([A-Z]|[a-z]+)+$")
    patternstring = re.compile("\w+")
    patterndatey = re.compile("^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$")
    patterndatem = re.compile("^(0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])[- /.](19|20)\d\d$")
    patterndated = re.compile("^(0[1-9]|[12][0-9]|3[01])[- /.](0[1-9]|1[012])[- /.](19|20)\d\d$")
    patternfloat=re.compile("^[-+]?[0-9]*\.[0-9]+$")
    for s, p, o in g:
        if patternstring.match(o) != None and len(o)>=2 and "symbol" not in str(p): #gene symbols are detected as lang
            # print(s,p,o)
            # print(detect(o))#works but string needs to be at least 3 characters- choice between string and lang
            if "name" in str(p):
                g.remove((s, p, o))
                # g.add((s, p, Literal(o, lang=detect(o)))) #works but string needs to be at least 3 charachters- choice between string and lang
                g.add((s, p, Literal(o, datatype=XSD.string)))
            elif patterndatey.match(o) != None or patterndated.match(o) != None or patterndatem.match(o)!= None:
                # print(o)
                g.remove((s, p, o))
                g.add((s, p,Literal(o, datatype=XSD.date)))
            elif re.search('true', o, re.IGNORECASE) or re.search('false', o, re.IGNORECASE):
                # print(o)
                g.remove((s, p, o))
                g.add((s, p, Literal(o, datatype=XSD.boolean)))
            elif patternfloat.match(o) != None:
                g.remove((s, p, o))
                g.add((s, p, Literal(o, datatype=XSD.float)))
            elif patternstring1.match(o) != None:
                g.remove((s, p, o))
                g.add((s, p, Literal(o, datatype=XSD.string)))
    if(datatype == "nq"):
        g.serialize(destination=workdir + outputfile, format='nquads')
    elif datatype == "nt":
        g.serialize(destination=workdir + outputfile, format='nt')
    elif datatype == "ttl":
        g.default_context.parse(workdir + outputfile,format='n3')

if __name__ == "__main__":
    main(sys.argv[1:])