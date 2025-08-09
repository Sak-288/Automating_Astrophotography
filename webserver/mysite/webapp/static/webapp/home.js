(function() {
    // Wait for DOM to be fully loaded
    document.addEventListener('DOMContentLoaded', function() {
        // Add event listener for mouse movement
        document.addEventListener("mousemove", parallax);
        const elem = document.querySelector("#parallax");
        
        // Check if element exists
        if (!elem) {
            console.error('Parallax element not found');
            return;
        }
        
        // Parallax effect function
        function parallax(e) {
            let _w = window.innerWidth / 2;
            let _h = window.innerHeight / 2;
            let _mouseX = e.clientX;
            let _mouseY = e.clientY;
            
            // Calculate different depth layers
            let _depth1 = `${50 - (_mouseX - _w) * 0.01}% ${50 - (_mouseY - _h) * 0.01}%`;
            let _depth2 = `${50 - (_mouseX - _w) * 0.02}% ${50 - (_mouseY - _h) * 0.02}%`;
            let _depth3 = `${50 - (_mouseX - _w) * 0.06}% ${50 - (_mouseY - _h) * 0.06}%`;
            
            // Combine all layers
            let backgroundPosition = `${_depth3}, ${_depth2}, ${_depth1}`;
            
            // Apply the parallax effect
            elem.style.backgroundPosition = backgroundPosition;
            
            // Optional: Log for debugging (remove in production)
            // console.log(backgroundPosition);
        }
    });
})();