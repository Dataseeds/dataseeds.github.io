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
		<p>
			<span class="temp">
			Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam a pharetra orci. Curabitur orci eros, auctor tristique auctor luctus, ultricies sed risus. Phasellus gravida orci in turpis lacinia varius. Mauris consequat erat risus, finibus malesuada diam auctor ac. Aenean non sem ex. Vivamus in libero purus. Morbi blandit, nisl non iaculis ultricies, orci nunc interdum turpis, eu tristique quam nunc ut lorem. Quisque pharetra ac leo et consequat.
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
		valueNames: ["name", "tags", { name: "link", attr: "href" } ],
		item: '<li><a class="link"><h3 class="name"></h3><p class="tags"></p></li>',
		page: 12,
  		pagination: true
	};

	var values = [
	{
		name: "Communication from the Commission to the European Parliament, the European Council, the Council, the European Economic and Social Committeee and the Committee of the Regions. The European Green Deal. COM/2019/640 final",
		tags: ["European Green Deal", "climate change", "natural capital", "green economy"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52019DC0640"
	}, { 
		name: "Regulation (EC) No 2150/2002 of the European Parliament and of the Council of 25 November 2002",
		tags: ["waste", "statistics", "recovery", "disposal", "data collection"],
		link: "https://eur-lex.europa.eu/legal-content/en/ALL/?uri=CELEX:32002R2150"
	}, { 
		name: "Commission Regulation (EU) No 849/2010 of 27 September 2010 amending Regulation (EC) No 2150/2002 of the European Parliament and of the Council on waste statistics",
		tags: ["waste", "statistics", "recovery", "disposal", "data collection"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:32010R0849"
	}, {
		name: "Directive 2008/98/EC of the European Parliament and of the Council of 19 November 2008 on waste and repealing certain Directives",
		tags: ["waste", "recycling", "public health", "pollution", "environmental protection"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02008L0098-20180705"
	}, {
		name: "Regulation (EC) No 1013/2006 of the European Parliament and of the Council of 14 June 2006 on shipments of waste",
		tags: ["intra-EU trade", "hazardous waste", "export of waste", "environmental protection", "administrative formalities", "waste management"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006R1013"
	}, {
		name: "Commission Decision (EU) No 2014/955/EU of 18 December 2014 amending Decision 2000/532/EC on the list of waste pursuant to Directive 2008/98/EC of the European Parliament and of the Council",
		tags: ["classification", "dangerous substance", "waste management", "technical specification", "hazardous waste"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014D0955"
	}, {
		name: "Commission Regulation (EU) No 1357/2014 of 18 December 2014 replacing Annex III to Directive 2008/98/EC of the European Parliament and of the Council on waste and repealing certain Directives",
		tags: ["hazardous waste", "chemical product", "classification", "dangerous substance"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R1357"
	}, {
		name: "Waste Prevention - Handbook: Guidelines on waste prevention programmes",
		tags: ["waste prevention", "guidance", "strategies", "initiatives", "setting priorities"],
		link: "https://ec.europa.eu/environment/waste/prevention/pdf/Waste%20prevention%20guidelines.pdf"
	}, {
		name: "Communication from the Commission to the European Parliament, the Council, the European Economic and Social Committee and the Committee of the Regions. A new Circular Economy Action Plan for a cleaner and more competitive Europe. COM/2020/98 final",
		tags: ["circular economy", "sustainable products", "production", "packaging", "plastics", "food", "water", "nutrients", "waste prevention", "innovation"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1583933814386&uri=COM:2020:98:FIN"
	}, {
		name: "European Parliament and Council Directive 94/62/EC of 20 December 1994 on packaging and packaging waste",
		tags: ["waste recycling", "packaging", "pollution", "prevention", "environmental protection", "heavy metal", "waste prevention"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01994L0062-20180704"
	}, {
		name: "Council Directive of 12 June 1986 on the protection of the environment, and in particular of the soil, when sewage sludge is used in agriculture (86/278/EEC)",
		tags: ["approximation of laws", "environmental protection", "soil conditioning", "pollution", "agriculture", "soil protection", "sewage sludge"],
		link: "https://eur-lex.europa.eu/eli/dir/1986/278/2018-07-04"
	}, {
		name: "Communication from the Commission to the European Parliament, the Council, the European Economic and Social Committee and the Committee of the Regions. A European Strategy for Plastics in a Circular Economy",
		tags: ["plastic", "packaging", "circular economy", "strategy", "environmental protection", "waste generation"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1516265440535&uri=COM:2018:28:FIN"
	}, {
		name: "Commission notice on technical guidance on the classification of waste (2018/C 124/01)",
		tags: ["technical guidance", "classification", "waste", "hazardous waste", "non-hazardous waste"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.C_.2018.124.01.0001.01.ENG&toc=OJ:C:2018:124:TOC"
	}];

	var userList = new List('search-list', options, values);
</script>

