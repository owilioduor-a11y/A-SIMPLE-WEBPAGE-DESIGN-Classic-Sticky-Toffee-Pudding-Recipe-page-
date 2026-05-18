## 2025-05-15 - [Luxury Dark Theme Focus Indicators]
**Learning:** In luxury dark-themed interfaces, default browser focus indicators are often invisible or aesthetically jarring. Using a high-contrast theme-aligned color (like gold) with `:focus-visible` and `outline-offset` provides clear accessibility without compromising the premium aesthetic.
**Action:** Always implement custom `:focus-visible` styles that use the primary brand accent color and `outline-offset` to ensure visibility on dark backgrounds.

## 2025-05-15 - [Semantic Mobile Toggles]
**Learning:** Transitioning from `div`-based mobile menu toggles to semantic `<button>` elements with `aria-expanded` and `aria-controls` is essential for screen reader users to understand the state and purpose of the navigation.
**Action:** Replace all interactive `div` or `span` elements with semantic `<button>` or `<a>` tags and manage state with appropriate ARIA attributes.
