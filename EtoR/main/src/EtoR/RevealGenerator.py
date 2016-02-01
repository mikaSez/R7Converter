#!/usr/bin/env python
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
html_doc = """
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

		<link rel="stylesheet" href="{pathRevealApp}/css/reveal.css"></link>
		<link rel="stylesheet" href="{pathRevealApp}/css/theme/beige.css" id="theme"></link>
		<link rel="stylesheet" href="{pathRevealApp}/css/presentable.min.css"></link>
		<!-- Code syntax highlighting -->
		<link rel="stylesheet" href="{pathRevealApp}/lib/css/zenburn.css"></link>

		<!-- Printing and PDF exports -->
		<script>
			var link = document.createElement( 'link' );
			link.rel = 'stylesheet';
			link.type = 'text/css';
			link.href = window.location.search.match( /print-pdf/gi ) ? '{pathRevealApp}/css/print/pdf.css' : '{pathRevealApp}/css/print/paper.css';
			document.getElementsByTagName( 'head' )[0].appendChild( link );
		</script>

		<!--[if lt IE 9]>
		<script src="{pathRevealApp}/lib/js/html5shiv.js"></script>
		<![endif]-->
	</head>

	<body>
<div class="reveal">
<div class="slides">
</div>
</div>
<aside id="presentable-icon" class="revealjs">
<a title="Table of Contents" href="#/1">
<img alt="Table of Contents" src="{pathRevealApp}/plugin/presentable/icons/impressjs.png" href="#/1"/>
</a>
</aside>
<script src="{pathRevealApp}/lib/js/head.min.js"></script>
<script src="{pathRevealApp}/js/reveal.js"></script>
<script>

			Reveal.initialize({
				controls: true,
				progress: true,
				history: true,
				center: true,
				slideNumber: true,
				mouseWheel: false,
				transition: 'zoom', // none/fade/slide/convex/concave/zoom

				// Optional reveal.js plugins
				dependencies: [
					{ src: '{pathRevealApp}/lib/js/classList.js', condition: function() { return !document.body.classList; } },
					{ src: '{pathRevealApp}/plugin/highlight/highlight.js', async: true, callback: function() { hljs.initHighlightingOnLoad(); } },
					{ src: '{pathRevealApp}/plugin/notes/notes.js', async: true },
					{ src: '{pathRevealApp}/plugin/math/math.js', async: true },
					{ src :'{pathRevealApp}/plugin/presentable/presentable.min.js' , async: true , callback : function(){presentable.toc({framework: "revealjs"});}}
				]

			});


		</script>

	</body>
</html>

"""


def generateHtmlFile():
    html = html_doc.replace("{pathRevealApp}","revealApp")
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
    return soup