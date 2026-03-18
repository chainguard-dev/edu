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
