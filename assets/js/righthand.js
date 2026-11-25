const sections = [...document.querySelectorAll(".tocLinks a")]
  .map((link) => ({
    link,
    heading: document.getElementById(decodeURIComponent(link.hash.slice(1))),
  }))
  .filter(({ heading }) => heading);

const update = () => {
  let current = sections[0];
  let nearest = Infinity;
  for (const section of sections) {
    const top = section.heading.getBoundingClientRect().top;
    if (top <= innerHeight / 2 && Math.abs(top) <= nearest) {
      current = section;
      nearest = Math.abs(top);
    }
  }
  sections.forEach(({ link }) =>
    link.setAttribute("aria-current", link === current.link)
  );
};

update();
addEventListener("scroll", update, { passive: true });
