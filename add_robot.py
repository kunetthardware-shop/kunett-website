import re

with open("index.html", "r") as f:
    content = f.read()

# 1. Inject the Robot SVG right after body opens
robot_html = """<body class="bg-brand-offwhite text-brand-black font-sans antialiased overflow-x-hidden pt-20 selection:bg-brand-black selection:text-white">

    <!-- Flying Robot Cursor Companion -->
    <div id="cursor-robot" class="hidden md:block fixed pointer-events-none z-[9999] will-change-transform" style="top: 0; left: 0; transform: translate(-100px, -100px);">
        <svg width="36" height="36" viewBox="0 0 100 100" fill="none" xmlns="http://www.w3.org/2000/svg" class="drop-shadow-lg">
            <!-- Antenna Base & Stick -->
            <line x1="50" y1="20" x2="50" y2="5" stroke="#111" stroke-width="4" stroke-linecap="round"/>
            <circle cx="50" cy="5" r="5" fill="#E23E57" class="animate-pulse"/>
            <!-- Head Main -->
            <rect x="20" y="20" width="60" height="50" rx="12" fill="#1A1A1A"/>
            <!-- Screen/Face plate -->
            <rect x="25" y="25" width="50" height="30" rx="6" fill="#0A0A0A"/>
            <!-- Eyes -->
            <circle id="robot-eye-l" cx="35" cy="40" r="5" fill="#00FFCC"/>
            <circle id="robot-eye-r" cx="65" cy="40" r="5" fill="#00FFCC"/>
            <!-- Mouth / Vent -->
            <rect x="40" y="60" width="20" height="4" rx="2" fill="#333"/>
        </svg>
    </div>"""

content = re.sub(r'<body.*?>', robot_html, content)


# 2. Inject the Robot Animation Logic inside the main script
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
            // Lerp for smooth floating effect (0.06 = slight delay/spring)
            robotX += (mouseX - robotX) * 0.06;
            robotY += (mouseY - robotY) * 0.06;
            
            // Offset so the robot floats slightly below and to the right of the cursor
            if (robot) {
                robot.style.transform = `translate(${robotX + 25}px, ${robotY + 25}px)`;
            }
            
            // Calculate distance to tilt the robot slightly when moving fast
            const dx = mouseX - robotX;
            const dy = mouseY - robotY;
            const tilt = Math.max(-15, Math.min(15, dx * 0.1));
            
            if (robot && robot.firstElementChild) {
                robot.firstElementChild.style.transform = `rotate(${tilt}deg)`;
                robot.firstElementChild.style.transition = 'transform 0.1s linear';
            }
            
            // Micro-interaction: Make eyes look towards the mouse
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
        // Only run on desktop/larger screens so it doesn't break mobile touch
        if (window.innerWidth > 768) {
            animateRobot();
        }

        // Add to history state so back button works
"""

content = content.replace("// Add to history state so back button works", robot_js)

with open("index.html", "w") as f:
    f.write(content)

print("Robot added.")
