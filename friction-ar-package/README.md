# Friction AR — complete website package

Live AR: https://touch-gesture-iphone7.seohm25.chatgpt.site/ar/
The included QR code and NFC link point to this live address.

## Contents
- `out/`: the complete static website, including the original Touch Gesture page and `/ar/` experience.
- `out/ar/assets/frictionAR.glb`: the mobile-optimized exhibition artwork.
- `out/ar/assets/tap.glb`: the 3D Tap start control.
- `out/ar/assets/targets.mind`: recognition data for both supplied poster designs.
- `out/ar/vendor/`: locally hosted AR/3D libraries and licenses; no CDN download is required.
- `qr/`: QR PNG, print-ready SVG, and the NFC URL.
- `.openai/hosting.json`: configuration for the existing Sites project (no credentials).

All files required to run the website are included. The much larger original authoring models, reference photos and source PDFs already on your computer are not duplicated. The optimized models included here are the exact models used by the published website.

## Open on your Mac
With Python 3 installed, double-click `START-LOCAL.command`, or run:

    python3 serve.py

The browser opens at http://localhost:8765/ar/. Keep the terminal open while using it; press Control-C to stop. If that port is in use, use `python3 serve.py 8766` instead.

Do not open the HTML by double-clicking it: camera access and model loading require a web server.

## Use on phones / publish elsewhere
Upload the contents of `out/` to an HTTPS static host. Open `/ar/` in Safari or Chrome. A phone cannot use your Mac's localhost address. Use the live HTTPS link above for the exhibition. Hosting elsewhere requires a new QR code for that new URL.

Allow camera access and, if requested, Motion & Orientation access. Sensors help maintain the vertical arrangement when the poster lies flat. Without sensor access, camera-up is used as a fallback.

## Current interaction
- A blinking 3D Tap model opens the camera.
- The four artwork objects rotate automatically around the vertical Y axis, in alternating directions.
- Speeds remain approximately 24–29 seconds per revolution.
- No shake/bounce reaction is active.
- The full stack stays upright, with Tap at the bottom and Drag at the top.
- Reduced-motion device preferences disable the decorative rotation and blinking.

## Edit
`out/ar/app.js` controls the model layout and animation. The `spinRate` array controls signed rotation speeds in radians per second, and `part.rotation.y` selects the vertical Y axis (left/right turning).
`out/ar/style.css` controls the Tap screen. `tower-layout.js` and `motion.js` control placement and sensor handling.

Changing the website does not require a new QR code while its URL stays the same. Verify actual printed targets, lighting, framing, and motion permissions on exhibition phones before opening.

## 33 × 54 inch poster
When the complete target image fills the print, the initial virtual composition measures approximately 36.96 inches wide × 47.81 inches high (94 × 121 cm). It is proportional to the detected poster; rotation and perspective change the apparent screen width.
