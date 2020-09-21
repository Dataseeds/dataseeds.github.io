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

		{% for project in site.citizens %}
		<div class="citizen-card">
			<div class="img-color-overlay">
				<img src="{{ project.img }}">
			</div>
			<br />
			<h2>{{ project.title }}</h2>
			<p>{{ project.description }}</p>
		</div>
		{% endfor %}

	</div>


</div>