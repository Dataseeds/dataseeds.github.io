---
layout: page
title: Processing & Packaging
visible: false
permalink: /packaging/data
---

<div>
	<div class="centered-title" onclick="location.href='/packaging'" style="cursor: pointer;">
		<img src="/assets/icons/DrawKit-Ecology/Color/Eco Tag.svg">
		<h1>{{ page.title }}</h1>
		<img src="/assets/icons/DrawKit-Ecology/Color/Paper bag.svg">
	</div>
	<div class="flex-container">
		<p>
			Reducing single-use packaging materials aligns with Sustainable Development Goal (SDG)
			number 12 on Recycling Paper, Plastic, Glass and Aluminium for a More Responsible
			Consumption and Production, which contributes to building a more responsible agriculture and
			making more environmentally friendly products available to consumers. The European Union is
			one of the main promoters of the ecological transition, and this is reflected in the data from
			recent years. The figures below show recent statistics of <span class="highlighted">packaging waste in the
				26 European Union Member States and the United Kingdom</span>. It summarises the development of
			packaging waste production and recycling during the 2005-2016 period.
		</p>
		<p style="font-style: italic;">
			<span>Dataset:
				<a class="underlined"
					href="https://www.eea.europa.eu/data-and-maps/daviz/sds/packaging-waste-recycling-2/@@view">Packaging
					waste recycling (eea.europa.eu)</a>
			</span>
		</p>
	</div>
	<div style="max-width: 57rem; margin: auto">
		{% include_relative packaging-graph.html %}
	</div>

</div>