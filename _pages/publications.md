---
layout: archive
# title: "Recent Publications"
title: ""
permalink: /publications/
author_profile: true
sitemap: false
---

{% if author.googlescholar %}
  You can also find my articles on <u><a href="{{author.googlescholar}}">my Google Scholar profile</a>.</u>
{% endif %}

{% include base_path %}

{% for post in site.publications reversed %}
  {% include publication-item.html %}
{% endfor %}
