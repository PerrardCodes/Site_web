# coding: utf-8
import bibtexparser as bib
import csv
import os
import bibstyle

from yattag import indent


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
    from operator import itemgetter
    
    m='<div id="flexpubli">'
    
    # for a list of bib elements
   # with open(file) as bibtex_file:
    #    bib_database = bib.load(bibtex_file)
        
    #    entries = list(bib_database.entries)
    #    entries.sort(key=lambda x: x['year'],reverse=True)

    #    stringlist = []
    #    for entry in entries:
    #        stringlist.append(bibstyle.display(entry,typ='html'))

     #   doc, tag, text = genhtml.makelist(stringlist,'Publications',order='o',opt=' reversed')

#        filename='siteweb/publications.html'
#        f=open(filename,'w')
#        f.write(indent(doc.getvalue()).encode('utf-8'))
#        f.close()
        
    with open(file) as bibtex_file:
        bib_database = bib.load(bibtex_file)
        
    t= bib_database.entries
    t = sorted(t, key=itemgetter('year'), reverse=True)

    for i in range(0, len(t)):
        namefile = t[i]["ID"].replace(" ", "")
        m+="""
        <div class="publication">
            <h5>"""
        m+=t[i]["title"]#.encode('utf-8')
        m+="""
            </h5>
            <p>
        """

        folder = '/MesArticles/image/'
        if not os.path.isfile(os.path.dirname(file)+folder+namefile+'.png'):
            print('Missing image for : '+folder+namefile)
            name = 'PDF'
            #print(name)
        else:
            name = namefile
            print('found !')
            print(name)
            
        m+="""
        </p>
        <img src="database/MesArticles/image/"""+name+""".png" class="pdf">
        <p class="date">
        """
        m+=bibstyle.display(t[i],typ='html')
#        m+='Published the :'
#        m+=t[i]["date-added"][:10]
        m+="""<a href="database/MesArticles/"""+namefile+""".pdf">"""
        m+='['+str(len(t)-i)+']'
        m+="</a>"
        m+= "</p></div>"
    m+="</div>"
    return m
