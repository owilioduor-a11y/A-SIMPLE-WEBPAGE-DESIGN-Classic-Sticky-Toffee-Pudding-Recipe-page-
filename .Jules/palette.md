# Palette's UX Journal

## 2024-05-22 - Improving Header Navigation Accessibility
**Learning:** Using non-semantic elements like `div` for interactive components (logo links, mobile menus) creates accessibility barriers for keyboard and screen reader users. Semantic elements like `<a>` and `<button>` provide built-in focusability and roles.
**Action:** Always refactor static branding and toggles into semantic `<a>` and `<button>` elements with appropriate ARIA attributes for state management.
## 2024-05-23 - Semantic Mobile Navigation
**Learning:** Using `div` for mobile menu toggles breaks keyboard accessibility. Refactoring to a semantic `button` with `aria-expanded` and `aria-label` provides necessary context for screen readers and ensures the element is focusable in the tab order.
**Action:** Always use `<button type="button">` for interactive toggles and synchronize ARIA states with the UI state via JavaScript.
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

## 2026-06-24 - Dynamic Checklist Injection and Persistence
**Learning:** For static sites with repetitive content (like recipe ingredients), using JavaScript to dynamically inject interactive elements (e.g., checkboxes wrapped in labels) is a highly efficient way to stay under strict code change limits while significantly enhancing UX. Pairing this with `localStorage` persistence (keyed by trimmed text content) provides a seamless "save-as-you-go" experience for users.
**Action:** Use JS-driven DOM enhancement for large-scale UX upgrades to maintain lean static source code and implement `localStorage` for any multi-step or tracking tasks.
## 2026-06-24 - Progressive Enhancement with CSS :has()
**Learning:** Implementing interactive checklists using the CSS `:has()` selector allows for clean, state-driven styling (like strikethroughs) without manual class management in JavaScript. For persistent states like recipe progress, `localStorage` keys based on a segment of the item's text content provide better stability than indices if the list order changes.
**Action:** Use `:has()` for conditional parent styling based on input states and prefer text-based content keys for persisting individual item states in dynamic lists.
## 2026-06-30 - Dynamic Ingredient Checklists & Persistence
**Learning:** Transforming static recipe lists into interactive checklists improves kitchen-time UX. Using `localStorage` with keys based on the page path and item index/text ensures state persistence across sessions without a backend. The `:has()` CSS selector allows for clean, declarative styling of completed states based on internal checkbox status.
**Action:** Use unique, stable keys for `localStorage` to avoid state leakage between pages and leverage modern CSS selectors like `:has()` for state-driven UI updates.
## 2026-07-08 - Interactive Recipe Checklists & Persistence
**Learning:** Adding interactive checkboxes to recipe ingredients and instructions using JavaScript injection allows for a "checklist" experience without modifying the underlying static HTML structure. Using `localStorage` keyed by content and path ensures progress is saved across sessions. The CSS `:has()` selector simplifies visual feedback (strikethrough/opacity) for completed tasks without requiring manual class toggling in JS.
**Action:** Implement progress-tracking checklists on instruction-heavy pages using JS injection, `localStorage` for persistence, and `:has()` for state-based styling.

## 2026-08-13 - State Reset Experience & Accessible Live Regions
**Learning:** Providing a way to reset checklists is essential for user retention and repeat cooking sessions. When clearing checklist states programmatically, dynamic feedback via an `aria-live` polite announcer is crucial to inform screen reader users that the action succeeded.
**Action:** Accompany batch list clearing actions with a dynamic hidden screen-reader announcement to maintain sensory synchronicity for visually impaired users.
