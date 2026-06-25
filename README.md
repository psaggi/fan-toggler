# fan-toggler
On/Off fan with Alexa and Streamdeck

Problem - Fan is connected to an Alexa smart-plug but Alexa doesn't have an app for Elgato Streamdeck which is my desktop-based controller.

Solution - Program a key on Elgato to launch a .bat file that fires a Python script which spins up a temporary Chrome instances that goes to alexa.com, finds the fan controller card and toggles it on/off. It uses Playwright.

Credit - Claude Code

Lessons Learned - 
    Claude is pattern matching and comes up with bad solutions (like it did in this case) before settling on a good solution.
    LLMS are trained on info that may be outdated so before going down a rabbit hole, use human judgement and verification.
    Multiple ways to solve a problem - avoid using ways that become significant security loopholes. 

Requires
    Python, Playwright - use pip install to install them
