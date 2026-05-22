## 2024-05-24 - [Accessible Navigation with Fixed Headers]
**Learning:** Fixed headers can obscure anchored content (like "Skip to Content" targets) when navigating via keyboard or hash links. Using `scroll-padding-top` on the `html` element is a clean, CSS-only solution to ensure focused elements are not hidden under the navigation bar.
**Action:** Always check for fixed headers when implementing in-page navigation or accessibility features like "Skip to Content" links, and apply `scroll-padding-top` equal to the header's height.
