## 2025-01-24 - Navigation Accessibility & Semantic Refactor
**Learning:** Refactoring non-semantic elements (like `div`) to semantic ones (like `<a>` or `<button>`) in a legacy CSS environment can introduce visual regressions due to default browser styles (e.g., underlines) or flexbox behavior changes. For example, a branding logo converted to a link might wrap unexpectedly in a flex container unless `white-space: nowrap` is applied.
**Action:** Always verify visual layout in various viewports after semantic refactoring, and use explicit CSS resets (like `text-decoration: none`, `background: none`, `white-space: nowrap`) to maintain the original design intent when upgrading to semantic HTML.

**Learning:** Fixed headers often obscure anchor link targets. While traditional fixes involve padding-top/margin-top offsets on every target, a more centralized and robust approach is using `scroll-padding-top` on the `<html>` element.
**Action:** Use `scroll-padding-top: [header-height]` on the global HTML selector to ensure all internal navigation targets are correctly positioned below a fixed header.
