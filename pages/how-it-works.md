---
layout: page
title: How it works
visible: false
permalink: /about/how-it-works
---
<head>
    <style type="text/css">
		//Text Styles
@import url("https://fonts.googleapis.com/css?family=Open+Sans:400,400i,700");
$font-sans: 'Open Sans', sans-serif;

//Colors
$black: #34435E;
$white: #ffffff;

body {
  font-family: $font-sans;
  margin: 0;
  padding: 0 4em;
}

main {
  min-width: 300px;
  max-width: 500px;
  margin: auto;
}

p {
  font-size: 1em;
  line-height: 1.75em;
  border-top: 3px solid;
  border-image: linear-gradient(to right, #743ad5 0%, #d53a9d 100%);
  border-image-slice: 1;
  border-width: 3px;
  margin: 0;
  padding: 40px;
  counter-increment: section;
  position: relative;
  color: $black;

  //numbers
  &:before {
    content: counter(section);
    position: absolute;
    border-radius: 50%;
    padding: 10px;
    height: 1.25em;
    width: 1.25em;
    background-color: $black;
    text-align: center;
    line-height: 1.25em;
    color: $white;
    font-size: 1em;
  }
}
//odd number borders
p:nth-child(odd) {
  border-right: 3px solid;
  padding-left: 0;

  &:before {
    left: 100%;
    margin-left: -20px;
  }
}
//even number borders
p:nth-child(even) {
  border-left: 3px solid;
  padding-right: 0;

  &:before {
    right: 100%;
    margin-right: -20px;
  }
}
//handle first and last
p:first-child {
  border-top: 0;
  border-top-right-radius:0;
  border-top-left-radius:0;
}
p:last-child {
  border-bottom-right-radius:0;
  border-bottom-left-radius:0;
}
    </style>
</head>

<body>
<div class="how-it-works">
	<div class="centered-title">
		<img src="/assets/icons/DrawKit-SaaS/Color/Development.svg">
		<h1>{{ page.title }}</h1>
		<img src="/assets/icons/DrawKit-SaaS/Color/Development.svg" style="transform: scaleX(-1);">
	</div>
</div>

<div class="centered-title">
  <h2>How serious are we about addressing the challenge of food security in the face of climate change? <span class="highlighted"> How does the food we buy, eat and don’t eat impact the environment?</span> Before reaching our plates, food needs to be produced, processed, packaged, and distributed. Every step uses up resources and generates more and more waste and pollution.</h2>
</div>

<div class= "info">
<main>
  <p>For instance, the role of transportation and logistics crucial in increasing food security, so we can feed 9 billion people by 2050, is responsible for up to 50% of harvest wasted between farm and fork. Transport-related emissions account for about 15% of overall greenhouse gas emissions. And 60% of those emissions are coming from road transport. Agricultural production alone accounts for 10% of greenhouse gas emissions (including 80% of methane emissions) contributing to climate change. If these are already problems to be considered, according to the European Enviroment Agency (EEA), "climate change is projected to reduce crop productivity especially in southern Europe and to improve the conditions for growing crops in northern Europe, although the negative impact of extreme events on agriculture is expected to increase"</p>

  <p>The aim of dataseeds is to help SMEs working in agriculture to have direct access to better and more detailed information regarding the coming changes in accordance to the European Green Deal and the inevitable climate change. Do you remember the avatar tree? A tree that would hold the knowledge of all its community. That is open data today. In this regard, the interface would encompass on the one hand, information and data on the production, packaging, transport, and waste processes, and on the other hand, the opinion of EU citizens as consumers. Multiple datasets are used to help SMEs reduce and control their flows concerning the Green Deal requirements – most of them are dynamic and continuously updated and some have a participatory approach.</p>

  <p>A connection between the private sector, EU institutions, and EU citizens is essential to undertake such a sustainable restructuring of the economy, and the agriculture sector cannot be left behind.</p>
  <p style="font-style: italic;">
		Datasets: EEA, Eurostat, EUR-Lex, EIB, REGIO, INEA, CORDIS, JRC. <br>
	<br>Vectorized icons from <href src="https://www.drawkit.io/free-icons">Drawkit</href>.
	</p>
</main>

<div class="centered-title">
	<h2>IT IS TIME TO <span class="highlighted">CULTIVATE</span> A BETTER FUTURE</h2>
</div>


<div class="about-sources">
	<h2>Used sources</h2>
	<p style="font-style: italic;">
		Datasets: EEA, Eurostat, EUR-Lex, EIB, REGIO, INEA, CORDIS, JRC. <br>
		<br>
		Vectorized icons from <href src="https://www.drawkit.io/free-icons">Drawkit</href>.
	</p>
</div>
</body>
