---
layout: page
title: Finance & Innovation
visible: true
permalink: /finance
---

<div class="finance">
	<div class="centered-title">
		<img src="/assets/icons/DrawKit-SaaS/Color/Binocular.svg">
		<h1>{{ page.title }}</h1>
		<img src="/assets/icons/DrawKit-SaaS/Color/Binocular.svg" style="transform: scaleX(-1);">
	</div>
	<div class="flex-container">
		<p>
			In this section, you will be able to find <span class="highlighted">information about the European funds
				destined towards agricultural reform and how they have been spent</span> by every Member State. The map
			showcases the amount agreed to for every state until 2023, what was finally allocated to each state, as well
			as, how much of it has been spent so far. Through this page you can also, access the CORDIS database where
			agricultural innovation projects of interest being carried out through Europe are shown in an interactive
			map.
		</p>
		<p style="font-style: italic;">
			<span>
				Dataset:
				<a class="underlined" href="https://cohesiondata.ec.europa.eu/funds/eafrd">European Agricultural Fund
					for Rural Development - cohesiondata.ec.europa.eu</a>
			</span>
		</p>

		<div class="grid-table-container">
			<div class="grid-table">
				<a href="javascript:void(0)" onclick="openTab(event, 'Tab-Pie');">
					<div class="tablink tablink-active">Pie chart</div>
				</a>
				<a href="javascript:void(0)" onclick="openTab(event, 'Tab-Map');">
					<div class="tablink">Map</div>
				</a>
			</div>

			<div id="Tab-Pie" class="tab-content" style="display:block">
				<h2>Total Budget by Theme of the European Agricultural Fund for Rural Development</h2>
				<h3>In billion EUR (ESIF 2020)</h3>
				<div class="legend-container">
					<div class="rectangle-container">
						<div style="background: #abddcf"></div>
						<p>Competitiveness of SMEs</p>
					</div>
					<div class="rectangle-container">
						<div style="background: #92d3c1"></div>
						<p>Environment Protection & Resource Efficiency</p>
					</div>
					<div class="rectangle-container">
						<div style="background: #6ec5ac"></div>
						<p>Climate Change Adaptation & Risk Prevention</p>
					</div>
					<div class="rectangle-container">
						<div style="background: #56bb9e"></div>
						<p>Social Inclusion</p>
					</div>
					<div class="rectangle-container">
						<div style="background: #44ab8d"></div>
						<p>Low-Carbon Economy</p>
					</div>
					<div class="rectangle-container">
						<div style="background: #3b9279"></div>
						<p>Research & Innovation</p>
					</div>
					<div class="rectangle-container">
						<div style="background: #317a65"></div>
						<p>Technical Assistance</p>
					</div>
					<div class="rectangle-container">
						<div style="background: #276251"></div>
						<p>Sustainable & Quality Employment</p>
					</div>
					<div class="rectangle-container">
						<div style="background: #1e4a3d"></div>
						<p>Information & Communication Technologies</p>
					</div>
					<div class="rectangle-container">
						<div style="background: #193e33"></div>
						<p>Educational & Vocational Training</p>
					</div>
					<div class="rectangle-container">
						<div style="background: #143129"></div>
						<p>Discontinued Measures</p>
					</div>
				</div>
				{% include_relative finance-piechart.html %}
			</div>

			<div id="Tab-Map" class="tab-content" style="display:none">
				<h2>Implementation by country for European Agricultural Fund for Rural Development</h2>
				<h3>Total cost of selection and spending as % of planned (ESIF 2014-2020)</h3>
				{% include_relative finance-map.html %}
			</div>

		</div>

		<p>
			<span class="temp">
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam a pharetra orci. Curabitur orci eros,
				auctor tristique auctor luctus, ultricies sed risus. Phasellus gravida orci in turpis lacinia varius.
				Mauris consequat erat risus, finibus malesuada diam auctor ac. Aenean non sem ex.
			</span>
		</p>

		<div style="place-self: center; height: 300px; width: 100%;">
			<a href="/finance/CORDIS">
				<div class="finance-img-overlay">
					<h1>CORDIS</h1>
				</div>
			</a>
		</div>
	</div>

</div>


<style>
	.loader-spinner {
		border-left: 1.1em solid #44AB8D !important;
	}

	.chart-background {
		fill: transparent !important;
	}

	.d3-scatter-chart svg {
		background-color: transparent !important;
	}

	.chart1 .color-box {
		background-color: #44AB8D !important;
	}

	.chart1 .s0,
	.chart1 .sEAFRD {
		fill: #44AB8D;
	}

	.content label,
	.content [type="checkbox"] {
		display: initial;
	}

	.ec-chart {
		padding: 0;
	}
</style>


<script>
	// var checkBarChart = setInterval(function () {
	// 	wrapper1 = document.getElementsByClassName("d3-bar-chart")[0];
	// 	chart1 = wrapper1.children[0];
	// 	if (chart1) {
	// 		clearInterval(checkBarChart);
	// 		chart1.setAttribute("viewBox", "0 0 380 1200");
	// 		chart1.setAttribute("height", "575px")
	// 	}
	// }, 100);

	// var checkCheckbox = setInterval(function () {
	// 	fixed_axes_checkbox = document.getElementsByClassName("ec-chart")[1].getElementsByTagName("input")[0]
	// 	if (fixed_axes_checkbox) {
	// 		clearInterval(checkCheckbox);
	// 		fixed_axes_checkbox.checked = false;
	// 		fixed_axes_checkbox.onchange();
	// 	}
	// }, 500);

	function openTab(evt, cityName) {
		var i, x, tablinks;
		x = document.getElementsByClassName("tab-content");
		for (i = 0; i < x.length; i++) {
			x[i].style.display = "none";
		}
		tablinks = document.getElementsByClassName("tablink");
		for (i = 0; i < x.length; i++) {
			tablinks[i].className = tablinks[i].className.replace(" tablink-active", "");
		}
		document.getElementById(cityName).style.display = "block";
		evt.currentTarget.firstElementChild.className += " tablink-active";
	}
</script>