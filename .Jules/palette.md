# Palette's UX Journal

## 2024-05-24 - [Semantic Navigation & Mobile Accessibility]
**Learning:** The "Classic Dinner Resort" template utilizes `div` elements for critical navigation components (Logo and Mobile Menu Toggle). While visually appealing, this pattern excludes keyboard users and screen readers, as `div` elements are not focusable or identifiable as interactive by default. Additionally, the fixed header can overlap content when navigating via anchor links if `scroll-padding-top` is missing.
**Action:** Replace interactive `div` elements with semantic `<button>` or `<a>` tags. Implement `aria-expanded` and `aria-controls` for state management, and add `scroll-padding-top` to the global `html` element to ensure content visibility after navigation.
