#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup, NavigableString, Tag

from templ import templet


@templet
def html_doc(params, content):
    """
<!doctype html>
<html lang="fr">
    <head>
		<meta charset="utf-8"></meta>

		<title>reveal.js – The HTML Presentation Framework</title>

		<meta name="description" content="A presentation"></meta>
		<meta name="author" content="has to be replaced by AUTOR"></meta>

		<meta name="apple-mobile-web-app-capable" content="yes"></meta>
		<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent"></meta>

		<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, minimal-ui"></meta>

		<link rel="stylesheet" href="${params.path}/css/reveal.css"></link>
		<link rel="stylesheet" href="${params.path}/css/theme/beige.css" id="theme"></link>
		<link rel="stylesheet" href="${params.path}/css/presentable.min.css"></link>
		<!-- Code syntax highlighting -->
		<link rel="stylesheet" href="${params.path}/lib/css/zenburn.css"></link>

		<!-- Printing and PDF exports -->
		<script>
			var link = document.createElement( 'link' );
			link.rel = 'stylesheet';
			link.type = 'text/css';
			link.href = window.location.search.match( /print-pdf/gi ) ? '${params.path}/css/print/pdf.css' : '${params.path}/css/print/paper.css';
			document.getElementsByTagName( 'head' )[0].appendChild( link );
		</script>

		<!--[if lt IE 9]>
		<script src="${params.path}/lib/js/html5shiv.js"></script>
		<![endif]-->
	</head>

	<body>
<div class="reveal">
<div class="slides">
    ${content}
</div>
</div>
<aside id="presentable-icon" class="revealjs">
<a title="Table of Contents" href="#/1">
<img alt="Table of Contents" src="${params.path}/plugin/presentable/icons/impressjs.png" href="#/1"/>
</a>
</aside>
<script src="${params.path}/lib/js/head.min.js"></script>
<script src="${params.path}/js/reveal.js"></script>
<script>

			Reveal.initialize({
				controls: ${params.ctrl},
				progress: true,
				history: true,
				center: true,
				slideNumber: true,
				showNotes: ${params.comms},
				mouseWheel: false,
				transition: 'zoom', // none/fade/slide/convex/concave/zoom

				// Optional reveal.js plugins
				dependencies: [
					{ src: '${params.path}/lib/js/classList.js', condition: function() { return !document.body.classList; } },
					{ src: '${params.path}/plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
					{ src: '${params.path}/plugin/notes/notes.js', async: true },
					{ src: '${params.path}/plugin/math/math.js', async: true },
					{ src :'${params.path}/plugin/presentable/presentable.min.js' , async: true , callback : function(){presentable.toc({framework: "revealjs"});}}
				]
			});

		</script>

	</body>
</html>

"""


empty_allowed_tags = ['br', 'img', 'meta']


def is_a_tag(tag):
    return (isinstance(tag, Tag))


def is_a_string(tag):
    return (isinstance(tag, NavigableString))


def not_empty_string(s):
    return (is_a_string(s) and s.string.strip())


def processTitle(c, el):
    if c.name is not None and c.name == "TITRE":
        el.insert(El("h3", c.string))
        return True
    return False


def processParagraphe(obj):
    el = El("p")
    for c in obj.contents:
        if not processTitle(c, el):
            if not_empty_string(c):
                el.insert(El("span", c.string))
            elif is_a_tag(c):
                el.insert(inlineNames(c.name, c))
    return el


def processListElement(obj):
    el = El("li")
    for c in obj.children:
        if not_empty_string(c):
            el.insert(El("span", c.string))
        if is_a_tag(c):
            if c.name == "LISTE":
                el.insert(processList(c))
            else:
                el.insert(inlineNames(c.name, c))
    return el


def processList(obj):
    el = El("ul")
    for c in obj.children:
        if not processTitle(c, el):
            if not_empty_string(c):
                el.insert(El("h3", c.string))
            elif is_a_tag(c):
                el.insert(processListElement(c))

    return el

def processExtLink(el):
    link = El("a", el.string)
    link.attr("href", el["href"])
    return link

def processEquation(el):
    return El("span", "\("+el["texte"]+"\)")


def inlineNames(x, y):
    if(x == "EMPHASE"):
        return El("em", y.string)

    elif(x == "LIEN_EXTERNE"):
        return processExtLink(y)
    elif(x == "EQUATION"):
        return processEquation(y)
    else:
        return El("em", "Cannot yet process : " + x  + " sorry :S ")

def blockNames(x, y):
    if(x=="PARAGRAPHE"):
        return processParagraphe(y)
    elif(x=="LISTE"):
        return processList(y)
    elif(x=="TITRE"):
        return El("h2", y.string)
    else:
        return  El("p", "not yet implemeneted" + x + "<br/> work in progress :)")


def processPart(part, el):
    """
    Process part processing
    Calls for all sub part parsers
    :param part:  the part to be parsed
    :param el: fragment of the final page
    """
    el.insert(El("section", El("h1", part.TITRE.string)))
    for section in part.find_all("SECTION"):
        s = El("section")
        for child in section.contents:
            if not isinstance(child, NavigableString):
                s.insert(blockNames(child.name, child))
        el.insert(s)


def processTitlePage(part):
    """
    EAST has a tag for title page, with no equivalences in Reveal
    It should be processed as a part, but with specific tags
    """
    tp = El("Section")
    if part is not None:
        tp.insert(El("h1", part.TITRE.string))
        if part.SOUS_TITRE:
            tp.insert(El("h3", part.SOUS_TITRE.string))
        if part.AUTEUR:
            tp.insert(El("h5", part.AUTEUR.string))
        if part.EMAIL:
            tp.insert(El("h6", El("small", part.EMAIL.string)))
    return tp


def generateHtmlFile(entry):
    xml = BeautifulSoup(entry, "xml")
    p = Params("non", "oui")
    el = El("div")
    el.attr("class", "slides")
    EAST = xml.contents[0]
    el.insert(processTitlePage(EAST.find("PAGE_TITRE")))
    for part in EAST.find_all("PARTIE"):
        processPart(part, el)

    ret = BeautifulSoup(html_doc(p, str(el)), 'html.parser')
    return ret


class Params:
    """this class is the object representation of powerpoint commentaries"""

    def __init__(self, commentaires, buttons):
        if commentaires == "oui":
            self.comms = "true"
        else:
            self.comms = "false"
        if buttons == "non":
            self.ctrl = "false"
        else:
            self.ctrl = "true"

        self.path = "revealApp"


class El:
    """this class give a simplified representation of an html element"""

    def __init__(self, name, content="", refs=None):
        self.b = name
        self.v = []
        if(refs is None):
            refs = {}
        self.refs = refs
        self.v.append(content)

    def __str__(self):
        """
        A str representation of the html element
        :return: All values surrounded by tags
        """
        ret = "<" + self.b
        ret += self.attrToString()
        return ret + ">" + self.getValue() + "</" + self.b + ">"

    def attrToString(self):
        """
        String representation of the current attributes
        :return: ref="val" pairs of attributes
        """
        ret = ""
        for k,v in self.refs.items():
            ret += " " + k + '="'+ v + '"'
        return ret

    def insert(self, element):
        self.v.append(element)

    def getValue(self):
        """ Assembling all elements into a single string chain """
        ret = ""
        for v in self.v:
            ret += str(v)
        return ret

    def attr(self, ref, val):
        """
        Adds a value to a specified references
        There is no consistency check
        You can add as many attributes as you want to any refs
        :param ref: the reference to append ex : href
        :param val: the value to be associated with the reference ex : "www.perdu.com"
        """
        if(ref in self.refs): self.refs[ref] = self.refs[ref] + " " + val
        else : self.refs[ref] = val


