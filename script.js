// Jaar in footer automatisch updaten
document.getElementById('year').textContent = new Date().getFullYear();

// “Meer bekijken” knop functionaliteit
const showMoreBtn = document.getElementById('show-more-btn');
const hiddenProjects = document.getElementById('more-projects');

showMoreBtn.addEventListener('click', () => {
    hiddenProjects.classList.toggle('show');
    showMoreBtn.textContent = hiddenProjects.classList.contains('show') ? "Minder bekijken" : "+ Meer bekijken";
});

// Fade-in animatie bij scroll
const portfolioItems = document.querySelectorAll('.portfolio-item');

function isInViewport(element) {
    const rect = element.getBoundingClientRect();
    return (
        rect.top <= (window.innerHeight || document.documentElement.clientHeight) - 100
    );
}

function checkVisibility() {
    portfolioItems.forEach(item => {
        if (isInViewport(item)) {
            item.classList.add('visible');
        }
    });
}

window.addEventListener('scroll', checkVisibility);
window.addEventListener('load', () => {
    checkVisibility();
    // ook direct de eerste items zichtbaar maken voor zekerheid
    portfolioItems.forEach(item => item.classList.add('visible'));
});

// Dropdown navigatie - alternatieve oplossing (voor kleinere schermen)
document.querySelectorAll('.dropbtn').forEach(btn => {
    btn.addEventListener('click', () => {
        const content = btn.nextElementSibling;
        content.style.display = content.style.display === 'block' ? 'none' : 'block';
    });
});