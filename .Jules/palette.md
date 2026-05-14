# Palette's Journal - Critical UX Learnings

## 2025-05-24 - [Accessible Luxury Focus States]
**Learning:** For luxury dark-themed interfaces, standard browser focus rings are often suppressed or visually jarring. Using `:focus-visible` with a brand-aligned color (e.g., gold) and an offset (`outline-offset`) maintains the aesthetic while providing critical feedback for keyboard users without affecting layout dimensions.
**Action:** Always implement a custom `:focus-visible` style that uses the site's primary accent color and ensures sufficient contrast against dark backgrounds.
