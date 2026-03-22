// static/js/theme.js

(function () {
  var HTML = document.documentElement;
  var BODY;
  var STORAGE_KEY = "portfolio-theme";

  // Apply immediately before paint
  var saved = localStorage.getItem(STORAGE_KEY) || "dark";
  applyTheme(saved);

  function applyTheme(theme) {
    if (theme === "light") {
      HTML.classList.remove("dark");
      HTML.classList.add("light");
    } else {
      HTML.classList.remove("light");
      HTML.classList.add("dark");
    }
    localStorage.setItem(STORAGE_KEY, theme);
    updateIcons(theme);
    updateCanvasOpacity(theme);
    updatePlaceholders(theme); // ✅ Add this
  }

  // ✅ Add this new function
  function updatePlaceholders(theme) {
    var placeholderDark = "0a0f1e/7c3aed";
    var placeholderLight = "ffffff/7c3aed";

    document.querySelectorAll("img.org-logo").forEach(function (img) {
      if (img.src.includes("placehold.co")) {
        img.src =
          theme === "dark"
            ? "https://placehold.co/48x48/" + placeholderDark + "?text=Co"
            : "https://placehold.co/48x48/" + placeholderLight + "?text=Co";
      }
    });
  }

  function updateIcons(theme) {
    var iconLight = document.getElementById("icon-light");
    var iconDark = document.getElementById("icon-dark");
    if (!iconLight || !iconDark) return;
    if (theme === "light") {
      iconLight.classList.add("hidden");
      iconDark.classList.remove("hidden");
    } else {
      iconLight.classList.remove("hidden");
      iconDark.classList.add("hidden");
    }
  }

  function updateCanvasOpacity(theme) {
    var canvas = document.getElementById("neural-canvas");
    if (!canvas) return;
    canvas.style.opacity = theme === "light" ? "0.06" : "0.18";
  }

  document.addEventListener("DOMContentLoaded", function () {
    BODY = document.body;

    var btn = document.getElementById("theme-toggle");
    if (btn) {
      btn.addEventListener("click", function () {
        var current = localStorage.getItem(STORAGE_KEY) || "dark";
        var next = current === "dark" ? "light" : "dark";
        applyTheme(next);
      });
    }

    // Set correct icons on load
    updateIcons(localStorage.getItem(STORAGE_KEY) || "dark");
    updateCanvasOpacity(localStorage.getItem(STORAGE_KEY) || "dark");
  });
})();
