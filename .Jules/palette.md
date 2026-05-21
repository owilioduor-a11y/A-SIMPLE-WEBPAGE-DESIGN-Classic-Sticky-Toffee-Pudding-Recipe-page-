## 2024-05-21 - [Mobile Header UX & Accessibility]
**Learning:** Fixed headers with multiple elements (logo, CTA, menu toggle) often suffer from layout congestion and overlap on mobile viewports (< 768px). Additionally, <div>-based toggles and static logos hinder navigation and accessibility.
**Action:** Prioritize the logo and menu toggle on mobile by hiding non-essential CTAs in the header. Always use semantic `<button>` elements for toggles with full ARIA support (`aria-expanded`, `aria-controls`) and wrap brand logos in home-bound links.
