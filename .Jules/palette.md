## 2024-05-24 - Semantic Navigation & Fixed Header UX

**Learning:** Fixed headers in single-page layouts often obscure anchor targets. Using `scroll-padding-top` on the `<html>` element is a clean, CSS-only solution to ensure headings remain visible after navigation. Additionally, converting branding logos from static `<div>`s to `<a>` tags significantly improves site discoverability and home navigation for both mouse and keyboard users.

**Action:** Always include `scroll-padding-top` when implementing fixed headers and ensure branding elements are semantic links with descriptive `aria-label` attributes.
