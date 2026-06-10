# Palette's UX Journal

## 2024-05-22 - Improving Header Navigation Accessibility
**Learning:** Using non-semantic elements like `div` for interactive components (logo links, mobile menus) creates accessibility barriers for keyboard and screen reader users. Semantic elements like `<a>` and `<button>` provide built-in focusability and roles.
**Action:** Always refactor static branding and toggles into semantic `<a>` and `<button>` elements with appropriate ARIA attributes for state management.
