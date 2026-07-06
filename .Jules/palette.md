## 2026-06-15 - [Semantic and Accessible Navigation]
**Learning:** Converting non-semantic elements (like `div`) to semantic ones (`button`, `a`) significantly improves accessibility but requires careful CSS resets (background, border, padding) to maintain visual design. ARIA attributes must be dynamically updated via JS to reflect state changes for screen readers.
**Action:** Always prefer `<button>` for interactions and `<a>` for navigation. Include `:focus-visible` styles early to ensure keyboard accessibility. Use a centralized state management function in JS to keep ARIA attributes in sync with visual classes.
## 2026-06-14 - Semantic Mobile Navigation
**Learning:** Transitioning from non-semantic `div` elements to semantic `<button>` tags for mobile menus requires explicit CSS resets (background: none, border: none, padding: 0) to maintain design consistency. Synchronizing `aria-expanded` and `aria-label` through a centralized JavaScript function ensures a predictable and accessible experience for assistive technology users.
**Action:** Always prefer semantic `<button type="button">` for interactive elements and use a helper function to manage multi-attribute ARIA state updates.

## 2026-06-15 - Fixed Headers and Keyboard Accessibility
**Learning:** Fixed headers can obscure content when navigating via anchor links or when using a keyboard to "Skip to content". Using `scroll-padding-top` on the `<html>` element is a clean CSS-only solution to ensure the target element is positioned below the header. Additionally, a "Skip to content" link must be the first focusable element to provide efficient navigation for keyboard-only users.
**Action:** Always check for fixed headers and implement `scroll-padding-top` alongside a functional "Skip to content" link.
## 2026-06-15 - Anchor Navigation with Fixed Headers
**Learning:** Fixed headers can obscure anchor link targets. Implementing `scroll-padding-top` on the `<html>` element provides a global, CSS-native solution to this UX friction without requiring JavaScript offsets.
**Action:** Always check anchor link visibility on sites with `position: fixed` headers and apply appropriate `scroll-padding-top`.

## 2026-06-15 - Semantic Branding and Skip Links
**Learning:** For users relying on keyboard navigation or screen readers, a "Skip to Content" link is essential for bypassing repetitive headers. Additionally, branding elements should always be semantic links (`<a>`) with descriptive `aria-label`s to ensure a consistent "Home" navigation path.
**Action:** Include "Skip to Content" links as a standard accessibility baseline and ensure branding is implemented as an interactive, labeled element.

## 2026-06-16 - Print-Friendly Utility & Focus Contrast
**Learning:** Utility features like "Print Recipe" require robust `@media print` overrides to ensure dark-themed sites remain legible and ink-efficient on paper. This includes resetting backgrounds to white, text/pseudo-elements to black, and hiding non-content UI. For gold-themed interactive elements on dark backgrounds, a white `:focus-visible` outline provides the necessary contrast for keyboard accessibility.
**Action:** Implement comprehensive print media queries for content-heavy pages and always verify focus indicator contrast against the brand's primary action colors.

## 2026-06-23 - Interactive Feedback & Document Hygiene
**Learning:** Providing immediate visual feedback for simulated asynchronous actions (like form submissions) significantly improves the perceived responsiveness of static sites. Additionally, maintaining a clean document structure—by removing duplicate `<body>` tags and redundant navigation links—prevents accessibility regressions and ensures reliable behavior in automated verification environments.
**Action:** Implement text-based state changes (e.g., "Checking...", "Reserved!") for interactive forms and audit HTML structure for redundant semantic markers.

## 2026-07-10 - Dynamic Checklist Injection
**Learning:** For content-heavy lists like recipes, dynamically injecting interactive checkboxes via JavaScript preserves semantic HTML while adding UX value without manual editing of hundreds of static items. Using the `:has()` selector allows for elegant visual feedback (strikethrough) based on the input state, and leveraging `localStorage` with content-derived keys ensures progress persistence without a backend.
**Action:** Use JS-driven enhancement for repetitive list items to keep HTML clean and minimize line counts in static site refactors. Always include print-specific CSS to hide interactive elements.
