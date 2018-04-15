title:Github

{% if GITHUB_USER %}
    <h1>Projects</h1>
    {% for project in github_projects %}
        <h2>{{ project.name }} <sup>({{ project.language }})</sup></h2>
        {% if project.description %}<p>{{ project.description }}</p>{% endif %}
        <p>
            {% if project.homepage %}<a href="{{ project.homepage }}">Homepage</a>{% endif %}
            <a href="{{ project.github_url }}">GitHub</a>
        </p>
    {% endfor %}
{% endif %}