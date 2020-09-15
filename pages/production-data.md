---
layout: page
title: Resource efficiency
visible: false
permalink: /production/data
---

<div>
	<div class="centered-title" onclick="location.href='/production'" style="cursor: pointer;">
		<img src="/assets/icons/DrawKit-Ecology/Color/Label.svg">
		<h1>{{ page.title }}</h1>
		<img src="/assets/icons/DrawKit-Ecology/Color/Leaves.svg">
	</div>
	<div class="flex-container">
		<p>
			Resource efficiency means utilizing the Earth’s resources sustainably, to avoid as much impact on the
			environment as possible. A resource-efficient Europe is one of the Europe 2020 initiatives to achieve
			sustainable growth in European states. Part of the strategy is the transition towards a Circular Economy
			which promotes the reuse of resources rather than the simple extraction and discarding of a linear
			economy.
		</p>

		<p>
			The following map offers a representation of the Resource efficiency lead indicator: Resource
			productivity. Resource productivity quantifies the relation between economic activity – expressed in GDP
			- and the consumption of material resources - measured as DMC which is an indicator derived from
			economy-wide material flow accounts.
		</p>

		<p>
			Domestic Material Resources (DMC) measures the total amount, in tonnes, of material directly used in an
			economy. At the same time, DMC is the amount of materials that become part of the material stock within
			the economy or are released back to the environment in form of e.g. emissions to air.
			Resource Productivity, then, is defined here as GDP divided by DMC. It is important to note that GDP is
			expressed in different measurement units, of which the following are used to calculate three different
			resource productivity ratios. Please, ensure you are choosing the correct one for your analysis:
		</p>

		<ul style="margin-left: 15px">
			<li>
				<p><b>Euro per kilogram using current price data for GDP:</b> which could be used when analysing a
					single
					economy at one point in time (for one particular year).
				</p>
			</li>
			<li>
				<p><b>Euro per kilogram using chain-linked volume data for GDP:</b> to be used for analysing
					developments in
					real terms over time.
				</p>
			</li>
			<li>
				<p><b>As an index (2000=100):</b> based on GDP in chain-linked volumes normalized to 2010 prices, for
					comparing the values in different years to a previous value (year 2000).
				</p>
			</li>
			<li>
				<p><b>PPS per kilogram</b> using current price data for GDP expressed in purchasing power standards
					(PPS); PPS are artificial currency units that remove differences in purchasing power between
					economies by taking account of price level differences; these can be used when comparing across
					different economies at one point in time (for one particular year).
				</p>
			</li>
		</ul>

		<p style="font-style: italic;">
			<span>Dataset:
				<a class="underlined"
					href="https://ec.europa.eu/eurostat/tgm/table.do?tab=table&init=1&plugin=0&language=en&pcode=t2020_rl100&tableSelection=1">
					Resource productivity (eurostat)</a>
			</span>
		</p>
	</div>
	<div style="max-width: 57rem; margin: auto">
		{% include_relative production-graph.html %}
	</div>

</div>