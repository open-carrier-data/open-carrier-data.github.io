const copyButtons = document.querySelectorAll("[data-copy]");

for (const button of copyButtons) {
  button.addEventListener("click", async () => {
    const target = document.querySelector(button.dataset.copy);
    if (!target) return;
    await navigator.clipboard.writeText(target.textContent.trim());
    const oldText = button.textContent;
    button.textContent = "Copied";
    window.setTimeout(() => {
      button.textContent = oldText;
    }, 1200);
  });
}

const tabs = document.querySelectorAll("[data-tab]");

for (const tab of tabs) {
  tab.addEventListener("click", () => {
    const name = tab.dataset.tab;
    for (const other of tabs) {
      other.classList.toggle("active", other === tab);
      other.setAttribute("aria-selected", String(other === tab));
    }
    for (const panel of document.querySelectorAll(".tab-panel")) {
      const active = panel.id === `tab-${name}`;
      panel.classList.toggle("active", active);
      panel.hidden = !active;
    }
  });
}

const navLinks = [...document.querySelectorAll(".top-nav a[href^='#']")];
const sections = navLinks
  .map((link) => document.querySelector(link.getAttribute("href")))
  .filter(Boolean);

const observer = new IntersectionObserver(
  (entries) => {
    const visible = entries
      .filter((entry) => entry.isIntersecting)
      .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];
    if (!visible) return;
    for (const link of navLinks) {
      link.classList.toggle(
        "active",
        link.getAttribute("href") === `#${visible.target.id}`,
      );
    }
  },
  { rootMargin: "-18% 0px -68% 0px", threshold: [0.1, 0.35, 0.65] },
);

for (const section of sections) {
  observer.observe(section);
}
