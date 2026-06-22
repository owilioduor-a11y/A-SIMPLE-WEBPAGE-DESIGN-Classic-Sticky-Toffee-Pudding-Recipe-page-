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
