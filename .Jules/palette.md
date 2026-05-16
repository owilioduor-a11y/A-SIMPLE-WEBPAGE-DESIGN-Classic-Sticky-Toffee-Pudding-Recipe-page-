## 2024-05-22 - [Enhancing Keyboard Discoverability in Luxury UIs]
**Learning:** Luxury interfaces often use minimal or non-standard interactive elements (like <div> toggles) that are invisible to keyboard users. Refactoring these to semantic <button> elements while resetting default browser styles maintains the aesthetic while providing critical accessibility.
**Action:** Always check navigation toggles for semantic correctness and implement :focus-visible with an offset to avoid clashing with tight design borders.
