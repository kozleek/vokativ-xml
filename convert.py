#!/usr/bin/python
from os import path
import codecs
from vokativ import vokativ
from vokativ import sex


fo = "jmena.xml"
fi = "jmena.txt"
fa = codecs.open( fo, "w", "UTF-8" );

fa.write("<names>\n")
with codecs.open(fi, "r", "UTF-8") as f:
    for line in f:
        name = line.strip()
        name_vokativ = vokativ(name).title()
        name_sex = sex(name)
        fa.write ("\t<item name='%s' vokativ='%s' sex='%s' />\n" % (name, name_vokativ, name_sex))
fa.write("</names>")