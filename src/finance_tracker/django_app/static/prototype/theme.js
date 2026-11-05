/* Only the display preference is stored; no account or session data. */
(() => {
  "use strict";
  const key = "finance-tracker-theme";
  const root = document.documentElement;
  const system = window.matchMedia("(prefers-color-scheme: dark)");
  let preference;
  try {
    const stored = window.localStorage.getItem(key);
    if (stored === "light" || stored === "dark") preference = stored;
  } catch (_) {
    // Private/restricted browser storage must not prevent page use.
  }

  function apply(theme) {
    root.dataset.theme = theme;
    const button = document.getElementById("theme-toggle");
    if (button) {
      button.setAttribute("aria-pressed", String(theme === "dark"));
      button.title = theme === "dark" ? "Açık temaya geç" : "Koyu temaya geç";
    }
  }
  apply(preference || (system.matches ? "dark" : "light"));

  function setup() {
    const button = document.getElementById("theme-toggle");
    if (!button) return;
    button.hidden = false;
    apply(root.dataset.theme);
    button.addEventListener("click", () => {
      preference = root.dataset.theme === "dark" ? "light" : "dark";
      apply(preference);
      try {
        window.localStorage.setItem(key, preference);
      } catch (_) {
        // The switch still works for this page if storage is unavailable.
      }
    });
  }
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", setup, { once: true });
  } else {
    setup();
  }
  system.addEventListener("change", (event) => {
    if (!preference) apply(event.matches ? "dark" : "light");
  });
})();
