---
layout: page
title: Waste prevention
visible: false
permalink: /waste/data
---

<div>
	<div class="centered-title" onclick="location.href='/waste'" style="cursor: pointer;">
		<img src="/assets/icons/DrawKit-Ecology/Color/Waste.svg">
		<h1>{{ page.title }}</h1>
		<img src="/assets/icons/DrawKit-Ecology/Color/Trash.svg">
	</div>
	<div class="flex-container">
		<p>
			An important element in circular economies is waste reduction and waste management. Yet waste prevention is
			the most desirable option. The success of the EU moving towards a green economy thus rests to a large extent
			on conducting research and giving priority to monitoring and choosing adapted solutions to achieve a
			sustainable production avoiding food losses and pollution. EU open data on waste management is beneficial to
			optimise existing techniques and mechanisms by using the information different EU institutions and agencies
			have stored. SMEs can use it to enhance their waste models to move through the path of a circular economy
			hand in hand with EU principles, innovation and resources. Waste prevention will contribute to the efforts
			made to comply with several Sustainable Development Goals (SDGs) and the Agenda 2030. Production patterns
			need to move towards a responsible and circular model (SDG 12) to protect Life on land (SDG 15) and as a way
			of reducing climate change negative impacts (SDG 13).
		</p>
		<p>
			The map below allows for a quick overview of the amount of waste produced per country per year. Moreover,
			the interactive map also gives access to the most recent reports on
			<a class="underlined" href="https://www.eea.europa.eu/themes/waste/waste-prevention/countries">
				waste reduction</a> and
			<a class="underlined"
				href="https://www.eionet.europa.eu/etcs/etc-wmge/products/country-factsheets-on-resource-efficiency-and-circular-economy-in-europe">
				resource efficiency</a>, which are available by clicking on the country of interest. These reports are
			based on a revision of existing national and regional waste prevention programmes, and information on
			resource efficiency, circular economy and raw material supply policies. For more information on the general
			progress made towards waste prevention in the EU, take a look at the
			<a class="underlined" href="https://www.eea.europa.eu/themes/waste/waste-prevention">
				Annual reviews</a> from the European Environmental Agency (EEA). More details on waste reduction on the
			agriculture sector might be found
			<a class="underlined" href="http://www.fao.org/platform-food-loss-waste/en/">
				here</a> at the Technical Platform on the Measurement and Reduction of Food
			Loss and Waste from the Food and Agriculture Organisation (FAO). The database includes data and information
			on food losses and waste from different countries (including EU member states), at all stages of the value
			chain and across food products.
		</p>
		<p style="font-style: italic;">
			<span>Dataset:
				<a class="underlined" href="#">EEA, Eurostat, EU Publications Office.</a>
			</span>
		</p>
	</div>
	<div style="max-width: 44rem; margin: auto">
		{% include_relative waste-graph.html %}
	</div>

	<p>
		Underneath the map, two folders give access to different reports on waste‐related challenges and best
		practices across the EU. The folder on the left gathers reports made by the European Publications Office,
		the European Commission, the European Environment Agency and the EU Platform on Food Losses and Food Waste.
		On the right, several partnerships and online networks can be found.
	</p>

	<div class="extrainfo-container">
		<div class="centered-title">
			<h1>Stakeholders</h1>
		</div>
		<div class="extrainfo-wrapper">
			<ul>
				<li>
					<img src="/assets/stakeholders/test.png">
					<div class="extrainfo-text">
						<h4>Bio-waste in Europe – turning challenges into opportunities (2020)</h4>
						<p>
							Bio-waste generation, prevention, collection and treatment have interesting opportunities to
							turn existing challenges into benefits (of moving towards a circular economy). This report
							explains the relevance of bio-waste and a quality management of compost and digestate. A
							section is dedicated to innovation and future related developments in Europe.<br>
							<br>
							Source: <a class="underlined" href="https://www.eea.europa.eu/">European Environment
								Agency</a>.
						</p>
						<button href="#">
							Learn more
						</button>
						<a href="#"></a>
					</div>
				</li>
			</ul>
		</div>
	</div>
</div>