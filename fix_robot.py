import re

with open("index.html", "r") as f:
    content = f.read()

robot_js = """
        // --- Flying Robot Logic ---
        const robot = document.getElementById('cursor-robot');
        const eyeL = document.getElementById('robot-eye-l');
        const eyeR = document.getElementById('robot-eye-r');
        
        let mouseX = window.innerWidth / 2;
        let mouseY = window.innerHeight / 2;
        let robotX = mouseX;
        let robotY = mouseY;
        
        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
        });
        
        function animateRobot() {
            robotX += (mouseX - robotX) * 0.06;
            robotY += (mouseY - robotY) * 0.06;
            
            if (robot) {
                robot.style.transform = `translate(${robotX + 25}px, ${robotY + 25}px)`;
            }
            
            const dx = mouseX - robotX;
            const dy = mouseY - robotY;
            const tilt = Math.max(-15, Math.min(15, dx * 0.1));
            
            if (robot && robot.firstElementChild) {
                robot.firstElementChild.style.transform = `rotate(${tilt}deg)`;
                robot.firstElementChild.style.transition = 'transform 0.1s linear';
            }
            
            const angle = Math.atan2(dy, dx);
            const eyeOffsetX = Math.cos(angle) * 3;
            const eyeOffsetY = Math.sin(angle) * 3;
            
            if (eyeL && eyeR) {
                eyeL.setAttribute('cx', 35 + eyeOffsetX);
                eyeL.setAttribute('cy', 40 + eyeOffsetY);
                eyeR.setAttribute('cx', 65 + eyeOffsetX);
                eyeR.setAttribute('cy', 40 + eyeOffsetY);
            }
            
            requestAnimationFrame(animateRobot);
        }
        
        if (window.innerWidth > 768) {
            animateRobot();
        }
    </script>
</body>"""

content = re.sub(r'</script>\s*</body>', robot_js, content)

with open("index.html", "w") as f:
    f.write(content)

print("Robot JS added.")
