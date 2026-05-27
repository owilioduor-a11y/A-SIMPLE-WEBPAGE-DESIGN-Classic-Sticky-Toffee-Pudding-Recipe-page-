## 2026-05-27 - [Accessibility & Header UX]
**Learning:** Using non-semantic `div` elements for interactive components like the logo and mobile menu toggle hinders keyboard accessibility and screen reader navigation. Additionally, fixed headers without `scroll-padding-top` cause anchor link targets to be obscured upon navigation.
**Action:** Always refactor interactive `div`s to semantic `<button>` or `<a>` tags with appropriate ARIA attributes (`aria-expanded`, `aria-label`). Implement `scroll-padding-top` on the `html` element to match the header height for a smoother jump-link experience.
