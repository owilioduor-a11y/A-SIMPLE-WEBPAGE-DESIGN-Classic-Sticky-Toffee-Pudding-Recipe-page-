## 2025-05-31 - [Semantic Mobile Navigation]
**Learning:** Refactoring static <div>-based mobile menus to semantic <button> elements improves screen reader accessibility but can break desktop-specific CSS if tag-qualified selectors (e.g., `div.menu-toggle`) or implicit display properties are relied upon.
**Action:** Always explicitly hide mobile-only interactive components (like menu toggles) in the base CSS using `display: none` and only enable them within the appropriate media queries.

## 2025-05-31 - [Skip to Content Implementation]
**Learning:** A "Skip to content" link is a high-impact, low-effort accessibility win for keyboard users. It must be the first focusable element in the DOM and use `scroll-padding-top` on the root element to account for fixed headers.
**Action:** Ensure `<main>` has a unique ID and the link is visually hidden but accessible on focus.
