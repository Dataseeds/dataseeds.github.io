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