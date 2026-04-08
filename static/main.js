
// Cache DOM elements
const header = document.querySelector(".header");
const sections = document.querySelectorAll(".section");
const navlinks = document.querySelectorAll(".navlink");
const menuBar = document.querySelector(".menu-bar");
const closeBtn = document.querySelector(".close");
const mobileMenu = document.querySelector(".mobile-menu");
const tabBtns = document.querySelectorAll(".tab-btn");
const menuCards = document.querySelectorAll(".menu-card");
const backToTopBtn = document.querySelector(".backToTop");

// ========================
// Init when DOM is ready
// ========================
window.addEventListener("DOMContentLoaded", () => {
    tabBtns.forEach(btn => btn.addEventListener("click", toggleTab));
    closeBtn?.addEventListener("click", closeMenu);
    menuBar?.addEventListener("click", openMenu);

    navlinks.forEach(link => {
        link.addEventListener("click", () => {
            if (mobileMenu?.classList.contains("active")) {
                mobileMenu.classList.remove("active");
            }
        });
    });

    backToTopBtn?.addEventListener("click", () => {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
});

// ========================
// Scroll handling
// ========================
let scrollTimeout;
window.addEventListener("scroll", () => {
    if (!scrollTimeout) {
        scrollTimeout = setTimeout(() => {
            handleScroll();
            scrollTimeout = null;
        }, 100); // throttle to run at most every 100ms
    }
});

function handleScroll() {
    // Toggle Back-to-Top button
    if (window.scrollY > 300) backToTopBtn?.classList.add("active");
    else backToTopBtn?.classList.remove("active");

    // Toggle header scrolled class
    if (window.scrollY > 50) header?.classList.add("scrolled");
    else header?.classList.remove("scrolled");

    // Update active nav link
    activeClass();
}

// ========================
// Active Nav Link Highlight
// ========================
function activeClass() {
    let current = "";

    sections.forEach(section => {
        const secTop = section.offsetTop;
        const secHeight = section.clientHeight;
        if (window.scrollY >= secTop - secHeight / 4) {
            current = section.getAttribute("id");
        }
    });

    navlinks.forEach(link => {
        link.classList.toggle("active", link.getAttribute("href") === `#${current}`);
    });
}

// ========================
// Tab Filtering
// ========================
function toggleTab() {
    const category = this.getAttribute("data-category");

    tabBtns.forEach(btn => btn.classList.remove("active"));
    this.classList.add("active");

    menuCards.forEach(item => {
        if (category === "all" || item.getAttribute("data-category") === category) {
            item.style.display = "block";
            item.classList.remove("fadeIn");
            void item.offsetWidth; // reflow for animation restart
            item.classList.add("fadeIn");
        } else {
            item.style.display = "none";
        }
    });
}

// ========================
// Mobile Menu Controls
// ========================
function closeMenu() {
    mobileMenu?.classList.remove("active");
}

function openMenu() {
    if (!mobileMenu?.classList.contains("active")) {
        mobileMenu.classList.add("active");
    }
}
