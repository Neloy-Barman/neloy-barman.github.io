// static/js/main.js

/* ═══════════════════════════════════════════════════════
   GLOBAL NEURAL NETWORK CANVAS — runs on every page
═══════════════════════════════════════════════════════ */
(function () {
  var canvas = document.getElementById("neural-canvas");
  if (!canvas) return;
  var ctx = canvas.getContext("2d");
  var W,
    H,
    particles = [],
    frame;

  function resize() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = window.innerHeight;
  }

  function makeParticle() {
    return {
      x: Math.random() * W,
      y: Math.random() * H,
      vx: (Math.random() - 0.5) * 0.4,
      vy: (Math.random() - 0.5) * 0.4,
      r: Math.random() * 1.5 + 0.5,
      color: Math.random() > 0.5 ? "0,212,255" : "124,58,237",
    };
  }

  function init() {
    resize();
    particles = [];
    for (var i = 0; i < 70; i++) particles.push(makeParticle());
  }

  function draw() {
    ctx.clearRect(0, 0, W, H);

    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0 || p.x > W) p.vx *= -1;
      if (p.y < 0 || p.y > H) p.vy *= -1;

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(" + p.color + ",0.8)";
      ctx.fill();
    }

    for (var i = 0; i < particles.length; i++) {
      for (var j = i + 1; j < particles.length; j++) {
        var dx = particles[i].x - particles[j].x;
        var dy = particles[i].y - particles[j].y;
        var dist = Math.sqrt(dx * dx + dy * dy);
        if (dist < 120) {
          ctx.beginPath();
          ctx.moveTo(particles[i].x, particles[i].y);
          ctx.lineTo(particles[j].x, particles[j].y);
          ctx.strokeStyle = "rgba(0,212,255," + (1 - dist / 120) * 0.2 + ")";
          ctx.lineWidth = 0.5;
          ctx.stroke();
        }
      }
    }

    frame = requestAnimationFrame(draw);
  }

  init();
  draw();
  window.addEventListener("resize", init);
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) {
      cancelAnimationFrame(frame);
    } else {
      draw();
    }
  });
})();

/* ═══════════════════════════════════════════════════════
   DOM READY — all other interactions
═══════════════════════════════════════════════════════ */
document.addEventListener("DOMContentLoaded", function () {
  /* ── Slide-up scroll observer ─────────────────────── */
  var slideEls = document.querySelectorAll(".slide-up");
  if (slideEls.length > 0) {
    var slideObserver = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible");
            slideObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.1, rootMargin: "0px 0px -40px 0px" },
    );
    slideEls.forEach(function (el) {
      slideObserver.observe(el);
    });
  }

  /* ── Mobile menu ──────────────────────────────────── */
  var mobileBtn = document.getElementById("mobile-menu-btn");
  var mobileMenu = document.getElementById("mobile-menu");
  var menuIconOpen = document.getElementById("menu-icon-open");
  var menuIconClose = document.getElementById("menu-icon-close");

  if (mobileBtn && mobileMenu) {
    mobileBtn.addEventListener("click", function () {
      var isOpen = !mobileMenu.classList.contains("hidden");
      mobileMenu.classList.toggle("hidden", isOpen);
      if (menuIconOpen) menuIconOpen.classList.toggle("hidden", !isOpen);
      if (menuIconClose) menuIconClose.classList.toggle("hidden", isOpen);
      mobileBtn.setAttribute("aria-expanded", String(!isOpen));
    });
    document.addEventListener("click", function (e) {
      if (!mobileBtn.contains(e.target) && !mobileMenu.contains(e.target)) {
        mobileMenu.classList.add("hidden");
        if (menuIconOpen) menuIconOpen.classList.remove("hidden");
        if (menuIconClose) menuIconClose.classList.add("hidden");
        mobileBtn.setAttribute("aria-expanded", "false");
      }
    });
  }

  /* ── Nav scroll shadow ────────────────────────────── */
  var nav = document.querySelector("nav");
  if (nav) {
    window.addEventListener(
      "scroll",
      function () {
        nav.style.boxShadow =
          window.scrollY > 20 ? "0 4px 30px rgba(0,0,0,0.4)" : "none";
      },
      { passive: true },
    );
  }

  /* ── Active nav highlight ─────────────────────────── */
  var path = window.location.pathname;
  document.querySelectorAll(".nav-link").forEach(function (link) {
    var href = link.getAttribute("href");
    if (href && href !== "/" && path.startsWith(href)) {
      link.classList.add("nav-link-active");
    } else if (href === "/" && path === "/") {
      link.classList.add("nav-link-active");
    }
  });

  /* ── Contact form spinner ─────────────────────────── */
  var contactForm = document.getElementById("contact-form");
  if (contactForm) {
    contactForm.addEventListener("submit", function () {
      var btn = contactForm.querySelector('button[type="submit"]');
      if (btn) {
        btn.innerHTML = '<i class="fas fa-spinner fa-spin mr-2"></i>Sending...';
        btn.disabled = true;
      }
    });
  }

  /* ── Smooth anchor scroll ─────────────────────────── */
  document.querySelectorAll('a[href^="#"]').forEach(function (anchor) {
    anchor.addEventListener("click", function (e) {
      var target = document.querySelector(this.getAttribute("href"));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: "smooth", block: "start" });
      }
    });
  });
});
