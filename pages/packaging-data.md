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

	<div class="stakeholders-container">
		<h1>Stakeholders</h1>
		<div style="width: fit-content; margin: auto;">
			<a title="Access and information on materials: Industrial Packaging"
				href="https://www.industrialpackaging.com/">
				<img src="/assets/stakeholders/Industrial-Packaging.png" alt="Industrial Packaging" />
			</a>
			<a title="FEFCO" href="https://www.fefco.org/">
				<img src="/assets/stakeholders/fefco.png" alt="FEFCO" />
			</a>
			<a title="European Organization for Packaging and the Environment"
				href="https://europen-packaging.eu/about-us.html">
				<img src="/assets/stakeholders/europen.png" alt="Europen" />
			</a>
		</div>
	</div>

	<div class="resources-container">
		<h1>Useful resources</h1>
		<ul>
			<li>
				<a class="underlined"
					href="https://op.europa.eu/en/publication-detail/-/publication/bb3ec82e-9a9f-11e6-9bca01aa75ed71a1">
					The impact of the use of "oxo-degradable" plastic on the environment
				</a>
			</li>

			<li>
				<a class="underlined"
					href="https://op.europa.eu/en/publication-detail/-/publication/05a3dace-8378-11ea-bf12-01aa75ed71a1/language-en/format-PDF/source-159275885">
					Effectiveness of the essential requirements for packaging and packaging waste and proposals
					for reinforcement
				</a>
			</li>

			<li>
				<a class="underlined"
					href="https://op.europa.eu/en/publication-detail/-/publication/3fde3279-77af-11ea-a07e01aa75ed71a1/language-en/format-PDF/source-159279986">
					Relevance of biodegradable and compostable consumer plastic products and packaging in a circular
					economy
				</a>
			</li>

			<li>
				<a class="underlined" href="https://www.eea.europa.eu/publications/eea_report_2005_3">
					Effectiveness of packaging waste management systems in selected countries: an EEA pilot study.
				</a>
			</li>
		</ul>


	</div>
</div>