## 2024-05-23 - Semantic Mobile Navigation
**Learning:** Using `div` for mobile menu toggles breaks keyboard accessibility. Refactoring to a semantic `button` with `aria-expanded` and `aria-label` provides necessary context for screen readers and ensures the element is focusable in the tab order.
**Action:** Always use `<button type="button">` for interactive toggles and synchronize ARIA states with the UI state via JavaScript.
