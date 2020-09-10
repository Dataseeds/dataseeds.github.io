---
layout: page
title: Processing & Packaging
visible: false
permalink: /packaging/legislations
---

<script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>

<div>
	<div class="centered-title" onclick="location.href='/production'" style="cursor: pointer;">
		<img src="/assets/icons/DrawKit-Ecology/Color/Label.svg">
		<h1>{{ page.title }}</h1>
		<img src="/assets/icons/DrawKit-Ecology/Color/Leaves.svg">
	</div>
	<div class="flex-container">
		<p>
			<span class="temp">
				Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam a pharetra orci. Curabitur orci eros,
				auctor tristique auctor luctus, ultricies sed risus. Phasellus gravida orci in turpis lacinia varius.
				Mauris consequat erat risus, finibus malesuada diam auctor ac. Aenean non sem ex. Vivamus in libero
				purus. Morbi blandit, nisl non iaculis ultricies, orci nunc interdum turpis, eu tristique quam nunc ut
				lorem. Quisque pharetra ac leo et consequat.
			</span>
		</p>
		<div id="search-list">
			<div class="searchbox">
				<input class="search" placeholder="Search" />
				<button class="sort" data-sort="name">Sort ↑↓</button>
			</div>
			<ul class="list"></ul>
			<ul class="pagination"></ul>
		</div>
	</div>

</div>


<script>
	var options = {
		valueNames: ["name", "tags", { name: "link", attr: "href" }],
		item: '<li><a class="link"><h3 class="name"></h3><p class="tags"></p></li>',
		page: 12,
		pagination: true
	};

	var values = [
		{
			name: "Directive (EU) 2015/2302 On package travel and linked travel arrangements",
			tags: ["package", "travel", "packaging"],
			link: "https://lexparency.org/eu/32015L2302/"
		}, {
			name: "Commission Implementing Directive 2014/96/EU on the requirements for the labelling, sealing and packaging of fruit plant propagating material and fruit plants intended for fruit production, falling within the scope of Council Directive 2008/90/EC",
			tags: ["requirements", "labelling", "sealing", "packaging"],
			link: "https://lexparency.org/eu/32014L0096/"
		}, {
			name: "Commission Implementing Decision (EU) 2020/1073 Granting a derogation requested by the Netherlands pursuant to Council Directive 91/676/EEC concerning the protection of waters against pollution caused by nitrates from agricultural sources",
			tags: ["water", "pollution", "processing", "nitrates"],
			link: "https://lexparency.org/eu/32020D1073/"
		}, {
			name: "Commission Regulation (EU) 2019/759 laying down transitional measures for the application of public health requirements of imports of food containing both products of plant origin and processed products of animal origin (composite products)",
			tags: ["public health", "processing", "imports", "agriculture"],
			link: "https://lexparency.org/eu/32019R0759/"
		}
	];

	var legislationsList = new List('search-list', options, values);
</script>