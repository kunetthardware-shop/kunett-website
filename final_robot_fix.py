import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Update HTML classes to allow visibility on all devices (but initially hidden with opacity-0)
old_html = r'<div id="cursor-robot" class="hidden md:block fixed pointer-events-none z-\[9999\] will-change-transform" style="top: 0; left: 0; transform: translate\(-100px, -100px\);">'
new_html = '<div id="cursor-robot" class="fixed pointer-events-none z-[9999] will-change-transform transition-opacity duration-500 opacity-0" style="top: 0; left: 0; transform: translate(-100px, -100px);">'
content = re.sub(old_html, new_html, content)


# 2. Inject Javascript Logic right before the final `</script>`
robot_js = """        
        // --- Flying Robot Logic ---
        let robotInitialized = false;
        let mouseX = window.innerWidth / 2;
        let mouseY = window.innerHeight / 2;
        let robotX = mouseX;
        let robotY = mouseY;
        
        window.addEventListener('mousemove', (e) => {
            mouseX = e.clientX;
            mouseY = e.clientY;
            
            // Only initialize and show robot if a real mouse is moved (solves mobile issue)
            if (!robotInitialized) {
                robotInitialized = true;
                const robot = document.getElementById('cursor-robot');
                if (robot) robot.classList.remove('opacity-0');
                animateRobot();
            }
        });
        
        function animateRobot() {
            const robot = document.getElementById('cursor-robot');
            const eyeL = document.getElementById('robot-eye-l');
            const eyeR = document.getElementById('robot-eye-r');
            
            robotX += (mouseX - robotX) * 0.08;
            robotY += (mouseY - robotY) * 0.08;
            
            if (robot) {
                robot.style.transform = `translate(${robotX + 20}px, ${robotY + 20}px)`;
                
                const dx = mouseX - robotX;
                const dy = mouseY - robotY;
                const tilt = Math.max(-20, Math.min(20, dx * 0.15));
                
                if (robot.firstElementChild) {
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
            }
            requestAnimationFrame(animateRobot);
        }
"""

# Find the last </script> and inject before it
last_script_idx = content.rfind("</script>")
if last_script_idx != -1:
    content = content[:last_script_idx] + robot_js + content[last_script_idx:]

with open("index.html", "w") as f:
    f.write(content)

print("Robot fully fixed.")
