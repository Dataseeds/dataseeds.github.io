---
layout: page
title: EU Citizens' opinions
visible: true
permalink: /citizens/
---

<div class="citizens">
	<div class="centered-title">
		<img src="/assets/icons/DrawKit-SaaS/Color/Feedback Audience.svg">
		<h1>{{ page.title }}</h1>
		<img src="/assets/icons/DrawKit-SaaS/Color/Feedback Audience.svg" style="transform: scaleX(-1);">
	</div>

	<div class="citizens-flex-container">
		<div class="citizen-hero-card"
			onclick='location.href="https://ec.europa.eu/commfrontoffice/publicopinion/index.cfm"'
			style="cursor: pointer;"> <img src="/assets/citizens/eurobarometer.png">
			<div class="citizen-hero-card-info">
				<h2>Eurobarometer</h2>
				<p> The distinct advantage of the Eurobarometer is that collected data gives us a general
					picture of the existing dynamics within the EU regarding several topics.
					Attitudes and opinions of European citizens figure on these surveys and might
					be of great interest for SMEs to check the current trends on climate change
					action or sustainable consumption and production. Click here to go to the official website to find
					surveys with a broad scope. </p>
			</div>
		</div>

		<p>
		EU Datathon event is part of the European Week of Regions and Cities which attracts more than 9,000 participants. This way, we feel it is a great chance to make your voice heard and build better and more substantial bridges between the European Union, European agriculture and citizens. For this reason, we have contacted experts from different areas (business, IT, research and activism) to comment on their views regarding the future of Europe. Is open data a tool or a road towards a stronger European agriculture? What does agriculture need in this difficult times of coronavirus and climate change?
		</p>

		<ul class="post-list">
			{% for post in site.citizens reversed %}
			{% if post.visible != false  %}
			<li>
				<a class="citizen-card-link" href="{{ post.url | prepend: site.baseurl }}">
					<div class="img-color-overlay">
						<img src="{{ post.img }}">
					</div>
					<div class="citizen-card-info">
						<h2>{{ post.title }}</h2>
						<p>{{ post.description }}</p>
					</div>
				</a>
			</li>
			{% endif  %}
			{% endfor %}
		</ul>

	</div>


</div>
