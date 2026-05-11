## 2025-05-14 - [Mobile Navigation Accessibility]
**Learning:** In projects with custom-styled UI components, interactive elements like mobile menu toggles are often implemented as non-semantic `div` tags, which are invisible to screen readers and inaccessible via keyboard.
**Action:** Always convert custom interactive `div` elements to semantic `<button>` elements, add appropriate ARIA attributes (`aria-label`, `aria-expanded`, `aria-controls`), and ensure `:focus-visible` styles are provided for keyboard users.
