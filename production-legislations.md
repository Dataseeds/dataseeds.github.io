---
layout: page
title: Clean & Efficient Production
visible: false
permalink: /production/legislations
---

<script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>

<div>
	<div class="centered-title" onclick="location.href='/production'" style="cursor: pointer;">
		<img src="/assets/icons/DrawKit-Ecology/Color/Label.svg">
		<h1>{{ page.title }}</h1>
		<img src="/assets/icons/DrawKit-Ecology/Color/Leaves.svg">
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
		page: 10,
  		pagination: true
	};

	var values = [
	{
		name: "Regulation (EC) No 66/2010 EU Ecolabel",
		tags: ["efficient production", "sustainable agriculture", "Ecolabel"],
		link: "https://eur-lex.europa.eu/eli/reg/2010/66/2017-11-14"
	}, 
	{ 
		name: "Council Regulation (EC) No 834/2007 on organic production and labelling of organic products and repealing Regulation (EEC) No 2092/91",
		tags: ["organic production", "sustainable agriculture", "organic farming", "processed food"],
		link: "http://data.europa.eu/eli/reg/2007/834/2013-07-01"
	},
	{
		name: "Commission Regulation (EC) No 889/2008 laying down detailed rules for the implementation of Council Regulation (EC) No 834/2007",
		tags: ["organic production", "commission regulation", "organic farming"],
		link: "http://data.europa.eu/eli/reg/2008/889/2020-01-07"
	},
	{
		name: "Commission Implementing Regulation (EU) 2020/464 laying down certain rules for the application of Regulation (EU) 2018/848",
		tags: ["retroactive recognition", "agricultural conversion", "farm conversion", "organic production", "organic farming"],
		link: "http://data.europa.eu/eli/reg_impl/2020/464/oj"
	},
	{
		name: "Regulation (EU) No 1303/2013",
		tags: ["European Regional Development Fund", "European Social Fund", "Cohesion Fund", "EAFDR", "European Maritime and Fisheries Fund", "sustainable agriculture", "rural development"],
		link: "http://data.europa.eu/eli/reg/2013/1303/2020-07-18"
	},
	{
		name: "Regulation (EU) No 1305/2013",
		tags: ["EAFDR", "rural development"],
		link: "http://data.europa.eu/eli/reg/2013/1305/2020-06-26"
	},
	{
		name:"Commission Delegated Regulation (EU) No 807/2014",
		tags: ["EAFDR", "young farmers", "farm development", "agri-environment-climate", "funding"],
		link: "http://data.europa.eu/eli/reg_del/2014/807/2018-01-01"
	}
	];

	var legislationsList = new List('search-list', options, values);
</script>

