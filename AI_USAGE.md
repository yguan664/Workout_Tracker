# AI Usage

We used ChatGPT as a helper tool during development, mainly for debugging and small implementation guidance.

## How we used AI

### 1. Debugging and environment issues
We used AI to help identify and fix issues such as:
- Python import errors related to project structure (`src` vs package imports)
- Fixing test failures caused by incorrect imports
- Understanding how to properly use `conftest.py` to adjust Python path for pytest
- Resolving GitHub Actions failures (e.g., missing dependencies like `matplotlib`)

### 2. Git and workflow guidance
AI was used to clarify correct Git workflows, including:
- How to use branches and pull requests properly when two people are working simultaneously on Github
- How to handle merge conflicts and sync with `main`
- How to fix CI failures and re-run GitHub Actions correctly

### 3. Testing guidance
AI helped with:
- Ensuring tests were minimal but covered core functionality
- Understanding expected testing structure

## Summary

AI was used as a support tool to help debug issues, clarify concepts, and suggest small improvements. All major implementation decisions and final code were written and verified by us.
