var index;
var searchForms = document.getElementsByClassName("search-container")

Array.from(searchForms).forEach(container => {
  const search = container.querySelectorAll('.search')[0]
  const suggestions = document.querySelectorAll('.suggestions')[0]

  if (search) {
    document.addEventListener('keydown', inputFocus);
  }
  
  function inputFocus(e) {
    if (e.key === '/' ) {
      e.preventDefault();
      search.focus();
    }
    if (e.key === 'Escape' ) {
      search.blur();
      suggestions.classList.add('d-none');
    }
  }

  document.addEventListener('click', function(event) {
    let isClickInsideElement = suggestions.contains(event.target);
  
    if (!isClickInsideElement) {
      suggestions.classList.add('d-none');
    }
  });

  document.addEventListener('keydown',suggestionFocus);
  
  function suggestionFocus(e) {
    const suggestionsHidden = suggestions.classList.contains('d-none');
    if (suggestionsHidden) return;
  
    const focusableSuggestions= [...suggestions.querySelectorAll('a')];
    if (focusableSuggestions.length === 0) return;
  
    const index = focusableSuggestions.indexOf(document.activeElement);
  
    if (e.key === "ArrowUp") {
      e.preventDefault();
      const nextIndex = index > 0 ? index - 1 : 0;
      focusableSuggestions[nextIndex].focus();
    }
    else if (e.key === "ArrowDown") {
      e.preventDefault();
      const nextIndex= index + 1 < focusableSuggestions.length ? index + 1 : index;
      focusableSuggestions[nextIndex].focus();
    }
  }

  search.addEventListener('input', show_results, true);

  function show_results(){
    const maxResult = 5;
    let searchQuery = this.value;
    let results = index.search(searchQuery, {limit: maxResult, enrich: true});

    // flatten results since index.search() returns results for each indexed field
    const flatResults = new Map(); // keyed by href to dedupe results
    for (const result of results.flatMap(r => r.result)) {
      if (flatResults.has(result.doc.href)) continue;
      flatResults.set(result.doc.href, result.doc);
    }

    suggestions.innerHTML = "";
    suggestions.classList.remove('d-none');

    // inform user that no results were found
    if (flatResults.size === 0 && searchQuery) {
      const noResultsMessage = document.createElement('div')
      noResultsMessage.innerHTML = `No results for "<strong>${searchQuery}</strong>"`
      noResultsMessage.classList.add("suggestion__no-results");
      suggestions.appendChild(noResultsMessage);
      return;
    }

    // construct a list of suggestions
    for(const [href, doc] of flatResults) {
      const entry = document.createElement('div');
      suggestions.appendChild(entry);

      const a = document.createElement('a');
      a.href = href;
      entry.appendChild(a);

      const title = document.createElement('div');
      title.textContent = doc.title;
      title.classList.add("suggestion__title");
      a.appendChild(title);

      const description = document.createElement('div');
      description.textContent = doc.description;
      description.classList.add("suggestion__description");
      a.appendChild(description);

      suggestions.appendChild(entry);

      if(suggestions.childElementCount == maxResult) break;
    }
  }
});

window.addEventListener('load', function() {
  index = new FlexSearch.Document({
    tokenize: "forward",
    cache: 100,
    document: {
      id: 'id',
      store: [
        "href", "title", "description"
      ],
      index: ["title", "description", "content"]
    }
  });
  
  /* build document index */
  {{ $list := .Site.AllPages -}}
  {{ $len := (len $list) -}}

  {{ range $index, $element := $list -}}
  index.add({
    id: {{ $index }},
    href: "{{ .RelPermalink }}",
    title: {{ .Title | jsonify }},
    {{ with .Description -}}
    description: {{ . | jsonify }},
    {{ else -}}
    description: {{ .Summary | plainify | jsonify }},
    {{ end -}}
    content: {{ .Plain | jsonify }}
  });
  {{ end -}}
});
