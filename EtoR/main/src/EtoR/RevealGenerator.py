#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

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





def generateHtmlFile(entry):
    xml = BeautifulSoup(entry, "xml")
    p = Params("non", "oui")
    el = El("div").withClass("slides")
    EAST = xml.contents[0]
    for partie in EAST.find_all("PARTIE"):
        print (partie);
        el.insert(El("section", El("h1", partie.TITRE.string)))

    ret = BeautifulSoup(html_doc(p, str(el)), 'html.parser')
    return ret

class Params:
    """this class is the object representation of powerpoint commentaries"""
    def __init__(self, commentaires, buttons):
        if commentaires == "oui": self.comms = "true"
        else: self.comms = "false"
        if buttons == "non" : self.ctrl="false"
        else: self.ctrl = "true"

        self.path = "revealApp"


class El:
    """this class give a simplified representation of an html element"""
    def __init__(self, name, content="", clazz=""):
        self.b = name
        self.v = []
        self.c = clazz
        self.v.append(content)

    def __str__(self):
        ret = "<" + self.b
        if self.c != "":
            ret += " class=\"" + self.c +'"'
        return  ret + ">" + self.getValue() + "</" + self.b + ">"

    def insert(self, element):
        self.v.append(element)

    def getValue(self):
        """ Assembling all elements into a single string chain """
        ret =""
        for v in self.v:
            ret += str(v)
        return ret
    def withClass(self, clazz):
        self.c = clazz
        return self
