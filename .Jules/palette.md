## 2024-05-23 - [Accessibility & Navigation Polish]
**Learning:** Fixed headers often obscure anchor link targets (e.g., #menu) in static landing pages. Using `scroll-padding-top` on the `<html>` element is a cleaner solution than adding top margins to sections, as it maintains consistent spacing across all internal navigations.
**Action:** Always implement `scroll-padding-top` equal to or slightly greater than the header height when using fixed navigation.

**Learning:** When refactoring non-semantic elements (like `div` toggles) into semantic ones (like `button`), explicit CSS resets for `background`, `border`, and `padding` are necessary to avoid default browser styling regressions.
**Action:** Include a dedicated "Semantics Reset" block in the CSS when converting divs to buttons or links to ensure visual consistency.
