---
layout: page
title: Clean & Efficient Production
visible: false
permalink: /production/data
---

<div>
	<div class="centered-title" onclick="location.href='/production'" style="cursor: pointer;">
		<img src="/assets/icons/DrawKit-Ecology/Color/Label.svg">
		<h1>{{ page.title }}</h1>
		<img src="/assets/icons/DrawKit-Ecology/Color/Leaves.svg">
	</div>
	<div class="data-flex-container">
		<p>
			<span>
			Cleaner production and resource efficiency is a key element to ensure a greener and more circular economy. Often, agricultural practices, especially in SMEs, do not get to be designed specifically for the type of crop or farming that is taking place, and instead, they use standard systems. In the following map, we have compiled data from the last few years to see how resources are being used and sometimes wasted because of lack of funds.
			</span>
		</p>
		<p>
			The indicator shows the <span class="highlighted">GDP of each country divided by the domestic material consumption.</span> DMC measures the amount of materials directly used by an economy.
		</p>
		<p style="font-style: italic;">
			<span>Dataset:
				<href src="https://ec.europa.eu/eurostat/tgm/table.do?tab=table&init=1&plugin=0&language=en&pcode=t2020_rl100&tableSelection=1">eurostat</href>
			</span>
		</p>
	</div>
	<div style="max-width: 57rem; margin: auto">
		{% include_relative production-graph.html %}
	</div>

</div>





