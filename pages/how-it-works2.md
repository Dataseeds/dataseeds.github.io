---
layout: page
title: How it works
visible: false
permalink: /about/how-it-works2
---

<body>
	<div class="how-it-works">
		<div class="centered-title">
			<img src="/assets/icons/DrawKit-SaaS/Color/Development.svg">
			<h1>{{ page.title }}</h1>
			<img src="/assets/icons/DrawKit-SaaS/Color/Development.svg" style="transform: scaleX(-1);">
		</div>
	</div>

	<div class="about-flex-container">
		<h2>Frontend stack</h2>
		<p>
			The frontend of the page is made with the usual web technologies of <b>HTML + CSS + JS</b>. But apart from
			that, <b>Jekyll</b> was also used, which is a great open
			source static site generator. This let us concentrate more on the contents of the page as it eased managing
			dozens of static pages, and also allowed us to use Markdown for blog posts and Liquid in HTML for a less
			tedious coding.
		</p>

		<img src="/assets/JekyllHTML_stack.png"
			style="width: 65%; max-width: 22rem; margin: auto; display: flex; padding-bottom: 1rem;" />

		<p>
			The webpage is totally open sourced in our <a class="underlined"
				href="https://github.com/Dataseeds/dataseeds.github.io">Github repo</a>
			and is also hosted there thanks to the amazing (and free) GitHub Pages, which is a static site hosting
			service that comes together perfectly with Jekyll (which the cofounder of GitHub created).
		</p>

		<h2>Data visualization</h2>
		<p>
			The webpage wouldn't be the same without the maps, charts and visualizations scattered around the
			different sections. Each one of them was created from scratch with datasets from the EU Open Data Portal.
		</p>

		<p>
			Finally, the data was processed and explored in Python with the Pandas library, and then a graph was
			created around the chosen data. All the graphs and charts were made with the <a class="underlined"
				href="https://plotly.com/python/">Plotly library</a>, which is a wonderful interactive graphing library
			for Python .
		</p>

		<h2>Used sources</h2>
		<p>
			This page wouldn't be the same without all the amazing open source libraries and frameworks used to create
			and manage both the website and the content. But a special thanks need to be provided to the amazing
			vectorized icons from <href class="underlined" src="https://www.drawkit.io/free-icons">Drawkit</href>, and
			the entirety of the datasets and information collected from a variety of sources: <a class="underlined"
				href="https://www.eea.europa.eu/">EEA</a>, <a class="underlined"
				href="https://ec.europa.eu/eurostat/home?">Eurostat</a>, <a class="underlined"
				href="https://eur-lex.europa.eu/homepage.html?locale=es">EUR-lex</a>, <a class="underlined"
				href="https://www.eib.org/en/index.htm">EIB</a>, <a class="underlined"
				href="https://cordis.europa.eu/datalab/datalab.php#">CORDIS</a> and <a class="underlined"
				href="https://ec.europa.eu/jrc/en">JRC</a>.
		</p>
	</div>
</body>