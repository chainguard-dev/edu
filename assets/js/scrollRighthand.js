class Scroller {
  static init() {
    if (document.querySelector(".tocLinks")) {
      this.tocLinks = document.querySelectorAll(".tocLinks a");
      this.tocLinks.forEach((link) =>
        link.classList.add("transition", "duration-200")
      );
      this.headers = Array.from(this.tocLinks).map((link) => {
        return document.querySelector(`#${link.href.split("#")[1]}`);
      });
      this.ticking = false;
      window.addEventListener("scroll", () => {
        this.onScroll();
      });
    }
  }

  static onScroll() {
    if (!this.ticking) {
      requestAnimationFrame(this.update.bind(this));
      this.ticking = true;
    }
  }

  static update() {
    this.activeHeader |= this.headers[0];
    let activeIndex = this.headers.findIndex((header) => {
      return header.getBoundingClientRect().top > 180;
    });
    if (activeIndex === 0) {
      if (this.tocLinks[0].nextElementSibling) {
        this.tocLinks[0].classList.add("active-element");
      } else {
        this.tocLinks[0].parentElement.classList.add("active-element");
      }
    }
    if (activeIndex == -1) {
      activeIndex = this.headers.length - 1;
    } else if (activeIndex > 0) {
      activeIndex--;
    }
    let active = this.headers[activeIndex];
    if (active !== this.activeHeader) {
      this.activeHeader = active;
      this.tocLinks.forEach((link) => link.classList.remove("active-link"));
      this.tocLinks.forEach((link) => link.classList.remove("active-element"));
      this.tocLinks.forEach((link) =>
        link.parentElement.classList.remove("active-element")
      );

      this.tocLinks[activeIndex].classList.add("active-link");
      if (this.tocLinks[activeIndex].nextElementSibling) {
        this.tocLinks[activeIndex].classList.add("active-element");
      } else {
        this.tocLinks[activeIndex].parentElement.classList.add(
          "active-element"
        );
      }
    }
    this.ticking = false;
  }
}

document.addEventListener("DOMContentLoaded", function () {
  Scroller.init();
});
