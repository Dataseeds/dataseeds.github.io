---
layout: page
title: How it works
visible: false
permalink: /about/how-it-works
---

<head>
	<style>
		body {
			background-color: #f7f7f7;
			margin-top: 20px;
		}

		*,
		::after,
		::before {
			box-sizing: border-box;
		}

		.main-timeline {
			position: relative
		}

		.main-timeline:before {
			content: "";
			display: block;
			width: 2px;
			height: 100%;
			background: #c6c6c6;
			margin: 0 auto;
			position: absolute;
			top: 0;
			left: 0;
			right: 0
		}

		.main-timeline .timeline {
			margin-bottom: 40px;
			position: relative
		}

		.main-timeline .timeline:after {
			content: "";
			display: block;
			clear: both
		}

		.main-timeline .icon {
			width: 18px;
			height: 18px;
			line-height: 18px;
			margin: auto;
			position: absolute;
			top: 4.7rem;
			left: 0;
			right: 0
		}

		.main-timeline .icon:before,
		.main-timeline .icon:after {
			content: "";
			width: 100%;
			height: 100%;
			border-radius: 50%;
			position: absolute;
			top: 0;
			left: 0;
			transition: all 0.33s ease-out 0s
		}

		.main-timeline .icon:before {
			background: #fff;
			border: 2px solid #c1ddd5;
			left: -3px
		}

		.main-timeline .icon:after {
			border: 2px solid #c1ddd5;
			left: 3px
		}

		.main-timeline .timeline:hover .icon:before {
			left: 3px
		}

		.main-timeline .timeline:hover .icon:after {
			left: -3px
		}

		.main-timeline .date-content {
			width: 50%;
			float: left;
			margin-top: 22px;
			position: relative
		}

		.main-timeline .date-content:before {
			content: "";
			width: 36.5%;
			height: 2px;
			background: #c6c6c6;
			margin: auto 0;
			position: absolute;
			top: 0;
			right: 10px;
			bottom: 0
		}

		.main-timeline .date-outer {
			img {
			width: 125px;
			height: 125px;
			font-size: 16px;
			text-align: center;
			margin: auto;
			z-index: 1
			}
		}

		.main-timeline .date-outer:before,
		.main-timeline .date-outer:after {
			content: "";
			width: 125px;
			height: 125px;
			margin: 0 auto;
			border-radius: 50%;
			position: absolute;
			top: 0;
			left: 0;
			right: 0;
			transition: all 0.33s ease-out 0s
		}

		.main-timeline .date-outer:before {
			background: #fff;
			border: 2px solid #c1ddd5;
			left: -6px
		}

		.main-timeline .date-outer:after {
			border: 2px solid #c6c6c6;
			left: 6px
		}

		.main-timeline .timeline:hover .date-outer:before {
			left: 6px
		}

		.main-timeline .timeline:hover .date-outer:after {
			left: -6px
		}

		.main-timeline .date {
			width: 100%;
			margin: auto;
			position: absolute;
			top: 27%;
			left: 0
		}

		.main-timeline .month {
			font-size: 18px;
			font-weight: 700
		}

		.main-timeline .year {
			display: block;
			font-size: 30px;
			font-weight: 700;
			color: #232323;
			line-height: 36px
		}

		.main-timeline .timeline-content {
			width: 50%;
			padding: 20px 0 20px 30px;
			float: right
		}

		.main-timeline .title {
			font-size: 19px;
			font-weight: 700;
			line-height: 24px;
			margin: 0 0 15px 0
		}

		.main-timeline .description {
			margin-bottom: 0
		}

		.main-timeline .timeline:nth-child(2n) .date-content {
			float: right
		}

		.main-timeline .timeline:nth-child(2n) .date-content:before {
			left: 10px
		}

		.main-timeline .timeline:nth-child(2n) .timeline-content {
			padding: 20px 30px 20px 0;
			text-align: right
		}

		@media only screen and (max-width: 991px) {
			.main-timeline .date-content {
				margin-top: 35px
			}

			.main-timeline .date-content:before {
				width: 22.5%
			}

			.main-timeline .timeline-content {
				padding: 10px 0 10px 30px
			}

			.main-timeline .title {
				font-size: 17px
			}

			.main-timeline .timeline:nth-child(2n) .timeline-content {
				padding: 10px 30px 10px 0
			}
		}

		@media only screen and (max-width: 767px) {
			.main-timeline:before {
				margin: 0;
				left: 7px
			}

			.main-timeline .timeline {
				margin-bottom: 20px
			}

			.main-timeline .timeline:last-child {
				margin-bottom: 0
			}

			.main-timeline .icon {
				margin: auto 0
			}

			.main-timeline .date-content {
				width: 95%;
				float: right;
				margin-top: 0
			}

			.main-timeline .date-content:before {
				display: none
			}

			.main-timeline .date-outer {
				width: 110px;
				height: 110px
			}

			.main-timeline .date-outer:before,
			.main-timeline .date-outer:after {
				width: 110px;
				height: 110px
			}

			.main-timeline .date {
				top: 30%
			}

			.main-timeline .year {
				font-size: 24px
			}

			.main-timeline .timeline-content,
			.main-timeline .timeline:nth-child(2n) .timeline-content {
				width: 95%;
				text-align: center;
				padding: 10px 0
			}

			.main-timeline .title {
				margin-bottom: 10px
			}
		}
	</style>

	<head>

	<body>
		<div class="how-it-works">
			<div class="centered-title">
				<img src="/assets/icons/DrawKit-SaaS/Color/Development.svg">
				<h1>{{ page.title }}</h1>
				<img src="/assets/icons/DrawKit-SaaS/Color/Development.svg" style="transform: scaleX(-1);">
			</div>
		</div>

		<div class="container">
			<div class="main-timeline">

				<!-- start experience section-->
				<div class="timeline">
					<div class="icon"></div>
					<div class="date-content">
						<div class="date-outer">
						<img src="/assets/about/Human-centered process.png">
						</div>
					</div>
					<div class="timeline-content">
						<h5 class="title">Human-centered process</h5>
						<p class="description"> Despite the increase in economic aid to the agricultural sector in
							recent years,
							both general citizens and farmers consider the support to food producers insufficient. The
							lack of
							technological resources and generational renewal adds to the complex administrative
							structure that must be
							dealt with to access to public funds, as reported by a large number of SMEs that we had the
							opportunity to
							interview. Today, without even having finished solving the problems of the past decade, this
							sector faces
							a new wave of changes that will condition production in the near future: the ecological
							transition. At a
							time when the European Union is preparing to increase subsidies for the greening and
							digitalisation of
							agriculture, it is more important than ever to launch applications aimed at SMEs in the
							sector to access
							clear and simple information that allow them to bring the European institutions closer
							together.
						</p>
					</div>
				</div>
				<!-- end experience section-->

				<!-- start experience section-->
				<div class="timeline">
					<div class="icon"></div>
					<div class="date-content">
						<div class="date-outer">

						</div>
					</div>
					<div class="timeline-content">
						<h5 class="title">Utility</h5>
						<p class="description"> The aim of dataseeds is to help SMEs working in agriculture to have
							direct access to
							better and more detailed information regarding the coming changes in accordance to the
							European Green Deal
							and the inevitable climate change. Do you remember the avatar tree? A tree that would hold
							the knowledge
							of all its community. That is open data today. In this regard, the interface would encompass
							on the one
							hand, information and data on the production, packaging, transport, and waste processes, and
							on the other
							hand, the opinion of EU citizens as consumers. Multiple datasets are used to help SMEs
							reduce and control
							their flows concerning the Green Deal requirements – most of them are dynamic and
							continuously updated and
							some have a participatory approach.
						</p>
					</div>
				</div>
				<!-- end experience section-->

				<!-- start experience section-->
				<div class="timeline">
					<div class="icon"></div>
					<div class="date-content">
						<div class="date-outer">
							<span class="date">
								<span class="month">2 Years</span>
								<span class="year">2016</span>
							</span>
						</div>
					</div>
					<div class="timeline-content">
						<h5 class="title">Open Data</h5>
						<p class="description">
							Dataseeds is built on the premise to democratize open data information to smallholder
							agriculture. The
							European Data Portal offers 90,883 datasets on open environment data, which could help SMEs
							be more
							competitive, yet sustainable if used well. However, the quantity of data is such that it
							makes it very
							complex to find and use. We have used the sources of information that the EU makes available
							to citizens,
							such as the databases of the European Environment Agency, European Data Portal, Publications
							Office of the
							EU, Joint Research Centre and CORDIS. The legislative material has been drawn mainly from
							EUR-LEX and
							Lexparency, winner of the legal-tech challenge at the EU Datathon 2018.
						</p>
					</div>
				</div>
				<!-- end experience section-->

				<!-- start experience section-->
				<div class="timeline">
					<div class="icon"></div>
					<div class="date-content">
						<div class="date-outer">
							<span class="date">
								<span class="month">2 Years</span>
								<span class="year">2018</span>
							</span>
						</div>
					</div>
					<div class="timeline-content">
						<h5 class="title">Front-end Stack</h5>
						<p class="description">
							The frontend of the page is made with the usual web technologies of HTML + CSS + JS. But
							apart from that,
							Jekyll was also used, which is a great open source static site generator. This let us
							concentrate more on
							the contents of the page as it eased managing dozens of static pages, and also allowed us to
							use Markdown
							for blog posts and Liquid in HTML for a less tedious coding. The webpage is totally open
							sourced in our
							Github repo and is also hosted there thanks to the amazing (and free) GitHub Pages, which is
							a static site
							hosting service that comes together perfectly with Jekyll (which the cofounder of GitHub
							created).
						</p>
					</div>
				</div>
				<!-- end experience section-->

				<!-- start experience section-->
				<div class="timeline">
					<div class="icon"></div>
					<div class="date-content">
						<div class="date-outer">
							<span class="date">
								<span class="month">2 Years</span>
								<span class="year">2018</span>
							</span>
						</div>
					</div>
					<div class="timeline-content">
						<h5 class="title">Data visualisation</h5>
						<p class="description">
							The webpage wouldn't be the same without the maps, charts and visualizations scattered
							around the
							different sections. Each one of them was created from scratch with datasets from the EU Open
							Data Portal.
							Finally, the data was processed and explored in Python with the Pandas library, and then a
							graph was
							created around the chosen data. All the graphs and charts were made with the Plotly library,
							which is a
							wonderful interactive graphing library for Python .
						</p>
					</div>
				</div>
				<!-- end experience section-->

				<!-- start experience section-->
				<div class="timeline">
					<div class="icon"></div>
					<div class="date-content">
						<div class="date-outer">
							<span class="date">
								<span class="month">2 Years</span>
								<span class="year">2018</span>
							</span>
						</div>
					</div>
					<div class="timeline-content">
						<h5 class="title">Used sources</h5>
						<p class="description">
							This page was also created with the help of a set of amazing open source libraries and
							frameworks used to
							build and manage both the website and the content. But a special thanks need to be provided
							to the amazing
							vectorized icons from Drawkit, and the entirety of the datasets and information collected
							from a variety
							of sources: EEA, Eurostat, EUR-lex, EIB, CORDIS and JRC. <br>
							<br>
							Datasets: EEA, Eurostat, EUR-Lex, EIB, REGIO, INEA, CORDIS, JRC. <br>
							<br>
							Vectorized icons from <href src="https://www.drawkit.io/free-icons">Drawkit</href>.
						</p>
					</div>
				</div>
				<!-- end experience section-->

			</div>
		</div>

	</body>
