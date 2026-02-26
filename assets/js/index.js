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

  document.addEventListener('keydown', suggestionFocus);

  function suggestionFocus(e) {
    const suggestionsHidden = suggestions.classList.contains('d-none');
    if (suggestionsHidden) return;

    const focusableSuggestions = [...suggestions.querySelectorAll('a')];
    if (focusableSuggestions.length === 0) return;

    const index = focusableSuggestions.indexOf(document.activeElement);

    if (e.key === "ArrowUp") {
      e.preventDefault();
      const nextIndex = index > 0 ? index - 1 : 0;
      focusableSuggestions[nextIndex].focus();
    } else if (e.key === "ArrowDown") {
      e.preventDefault();
      const nextIndex = index + 1 < focusableSuggestions.length ? index + 1 : index;
      focusableSuggestions[nextIndex].focus();
    }
  }

  search.addEventListener('input', show_results, true);

  function show_results() {
    const maxResult = 5;
    let searchQuery = this.value;

    if (!searchQuery) {
      suggestions.classList.add('d-none');
      suggestions.innerHTML = "";
      return;
    }

    algoliaIndex.search(searchQuery, { hitsPerPage: maxResult }).then(({ hits }) => {
      suggestions.innerHTML = "";
      suggestions.classList.remove('d-none');

      if (hits.length === 0) {
        const noResultsMessage = document.createElement('div');
        noResultsMessage.textContent = 'No results for "';
        const strong = document.createElement('strong');
        strong.textContent = searchQuery;
        noResultsMessage.appendChild(strong);
        noResultsMessage.appendChild(document.createTextNode('"'));
        noResultsMessage.classList.add("suggestion__no-results");
        suggestions.appendChild(noResultsMessage);
        return;
      }

      for (const hit of hits) {
        const entry = document.createElement('div');
        suggestions.appendChild(entry);

        const a = document.createElement('a');
        a.href = hit.url;
        entry.appendChild(a);

        const title = document.createElement('div');
        title.textContent = hit.hierarchy.lvl1 || hit.hierarchy.lvl0 || '';
        title.classList.add("suggestion__title");
        a.appendChild(title);

        const description = document.createElement('div');
        description.textContent = hit.content || '';
        description.classList.add("suggestion__description");
        a.appendChild(description);

        suggestions.appendChild(entry);
      }
    });
  }
});

const menuPositioner = () => {
  const nav = document.querySelectorAll("#sidebar-default")[1]
  const itemActive = document.querySelectorAll(".sidebar-item-active")
  const itemActiveMobile = document.querySelectorAll(".offcanvas-body .sidebar-item-active")
  const navMobile = document.querySelector(".offcanvas-body")

  if (itemActive.length) {
    nav.scrollTop = itemActive[itemActive.length - 1].offsetTop - 300
    navMobile.scrollTop = itemActiveMobile[itemActiveMobile.length - 1].offsetTop - 200
  }
}

menuPositioner()
