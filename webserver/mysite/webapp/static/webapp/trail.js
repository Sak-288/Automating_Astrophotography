document.addEventListener('mousemove', function(e) {
    // Create a new trail element
    const trail = document.createElement('div');
    trail.textContent = '⸱';
    trail.classList.add('trailing');

    // Position the trail element at the mouse cursor's location
    trail.style.left = e.clientX + 'px';
    trail.style.top = e.clientY + 'px';

    // Add the new element to the container
    document.getElementById('trail').appendChild(trailing);

    // Remove the element after the animation is complete (5 seconds)
    // This prevents the DOM from getting too large and slowing down the page
    setTimeout(() => {
        trail.remove();
    }, 5000);
});