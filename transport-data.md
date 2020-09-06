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
	<div class="data-flex-container">
		<p>
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam a pharetra orci. Curabitur orci eros, auctor tristique auctor luctus, ultricies sed risus. Phasellus gravida orci in turpis lacinia varius. Mauris consequat erat risus, finibus malesuada diam auctor ac. Aenean non sem ex. Vivamus in libero purus. Morbi blandit, nisl non iaculis ultricies, orci nunc interdum turpis, eu tristique quam nunc ut lorem. Quisque pharetra ac leo et consequat.
		</p>
		<p>
			Morbi consequat eros sit amet lacus bibendum rhoncus. Proin eros neque, volutpat a massa vel, iaculis sagittis purus. Phasellus leo nunc, ultricies eu enim sit amet, rutrum sagittis lacus.
		</p>
		<p style="font-style: italic;">
			<span>
				Dataset:
				<a class="underlined"
				   href="https://www.eea.europa.eu/data-and-maps/daviz/change-in-final-energy-consumption-5#tab-chart_3">Change in energy consumption by transport mode - eea.europa.eu</a>
			</span>
		</p>
	</div>
	<div style="max-width: 900px; margin: auto">
		{% include_relative vis/transport.html %}
	</div>
</div>
