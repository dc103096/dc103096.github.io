let targetX = 0;
let targetY = 0;
let currentX = 0;
let currentY = 0;

const container = document.querySelector('.container');

document.addEventListener('mousemove', (e) => {
	targetX = (e.clientX / window.innerWidth - 0.5) * 20; // -10 ~ +10
	targetY = (e.clientY / window.innerHeight - 0.5) * 20;
});

function animateParallax() {
	// 緩慢靠近 targetX/Y
	currentX += (targetX - currentX) * 0.1;
	currentY += (targetY - currentY) * 0.1;

	container.style.transform = `translate(${currentX}px, ${currentY}px)`;

	requestAnimationFrame(animateParallax);
}

animateParallax();