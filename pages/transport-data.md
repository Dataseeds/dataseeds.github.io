---
layout: page
title: Sustainable transport
visible: false
permalink: /transport/data
---

<div>
	<div class="centered-title" onclick="location.href='/transport'" style="cursor: pointer;">
		<img src="/assets/icons/DrawKit-Ecology/Color/Gas Station.svg">
		<h1>{{ page.title }}</h1>
		<img src="/assets/icons/DrawKit-Ecology/Color/Gas Station.svg" style="transform: scaleX(-1);">
	</div>
	<div class="flex-container">
		<p>
			<span class="highlighted">How much do food miles matter when it comes to carbon emissions?</span> The role of transportation and logistics, both crucial in increasing food security and mitigating climate change, is a key element to consider when applying political ecology. Yet, <span class="highlighted">decreasing geographical distance does not always mean better transportation</span>. Other matters as cold storage facilities and transport refrigeration units are crucial parts to consider. At the same time, the more agents are involved between harvest and table, the less incentive there is for each agent to control costs and food losses.
		</p>
		<p>
			<span class="temp">
				In this context, Dataseeds considers two specific pillars to feed the future through a more sustainable transport logistic: First, to encourage a less carbon-intensive value chains. Second, to improve agro-logistics by reducing the costs as well as food losses. 
			</span>
		</p>
		<p style="font-style: italic;">
			<span>
				Dataset:
				<a class="underlined"
					href="https://www.eea.europa.eu/data-and-maps/daviz/change-in-final-energy-consumption-5#tab-chart_3">Change
					in energy consumption by transport mode - eea.europa.eu</a>
			</span>
		</p>
	</div>
	<div style="max-width: 57rem; margin: auto">
		{% include_relative transport-graph.html %}
	</div>
</div>
