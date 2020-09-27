---
layout: page
title: Sustainable Transport
visible: false
permalink: /transport/legislations


<script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>

<div>
  <div class="centered-title" onclick="location.href='/transport'" style="cursor: pointer;">
  <img src="/assets/icons/DrawKit-Ecology/Color/Gas Station.svg">
  <h1>{{ page.title }}</h1>
  <img src="/assets/icons/DrawKit-Ecology/Color/Gas Station.svg" style="transform: scaleX(-1);">
</div>
<div class="flex-container">
  <p>
  In order for the European Union to reach its climate-neutral objectives, existing goals need to be accompanied by innovative and ambitious legislative and non-legislative actions. This broad scope of actions includes <i>inter alia</i> policy proposals and new legal acts – some are binding, others are not. Moreover, not all actions apply to all EU countries, or in the same way. Hereafter you will be able to find legislative and non-legislative documents on <b>clean and efficient production</b>.
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

 var legislationsList = new List('search-list', options, values);
</script>
