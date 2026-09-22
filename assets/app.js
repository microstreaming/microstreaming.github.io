/* MicrosStreaming - interacciones minimas.
   Sin dependencias. Regla de oro: si algo de esto falla, el contenido se
   sigue viendo. Nada oculta texto de forma permanente. */
(function () {
  "use strict";

  var doc = document.documentElement;

  /* --- Tema: claro / oscuro, recordado por navegador --------------------- */
  var btn = document.querySelector(".theme-btn");
  if (btn) {
    btn.addEventListener("click", function () {
      var cur = doc.getAttribute("data-theme");
      if (!cur) {
        cur = window.matchMedia("(prefers-color-scheme: dark)").matches
          ? "dark" : "light";
      }
      var next = cur === "dark" ? "light" : "dark";
      doc.setAttribute("data-theme", next);
      try { localStorage.setItem("ms-theme", next); } catch (e) { /* modo privado */ }
    });
  }

  /* --- Barra de progreso de lectura -------------------------------------- */
  var bar = document.querySelector(".progress");
  if (bar) {
    var queued = false;
    var paint = function () {
      var h = doc.scrollHeight - window.innerHeight;
      var p = h > 0 ? window.scrollY / h : 0;
      bar.style.transform = "scaleX(" + Math.min(1, Math.max(0, p)) + ")";
      queued = false;
    };
    window.addEventListener("scroll", function () {
      if (!queued) { queued = true; requestAnimationFrame(paint); }
    }, { passive: true });
    paint();
  }

  /* --- Scrollspy del indice lateral -------------------------------------- */
  var links = Array.prototype.slice.call(document.querySelectorAll(".rail a"));
  if (links.length && "IntersectionObserver" in window) {
    var byId = {};
    var targets = [];
    links.forEach(function (a) {
      var id = a.getAttribute("href").slice(1);
      var el = document.getElementById(id);
      if (el) { byId[id] = a; targets.push(el); }
    });

    var seen = {};
    var mark = function () {
      var best = null;
      targets.forEach(function (t) {
        if (seen[t.id] && (best === null || t.offsetTop < best.offsetTop)) best = t;
      });
      if (!best) return;
      links.forEach(function (a) { a.classList.remove("active"); });
      if (byId[best.id]) byId[best.id].classList.add("active");
    };

    var spy = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { seen[e.target.id] = e.isIntersecting; });
      mark();
    }, { rootMargin: "-88px 0px -62% 0px", threshold: 0 });

    targets.forEach(function (t) { spy.observe(t); });
  }

  /* --- Cerrar el menu movil al navegar ----------------------------------- */
  var toggle = document.getElementById("nav-toggle");
  if (toggle) {
    Array.prototype.forEach.call(document.querySelectorAll("nav.main a"), function (a) {
      a.addEventListener("click", function () { toggle.checked = false; });
    });
  }

  /* --- Nota sobre animaciones de entrada ---------------------------------
     No ocultamos bloques de contenido para animarlos al hacer scroll. Se
     probo y, si el observador no dispara (pestana en segundo plano, motor
     que limita el repintado), el texto se queda invisible de forma
     permanente. En un sitio cuyo objetivo es que se lea, ese riesgo no
     compensa el efecto. El movimiento vive en el hover, la barra de
     progreso y el indice lateral, que nunca esconden nada. */
})();
