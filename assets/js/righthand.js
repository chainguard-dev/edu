const tableOfContents = document.querySelector("#TableOfContents ul");
const navLinkElements = tableOfContents ? tableOfContents.children : [];
const activeElementClassName = "active-element";
const activeLinkClassName = "active-link";

const hasSecondLevelLinks = (element) => (element.children[1] ? true : false);

const removeClass = (linkElements) => {
  Array.from(linkElements).forEach((element) => {
    element.children[0].classList.remove(activeLinkClassName);
    element.children[0].classList.remove(activeElementClassName);
    element.classList.remove(activeElementClassName);
    if (hasSecondLevelLinks(element)) {
      removeClass(element.children[1].children);
    }
  });
};

const elementClickHandler = (element) => {
  // Trick to select items that don't match scrollbar (e.g. when more than one section fit the bottom of the screen)
  element.addEventListener("click", () => {
    setTimeout(() => {
      removeClass(navLinkElements);
      element.classList.add(activeElementClassName);
      element.children[0].classList.add(activeLinkClassName);
    }, 500);
  });
};

const hashValueHandler = (element) => {
  const currentHash = window.location.hash;
  const elementHash = element.children[0].getAttribute("href");
  if (currentHash === elementHash) {
    removeClass(navLinkElements);
    element.children[0].classList.add(activeElementClassName);
    element.children[0].classList.add(activeLinkClassName);
  }
};

const highlightLink = (linkElements) =>
  Array.from(linkElements).forEach((element, i) => {
    hashValueHandler(element, i);
    if (!hasSecondLevelLinks(element)) {
      elementClickHandler(element);
    } else {
      element.children[0].addEventListener("click", () => {
        removeClass(navLinkElements);
        element.children[0].classList.add(activeElementClassName);
        element.children[0].classList.add(activeLinkClassName);
      });
      highlightLink(element.children[1].children);
    }
  });

highlightLink(navLinkElements);
