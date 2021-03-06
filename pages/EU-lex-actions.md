---
layout: page
title: EU lex actions
visible: true
permalink: /actions
---

<script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>

<div>
	<div class="centered-title">
		<img src="/assets/icons/DrawKit-SaaS/Color/Digital Agreement.svg">
		<h1>{{ page.title }}</h1>
		<img src="/assets/icons/DrawKit-SaaS/Color/Digital Agreement.svg" style="transform: scaleX(-1);">
	</div>
	<div class="flex-container">
		<p>
			In order for the European Union to reach its climate-neutral objectives, existing goals need to be
			accompanied by innovative and ambitious legislative and non-legislative actions. This broad scope of
			actions includes inter alia policy proposals and new legal acts – some are binding, others are not.
			Moreover, not all actions apply to all EU countries, or in the same way. Hereafter you will be able to
			find different types of legislative and non-legislative documents.
		</p>
		<ul style="margin-left: 15px">
			<li>
				<p><b>Regulations (Article 288 TFEU)</b>
					Every regulation in force has a binding effect. It has a direct application across the EU.
				</p>
			</li>
			<li>
				<p><b>Directives (Article 288 TFEU)</b>
					A directive is a legislative act that establishes a particular objective that all EU countries much
					reach. Member States are free to choose how to achieve the goals established by the directive.
				</p>
			</li>
			<li>
				<p><b>Decisions (Article 288 TFEU)</b>
					A decision is binding in its entirety. However, it could have one or more addressees (one or several
					EU
					countries, companies or even individuals). In this case, it shall be binding on the concerned
					parties.
				</p>
			</li>
			<li>
				<p><b>Policy non-binding documents (Article 290 TFEU)</b>
					Policies are developed to benefit citizens, businesses, and other set of stakeholders. EU
					non-legislative acts of general application can be adopted or proposed to complement or amend
					non-essential elements of legislative acts. For example, a Communication is a policy document which
					relates with a particular initiative but has no legal effect.
				</p>
			</li>
		</ul>

		<p style="font-style: italic;">
			Sources: EUR-Lex, Lexparency, TFEU.
		</p>

		<div id="search-list">
			<div class="searchbox">
				<input class="search" placeholder="Search" />
				<button class="sort" data-sort="name">Sort ↑↓</button>
				<select name="type" id="typeSelector" onchange="typeChange(this.value)">
					<option value="Any type">Any type</option>
					<option value="Regulation">Regulations</option>
					<option value="Directive">Directives</option>
					<option value="Policy">Policies </option>
					<option value="Decision">Decisions </option>
				</select>
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
		page: 15,
		pagination: true
	};

	// Production (Paula)
	var vals1 = [{
		name: "Regulation (EC) No 66/2010 EU Ecolabel",
		tags: ["efficient production", "sustainable agriculture", "Ecolabel"],
		type: "Regulation",
		link: "https://eur-lex.europa.eu/eli/reg/2010/66/2017-11-14"
	}, {
		name: "Council Regulation (EC) No 834/2007 on organic production and labelling of organic products and repealing Regulation (EEC) No 2092/91",
		tags: ["organic production", "sustainable agriculture", "organic farming", "processed food"],
		type: "Regulation",
		link: "http://data.europa.eu/eli/reg/2007/834/2013-07-01"
	}, {
		name: "Commission Regulation (EC) No 889/2008 laying down detailed rules for the implementation of Council Regulation (EC) No 834/2007",
		tags: ["organic production", "commission regulation", "organic farming"],
		type: "Regulation",
		link: "http://data.europa.eu/eli/reg/2008/889/2020-01-07"
	}, {
		name: "Commission Implementing Regulation (EU) 2020/464 laying down certain rules for the application of Regulation (EU) 2018/848",
		tags: ["retroactive recognition", "agricultural conversion", "farm conversion", "organic production", "organic farming"],
		type: "Regulation",
		link: "http://data.europa.eu/eli/reg_impl/2020/464/oj"
	}, {
		name: "Regulation (EU) No 1303/2013",
		tags: ["European Regional Development Fund", "European Social Fund", "Cohesion Fund", "EAFDR", "European Maritime and Fisheries Fund", "sustainable agriculture", "rural development"],
		type: "Regulation",
		link: "http://data.europa.eu/eli/reg/2013/1303/2020-07-18"
	}, {
		name: "Regulation (EU) No 1305/2013",
		tags: ["EAFDR", "rural development"],
		type: "Regulation",
		link: "http://data.europa.eu/eli/reg/2013/1305/2020-06-26"
	}, {
		name: "Commission Delegated Regulation (EU) No 807/2014",
		tags: ["EAFDR", "young farmers", "farm development", "agri-environment-climate", "funding"],
		type: "Regulation",
		link: "http://data.europa.eu/eli/reg_del/2014/807/2018-01-01"
	}, {
		name: "General Union Environment Action Programme 'Living well, within the limits of our planet'",
		tags: ["european parliament", "EAP", "sustainable production", "resource-efficience"],
		type: "Decision",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32013D1386"
	}];

	// Packaging (Borja)
	var vals2 = [{
		name: "Directive (EU) 2015/2302 On package travel and linked travel arrangements",
		tags: ["package", "travel", "packaging"],
		type: "Directive",
		link: "https://lexparency.org/eu/32015L2302/"
	}, {
		name: "Commission Implementing Directive 2014/96/EU on the requirements for the labelling, sealing and packaging of fruit plant propagating material and fruit plants intended for fruit production, falling within the scope of Council Directive 2008/90/EC",
		tags: ["requirements", "labelling", "sealing", "packaging"],
		type: "Directive",
		link: "https://lexparency.org/eu/32014L0096/"
	}, {
		name: "Commission Implementing Decision (EU) 2020/1073 Granting a derogation requested by the Netherlands pursuant to Council Directive 91/676/EEC concerning the protection of waters against pollution caused by nitrates from agricultural sources",
		tags: ["water", "pollution", "processing", "nitrates"],
		type: "Decision",
		link: "https://lexparency.org/eu/32020D1073/"
	}, {
		name: "Commission Regulation (EU) 2019/759 laying down transitional measures for the application of public health requirements of imports of food containing both products of plant origin and processed products of animal origin (composite products)",
		tags: ["public health", "processing", "imports", "agriculture"],
		type: "Regulation",
		link: "https://lexparency.org/eu/32019R0759/"
	}, {
		name: "Directive 2008/98/EC on waste (Waste Framework Directive)",
		tags: ["packaging", "processing", "waste"],
		link: "https://ec.europa.eu/environment/waste/framework/"
	}, {
		name: "Regulation(EU) No 1308/2013 of the European Parliament and of the Council of 17 December 2013 establishing a common organisation of the markets in agricultural products and repealing Council Regulations (EEC) No 922/72, (EEC) No 234 / 79, (EC) No 1037 / 2001 and(EC) No 1234 / 2007",
		tags: ["CAP", "common agrary policy", "processing", "repealing products"],
		link: "https://ec.europa.eu/environment/waste/framework/"
	}, {
		name: "European Parliament and Council Directive 94/62/EC of 20 December 1994",
		tags: ["package", "travel", "packaging"],
		link: "https://lexparency.org/eu/31994L0062/"
	},
	{
		name: "Regulation (EC) No 1935/2004 of the European Parliament and of the Council of 27 October 2004 on materials and articles intended to come into contact with food and repealing Directives 80/590/EEC and 89/109/EEC",
		tags: ["package", "materials", "packaging"],
		link: "https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A32004R1935"
	},
	{
		name: "Commission Regulation (EC) No 2023/2006 of 22 December 2006 on good manufacturing practice for materials and articles intended to come into contact with food",
		tags: ["package", "materials", "packaging"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32006R2023"
	},
	{
		name: "Commission Regulation (EC) No 2023/2006 of 22 December 2006 on good manufacturing practice for materials and articles intended to come into contact with food",
		tags: ["package", "materials", "packaging"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex%3A32006R2023"
	}
	];


	// Waste (Andrea)
	var vals3 = [{
		name: "Communication from the Commission to the European Parliament, the European Council, the Council, the European Economic and Social Committeee and the Committee of the Regions. The European Green Deal. COM/2019/640 final",
		tags: ["European Green Deal", "climate change", "natural capital", "green economy"],
		type: "Policy",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52019DC0640"
	}, {
		name: "Regulation (EC) No 2150/2002 of the European Parliament and of the Council of 25 November 2002",
		tags: ["waste", "statistics", "recovery", "disposal", "data collection"],
		type: "Regulation",
		link: "https://eur-lex.europa.eu/legal-content/en/ALL/?uri=CELEX:32002R2150"
	}, {
		name: "Commission Regulation (EU) No 849/2010 of 27 September 2010 amending Regulation (EC) No 2150/2002 of the European Parliament and of the Council on waste statistics",
		tags: ["waste", "statistics", "recovery", "disposal", "data collection"],
		type: "Regulation",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=celex:32010R0849"
	}, {
		name: "Directive 2008/98/EC of the European Parliament and of the Council of 19 November 2008 on waste and repealing certain Directives",
		tags: ["waste", "recycling", "public health", "pollution", "environmental protection"],
		type: "Directive",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02008L0098-20180705"
	}, {
		name: "Regulation (EC) No 1013/2006 of the European Parliament and of the Council of 14 June 2006 on shipments of waste",
		tags: ["intra-EU trade", "hazardous waste", "export of waste", "environmental protection", "administrative formalities", "waste management"],
		type: "Regulation",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32006R1013"
	}, {
		name: "Commission Decision (EU) No 2014/955/EU of 18 December 2014 amending Decision 2000/532/EC on the list of waste pursuant to Directive 2008/98/EC of the European Parliament and of the Council",
		tags: ["classification", "dangerous substance", "waste management", "technical specification", "hazardous waste"],
		type: "Decision",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014D0955"
	}, {
		name: "Commission Regulation (EU) No 1357/2014 of 18 December 2014 replacing Annex III to Directive 2008/98/EC of the European Parliament and of the Council on waste and repealing certain Directives",
		tags: ["hazardous waste", "chemical product", "classification", "dangerous substance"],
		type: "Regulation",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014R1357"
	}, {
		name: "Waste Prevention - Handbook: Guidelines on waste prevention programmes",
		tags: ["waste prevention", "guidance", "strategies", "initiatives", "setting priorities"],
		type: "Policy",
		link: "https://ec.europa.eu/environment/waste/prevention/pdf/Waste%20prevention%20guidelines.pdf"
	}, {
		name: "Communication from the Commission to the European Parliament, the Council, the European Economic and Social Committee and the Committee of the Regions. A new Circular Economy Action Plan for a cleaner and more competitive Europe. COM/2020/98 final",
		tags: ["circular economy", "sustainable products", "production", "packaging", "plastics", "food", "water", "nutrients", "waste prevention", "innovation"],
		type: "Policy",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1583933814386&uri=COM:2020:98:FIN"
	}, {
		name: "European Parliament and Council Directive 94/62/EC of 20 December 1994 on packaging and packaging waste",
		tags: ["waste recycling", "packaging", "pollution", "prevention", "environmental protection", "heavy metal", "waste prevention"],
		type: "Directive",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:01994L0062-20180704"
	}, {
		name: "Council Directive of 12 June 1986 on the protection of the environment, and in particular of the soil, when sewage sludge is used in agriculture (86/278/EEC)",
		tags: ["approximation of laws", "environmental protection", "soil conditioning", "pollution", "agriculture", "soil protection", "sewage sludge"],
		type: "Directives",
		link: "https://eur-lex.europa.eu/eli/dir/1986/278/2018-07-04"
	}, {
		name: "Communication from the Commission to the European Parliament, the Council, the European Economic and Social Committee and the Committee of the Regions. A European Strategy for Plastics in a Circular Economy",
		tags: ["plastic", "packaging", "circular economy", "strategy", "environmental protection", "waste generation"],
		type: "Policy",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?qid=1516265440535&uri=COM:2018:28:FIN"
	}, {
		name: "Commission notice on technical guidance on the classification of waste (2018/C 124/01)",
		tags: ["technical guidance", "classification", "waste", "hazardous waste", "non-hazardous waste"],
		type: "Policy",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.C_.2018.124.01.0001.01.ENG&toc=OJ:C:2018:124:TOC"
	}, {
		name: "Commission Notice - EU guidelines on food donation (2017/C 361/01)",
		tags: ["food redistribution", "surplus food", "charity", "food safety", "food donation", "agricultural products"],
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=uriserv:OJ.C_.2017.361.01.0001.01.ENG&toc=OJ:C:2017:361:TOC"
	}];

	// Transport (Cristina)
	var vals4 = [{
		name: "Communication from the Commission to the Council, the European Parliament, the European Economic and Social Committee and the Committee of the Regions - Mid-term review of the Programme for the promotion of short sea shipping (COM(2003) 155 final)",
		tags: ["communication", "transport", "sea shipping", "short"],
		type: "Policy",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52006DC0380"
	}, {
		name: "Proposal for a Regulation of the European Parliament and of the Council establishing the second 'Marco Polo' programme for the granting of Community financial assistance to improve the environmental performance of the freight transport system ('Marco Polo II')(COM/2004/0478 final - COD 2004/0157)",
		tags: ["proposal", "transport", "funding", "marco polo", "freight transport"],
		type: "Policy",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52004PC0478"
	}, {
		name: "Communication from the commission to the European Parliament, the council, the European Economic and Social Committee and the Committee of the regions Towards quality inland waterway transport NAIADES II (COM/2013/0623 final)",
		tags: ["communication", "transport", "inland waterway transport"],
		type: "Policy",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52013DC0623&qid=1599669806396"
	}, {
		name: "Proposal for a COUNCIL DIRECTIVE amending Directive 1999/62/EC on the charging of heavy goods vehicles for the use of certain infrastructures, as regards certain provisions on vehicle taxation COM/2017/0276 final - 2017/0115 (CNS)",
		tags: ["proposal", "transport", "vehicle taxation"],
		type: "Policy",
		link: "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A52017PC0276"
	}, {
		name: "Directive 1999/62/EC of the European Parliament and of the Council of 17 June 1999 on the charging of heavy goods vehicles for the use of certain infrastructures",
		tags: ["1999/62", "heavy goods vehicles", "inland waterway transport"],
		type: "Directive",
		link: "https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX%3A31999L0062"
	}];

	var values = vals1.concat(vals2).concat(vals3).concat(vals4);
	var legislationsList = new List('search-list', options, values);

	function typeChange(type) {
		if (type == "Any type") {
			legislationsList.filter();
		} else {
			legislationsList.filter(function (item) {
				return (item._values.type == type);
			});
		}
	}
</script>