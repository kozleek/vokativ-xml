#!/usr/bin/python
from os import path
import codecs
from vokativ import vokativ


fo = "jmena.xml"
fi = "jmena.txt"
fa = codecs.open( fo, "w", "UTF-8" );

fa.write("<names>\n")
with codecs.open(fi, "r", "UTF-8") as f:
    for line in f:
        name = line.strip()
        name_vokativ = vokativ(name).title()
        fa.write ("\t<item name='%s' vokativ='%s' />\n" % (name, name_vokativ))
fa.write("</names>")