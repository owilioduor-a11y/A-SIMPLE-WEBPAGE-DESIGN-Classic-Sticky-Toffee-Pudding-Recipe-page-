## 2024-05-22 - Enhanced Navigation Accessibility and UX

**Learning:** Fixed headers in single-page layouts often obscure the top of the target section when navigating via anchor links. Additionally, using `div` elements for interactive components like logos and menu toggles breaks keyboard accessibility.

**Action:**
- Apply `scroll-padding-top` to the `html` element to ensure content visibility after anchor link navigation.
- Use semantic `<button>` and `<a>` tags for all interactive elements.
- Implement `:focus-visible` styles to provide high-contrast focus indicators for keyboard users while maintaining a clean aesthetic for mouse users.
- Manage ARIA states (like `aria-expanded`) via JavaScript to ensure screen reader synchronization with the UI state.
