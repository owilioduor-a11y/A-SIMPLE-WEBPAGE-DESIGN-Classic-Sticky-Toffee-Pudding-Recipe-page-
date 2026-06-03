## 2024-05-24 - [Accessibility & Scroll UX Overhaul]
**Learning:** Fixed headers often obscure content when navigating via anchor links, requiring the use of `scroll-padding-top` on the root element. Additionally, refactoring non-semantic `div` toggles into `<button>` elements requires explicit CSS resets (background, border, padding) to preserve the original design while gaining critical ARIA support.
**Action:** Always apply `scroll-padding-top` when implementing a sticky/fixed header and use semantic `<button>` tags for interactive toggles to ensure screen reader compatibility.
