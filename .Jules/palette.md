## 2024-05-17 - [Accessible Navigation Enhancements]
**Learning:** Converting `div` based interactive elements to semantic `<button>` tags with appropriate ARIA attributes (`aria-expanded`, `aria-controls`) significantly improves accessibility for screen readers and keyboard users with minimal CSS overhead.
**Action:** Always prioritize semantic HTML elements for interactions and ensure state changes (like menu toggles) are programmatically communicated via ARIA attributes.

**Learning:** Global focus indicators using `:focus-visible` and a "Skip to main content" link are essential micro-UX improvements for keyboard navigability in content-heavy landing pages.
**Action:** Implement a standard `:focus-visible` style and a skip link as a baseline for all new projects.
