---
layout: page
title: Waste management
visible: false
permalink: /waste/legislations
---

<script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>

<div>
	<div class="centered-title" onclick="location.href='/waste'" style="cursor: pointer;">
		<img src="/assets/icons/DrawKit-Ecology/Color/Waste.svg">
		<h1>{{ page.title }}</h1>
		<img src="/assets/icons/DrawKit-Ecology/Color/Trash.svg">
	</div>
	<div class="flex-container">
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
		valueNames: [
			"name",
			"tags",
			{ name: "link", attr: "href" } ],
		item: '<li><a class="link"><h3 class="name"></h3><p class="tags"></p></li>',
		page: 5,
  		pagination: true
	};

	var values = [
	{
		name: "VAT directive",
		tags: ["VAT"],
		link: "https://lexparency.org/eu/32006L0112/"
	}, 
	{ 
		name: "Regulation (EU) 2016/679 — General Data Protection Regulation (GDPR)",
		tags: ["privacy", "GDPR"],
		link: "https://lexparency.org/eu/GDPR/"
	},
	{
		name: "Benchmarks Regulation  – BMR",
		tags: ["2986"],
		link: "https://lexparency.org/eu/32016R1011/"
	},
	{
		name: "Payment Services Directive (PSD II)",
		tags: ["Pay", "Payments"],
		link: "https://lexparency.org/eu/32015L2366/"
	}
	];

	var userList = new List('search-list', options, values);
</script>

