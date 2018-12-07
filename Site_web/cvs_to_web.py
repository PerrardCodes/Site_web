# coding: utf-8
import bibtexparser
import csv
def internship(file):
    f = open(file, "r")
    t = f.read()
    t = t.replace("\n", ";")
    t = t.split(";")
    m="<ul>"
    for i in range(10, len(t), 10):
        if(t[i+3]!=""):
            t[i+3]="<i>, with " + t[i+3] + "</i>"
        m += "<li> %s %s, %s%s (%s, %s)</li>" % (t[i+0], t[i+1], t[i+8], t[i+3], t[i+7], t[i+2])
    m+= """</ul>"""
    return m

def contributor(file):
    t = ""
    with open(file) as csvfile:
        spamreader=csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in spamreader :
            t +=" ".join(row)

    t = t.split(";;;")
    m="<ul>"
    for i in range(1, len(t)):
        temp = t[i].split(";")
        if(len(temp) >1):
            m+="<li> %s %s %s (%s, %s)</li>" % (temp[0], temp[1], temp[2], temp[3], temp[4])
    m+= """</ul>"""
    return m

def article(file):
    m='<div id="flexpubli">'
    with open(file) as bibtex_file:
        bib_database = bibtexparser.load(bibtex_file)
    t= bib_database.entries
    for i in range(0, len(t)):
        m+="""
        <div class="publication">
            <h5>"""
        m+=t[i]["title"].encode('utf-8')
        m+="""
            </h5>
            <p>
        """
        m+=t[i]["ENTRYTYPE"].encode('utf-8').lower().capitalize()
        m+=" by "
        m+= t[i]["author"].encode('utf-8')
        m+= " published in \""
        m+= t[i]["journal"].encode('utf-8')
        m+="\", volume "
        m+= t[i]["volume"].encode('utf-8')
        if "pages" in t[i] :
            m+=", page "
            m+= t[i]["pages"].encode('utf-8')
        m+=", in "
        m+=t[i]["year"].encode('utf-8')
        m+="""
        </p>
        <a href="database/MesArticles/"""
        m+=t[i]["ID"].encode("utf-8").replace(" ", "")
        m+=""".pdf"><img src="image/PDF.png" class="pdf"></a>
        <p class="date">Published the :
        """
        m+=t[i]["date-added"].encode('utf-8')[:10]
        m+= "</p></div>"
    m+="</div>"
    return m
