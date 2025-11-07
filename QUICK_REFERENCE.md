# 🚀 Quick Reference - Portfolio Animations

## 🎯 Most Used Animation Classes

### Basic Scroll Animations
```html
<!-- Fade in when scrolled into view -->
<div class="reveal">Content</div>

<!-- Fade in and slide up -->
<div class="fade-in-up">Content</div>

<!-- Slide from left -->
<div class="slide-in-left">Content</div>

<!-- Slide from right -->
<div class="slide-in-right">Content</div>
```

### Stagger Delays (for multiple elements)
```html
<div class="reveal">First</div>
<div class="reveal delay-200">Second (200ms later)</div>
<div class="reveal delay-400">Third (400ms later)</div>
```

### Interactive Cards
```html
<!-- Hover lift effect -->
<div class="card-hover">Card</div>

<!-- 3D tilt on mouse move -->
<div class="card-3d">Card</div>

<!-- Skill card with shimmer -->
<div class="skill-card">Card</div>
```

### Buttons
```html
<!-- Glow + Ripple effect -->
<button class="btn-glow btn-ripple">Click Me</button>

<!-- Magnetic button (follows cursor) -->
<button class="magnetic-btn">Hover Me</button>
```

### Text Effects
```html
<!-- Animated gradient text -->
<h1 class="gradient-text-animated">Title</h1>

<!-- Counter animation -->
<span class="counter" data-count="100">0</span>
```

### Special Effects
```html
<!-- Floating animation -->
<div class="float">Floats up and down</div>

<!-- Glassmorphism -->
<div class="glass">Glass effect</div>

<!-- Parallax -->
<div class="parallax" data-speed="0.5">Moves on scroll</div>
```

## 🎨 Color Variables

```css
Primary Gradient: from-[#9de1f5] to-[#33c46b]
Hover Color: #33c46b
Dark Background: #101923
Card Background: #182534
Border Color: #314b68
```

## 📱 Test Your Animations

Visit: `http://localhost:5000/animations-demo`

## 🔧 Common Tasks

### Add animation to new element:
1. Add `reveal` class for scroll animation
2. Add `delay-XXX` for stagger effect
3. Add specific animation class (card-hover, btn-glow, etc.)

### Adjust animation speed:
Edit `static/css/input.css` and change `duration` values

### Rebuild CSS after changes:
```bash
npm run build:css
```

### Restart server:
```bash
python app.py
```

## 🎯 Pro Tips

1. **Don't overuse**: 2-3 animation types per page is enough
2. **Stagger delays**: Use 100-200ms between elements
3. **Test on mobile**: Animations should work on touch devices
4. **Performance**: Use `transform` and `opacity` for smooth animations
5. **Accessibility**: Animations respect `prefers-reduced-motion`

## 🐛 Quick Fixes

**Animations not showing?**
- Check if `animations.js` is loaded
- Run `npm run build:css`
- Clear browser cache

**Animations too slow/fast?**
- Edit duration in CSS (e.g., `0.3s` → `0.5s`)

**Elements not revealing?**
- Make sure element has `reveal` class
- Check if element is in viewport

## 📚 Files to Know

- `static/css/input.css` - All animation styles
- `static/js/animations.js` - JavaScript animations
- `templates/base.html` - Base template with scripts
- `templates/index.html` - Home page with animations

## 🎉 Your Animation Stack

✅ Scroll reveal animations
✅ 3D card effects
✅ Button interactions
✅ Text animations
✅ Progress bars
✅ Parallax effects
✅ Magnetic buttons
✅ Ripple effects
✅ Gradient animations
✅ Glassmorphism
✅ Custom scrollbar
✅ Scroll progress bar
✅ Social icon animations
✅ Form input animations
✅ Navbar scroll effects

**Everything is ready to go! 🚀**
