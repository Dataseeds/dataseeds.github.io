---
layout: post-minimal

description: Simple yet powerful crypto-currency tracker for Windows 10.
img: /assets/1.jpg
---

<style>
.hero-blur-background{
	background: url('/assets/cryptotracker/hero-img.png') repeat;
	background-size: cover;
	background-attachment: fixed;
	background-position: center;
	bottom: 0;
	filter: blur(5px);
	height: 100vh;
	left: 0;
	overflow: hidden;
	position: relative;
	position: absolute;
	right: 0;
	top: 0;
	z-index: -1;
	-webkit-mask-image: linear-gradient(0deg, transparent 0%, black 100vh);
}

.hero-blur-descr{
	color: white;
	font-size: 32px;
	font-weight: 500;
	text-align: center;
}
.hero-blur-descr h1{
	font-size: 1em;
	line-height: 1.3em;
	margin: 5vw auto;
	text-align: center;
	width: 80%;
}
.hero-blur-descr img{
	margin-left: auto;
	display: block;
	margin: auto;
	margin-top: 25vh;
	width: 75%;
}
@media (max-width: 700px) {
	.hero-blur-background {	background-attachment: scroll; }
	.hero-blur-descr img{ width: 95%; }
}

@media (prefers-color-scheme: light){
	.hero-blur-descr h1{ filter: drop-shadow(1px 1px 4px white) }
	.hero-blur-descr img{ filter: drop-shadow(1px 1px 4px white) }
}
@media (prefers-color-scheme: dark){
	.hero-blur-descr h1{ filter: drop-shadow(1px 1px 4px black) }
	.hero-blur-descr img{ filter: drop-shadow(1px 1px 4px black) }
}
</style>

<div class="page-content" style="position: relative; height: 90vh; width: 100vw;">
	<div class="hero-blur-background">
	</div>
	<div class="hero-blur-descr maxwidth">
		<img id="hero-img" src="/assets/cryptotracker/logo-wide-light.png">
		<h1>Simple yet powerful cryptocurrency tracker for Windows 10</h1>
		<a href="https://www.microsoft.com/store/apps/9n3b47hbvblc?ocid=badge?cid=personal">
		<img src="https://assets.windowsphone.com/85864462-9c82-451e-9355-a3d5f874397a/English_get-it-from-MS_InvariantCulture_Default.png" alt="Get it from Microsoft" class="img-center" style="max-width: 250px; margin-top: 10vw; width: 50vw;">
	</a>
	</div>
</div>

<div class="page-content maxwidth">
	<div class="project_descr">
		<img class="project_img" id="gridRow1" src="/assets/cryptotracker/top100_light.png"/>
		<div class="project_explanation">
			<h1>Supports over 100 cryptocurrencies</h1>
			<h5>Keep up to date with Bitcoin, Ethereum, Litecoin... and over a hundred alt-coins, all supporting the main exchanges and currencies all over the world.</h5>
		</div>
	</div>
	<div class="project_descr">
		<img class="project_img" id="gridRow2" src="/assets/cryptotracker/details_light.png"/>
		<div class="project_explanation">
			<h1>Detailed overview</h1>
			<h5>Compare the prices of the main exchanges, watch the traded volume of the last 24h, read information about the coin...</h5>
		</div>
	</div>
	<div class="project_descr">
		<img class="project_img" id="gridRow3" src="/assets/cryptotracker/portfolio_light.png"/>
		<div class="project_explanation">
			<h1>Your portfolio at a glance</h1>
			<h5>Keep track of your purchases with the Portfolio section, and stay up to date with the News section.</h5>
		</div>
	</div>
</div>

<script>
	function lightTheme(){
		document.getElementById("gridRow1").src = "/assets/cryptotracker/top100_light.png";
		document.getElementById("gridRow2").src = "/assets/cryptotracker/details_light.png";
		document.getElementById("gridRow3").src = "/assets/cryptotracker/portfolio_light.png";
		document.getElementById("hero-img").src = "/assets/cryptotracker/logo-wide-dark.png";
	}
	function darkTheme(){
		document.getElementById("gridRow1").src = "/assets/cryptotracker/top100_dark.png";
		document.getElementById("gridRow2").src = "/assets/cryptotracker/details_dark.png";
		document.getElementById("gridRow3").src = "/assets/cryptotracker/portfolio_dark.png";
		document.getElementById("hero-img").src = "/assets/cryptotracker/logo-wide-light.png";
	}
</script>