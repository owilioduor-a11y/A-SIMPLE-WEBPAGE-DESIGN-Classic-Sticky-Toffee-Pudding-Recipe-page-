## 2024-05-24 - Semantic and Accessible Navigation in Fixed Header Layouts
**Learning:** Fixed headers often obscure anchor link targets, making internal navigation feel broken for users. Additionally, using `div` for interactive elements like mobile toggles or logos excludes keyboard and screen reader users.
**Action:** Use `scroll-padding-top` on the `html` element to offset fixed headers. Always use semantic `<button>` and `<a>` tags for interactions, and synchronize ARIA states (like `aria-expanded`) in JavaScript to maintain accessibility tree integrity.
