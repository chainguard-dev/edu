(() => {
  const hideKapaButtonOnMobile = () => {
    const host = document.getElementById("kapa-widget-container");
    if (!host || !host.shadowRoot) return false;
    const style = document.createElement("style");
    style.textContent =
      "@media (max-width: 672px) { #kapa-button { display: none !important; } }";
    host.shadowRoot.appendChild(style);
    return true;
  };
  if (hideKapaButtonOnMobile()) return;
  const observer = new MutationObserver(() => {
    if (hideKapaButtonOnMobile()) observer.disconnect();
  });
  observer.observe(document.documentElement, {
    childList: true,
    subtree: true,
  });
})();

const menuPositioner = () => {
  const nav = document.querySelectorAll("#sidebar-default")[1];
  const itemActive = document.querySelectorAll(".sidebar-item-active");
  const itemActiveMobile = document.querySelectorAll(
    ".offcanvas-body .sidebar-item-active",
  );
  const navMobile = document.querySelector(".offcanvas-body");

  if (itemActive.length) {
    nav.scrollTop = itemActive[itemActive.length - 1].offsetTop - 300;
    navMobile.scrollTop =
      itemActiveMobile[itemActiveMobile.length - 1].offsetTop - 200;
  }
};

menuPositioner();
