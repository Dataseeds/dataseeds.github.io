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
		In order for the European Union to reach its climate-neutral objectives, existing goals need to be accompanied by innovative and ambitious legislative and non-legislative actions. This broad scope of actions includes <i>inter alia</i> policy proposals and new legal acts – some are binding, others are not. Moreover, not all actions apply to all EU countries, or in the same way. Hereafter you will be able to find legislative and non-legislative documents on <b>processing and packaging</b>.
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
