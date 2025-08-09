(function() {
    console.log("JavaScript loaded!");
    
    document.addEventListener('DOMContentLoaded', function() {
        console.log("DOM loaded!");
        
        const elem = document.querySelector("#parallax");
        console.log("Parallax element found:", elem);
        
        if (!elem) {
            console.error('Parallax element not found!');
            return;
        }
        
        document.addEventListener("mousemove", parallax);
        
        function parallax(e) {
            console.log("Mouse moved!", e.clientX, e.clientY);
            // ... rest of your parallax code
        }
    });
})();