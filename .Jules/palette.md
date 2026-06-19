## 2026-06-14 - Semantic Mobile Navigation
**Learning:** Transitioning from non-semantic `div` elements to semantic `<button>` tags for mobile menus requires explicit CSS resets (background: none, border: none, padding: 0) to maintain design consistency. Synchronizing `aria-expanded` and `aria-label` through a centralized JavaScript function ensures a predictable and accessible experience for assistive technology users.
**Action:** Always prefer semantic `<button type="button">` for interactive elements and use a helper function to manage multi-attribute ARIA state updates.

## 2026-06-15 - Anchor Navigation with Fixed Headers
**Learning:** Fixed headers can obscure anchor link targets. Implementing `scroll-padding-top` on the `<html>` element provides a global, CSS-native solution to this UX friction without requiring JavaScript offsets.
**Action:** Always check anchor link visibility on sites with `position: fixed` headers and apply appropriate `scroll-padding-top`.

## 2026-06-15 - Semantic Branding and Skip Links
**Learning:** For users relying on keyboard navigation or screen readers, a "Skip to Content" link is essential for bypassing repetitive headers. Additionally, branding elements should always be semantic links (`<a>`) with descriptive `aria-label`s to ensure a consistent "Home" navigation path.
**Action:** Include "Skip to Content" links as a standard accessibility baseline and ensure branding is implemented as an interactive, labeled element.

## 2026-06-19 - Print-Friendly Recipe Layouts
**Learning:** For luxury dark-themed websites, print-friendly CSS must explicitly override the background to white (#ffffff) and text to black (#000000) using `!important` to ensure legibility and ink efficiency. Hiding non-essential UI elements like navigation, footers, and large hero images creates a focused, professional-grade printed document that users value.
**Action:** Always include a `@media print` block for content-heavy pages like recipes, ensuring high contrast and removing distractions.
