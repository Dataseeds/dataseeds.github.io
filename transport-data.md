---
layout: page
title: Waste management
visible: false
permalink: /transport/data
---
<head>
	<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>
</head>

<div>
	<div class="centered-title">
		<img src="/assets/icons/transport.png">
		<h1>SUSTAINABLE TRANSPORT</h1>
		<img src="/assets/icons/transport.png" style="transform: scaleX(-1);">
	</div>
	<div class="data-flex-container">
		<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam a pharetra orci. Curabitur orci eros, auctor tristique auctor luctus, ultricies sed risus. Phasellus gravida orci in turpis lacinia varius. Mauris consequat erat risus, finibus malesuada diam auctor ac. Aenean non sem ex. Vivamus in libero purus. Morbi blandit, nisl non iaculis ultricies, orci nunc interdum turpis, eu tristique quam nunc ut lorem. Quisque pharetra ac leo et consequat.
		</p>
		<p>Morbi consequat eros sit amet lacus bibendum rhoncus. Proin eros neque, volutpat a massa vel, iaculis sagittis purus. Phasellus leo nunc, ultricies eu enim sit amet, rutrum sagittis lacus.
		</p>
	</div>
	{% include_relative transport-graph-change.html %}
	<!-- <select onChange="onSelect()" id="selectOpt">
		<option value="EU-13" selected>EU-13</option> 
		<option value="EU-15">EU-15</option>
		<option value="EEA-33">EEA-33</option>
	</select> -->

</div>

<!-- <script>
EU13=["Bulgaria", "Czech Republic", "Cyprus", "Estonia", "Croatia", "Hungary",
      "Lithuania", "Latvia", "Malta", "Poland", "Romania", "Slovenia", "Slovakia"]
EU15 = ["Austria", "Belgium", "Denmark", "Finland", "France", "Germany",
        "Greece", "Ireland", "Italy", "Luxembourg", "Netherlands", "Portugal",
        "Spain", "Sweden", "United Kingdom"]
EEA33 = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czech Republic',
         'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece',
         'Hungary', 'Iceland', 'Ireland', 'Italy', 'Latvia', 'Liechtenstein',
         'Lithuania', 'Luxembourg', 'Malta', 'Netherlands', 'Norway', 'Poland',
         'Portugal', 'Romania', 'Slovakia', 'Slovenia', 'Spain', 'Sweden',
		 'United Kingdom']
</script>

<script>
var layout = {
	dragmode: false,
	title: '2011 US Agriculture Exports by State',
	geo: {
		bgcolor: "transparent",
		scope: 'europe',
		scale: 8
	},
	margin: { l: 0, r: 0, b: 0, t: 0, pad: 0 },
	paper_bgcolor: "transparent",
	showlegend: false
};

var config = {autosizable: true, fillFrame: false, displayModeBar: false,
			  showTips: false, showLink: false, scrollZoom: true,
			  responsive: true, doubleClickDelay: 1000};

function plot(data){
	Plotly.newPlot("myDiv", data, layout, config);
}

var data = [{
	colorscale: 'Greens',
	type: "choropleth",
	locations: EU13,
	locationmode: 'country names',
	z: Array(13).fill(1)
}];
plot(data);
</script>

<script>		 
function onSelect(){
	var myselect = document.getElementById("selectOpt");
	var opt = myselect.options[myselect.selectedIndex].value;
	if (opt == "EU-13"){
		plot([{ colorscale: 'Greens', type: "choropleth", locations: EU13,
			locationmode: 'country names', z: Array(13).fill(1)}]);
	} else if(opt == "EU-15"){
		plot([{ colorscale: 'Greens', type: "choropleth", locations: EU15,
			locationmode: 'country names', z: Array(15).fill(1)}]);
	} else if(opt == "EEA-33"){
		plot([{ colorscale: 'Greens', type: "choropleth", locations: EEA33,
			locationmode: 'country names', z: Array(33).fill(1)}]);
	}
}
</script> -->
