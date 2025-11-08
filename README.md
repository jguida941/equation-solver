# Equation Solver Companion

This repository accompanies the FreeCodeCamp project **“Python: Learn Interfaces by Building an Equation Solver”**. It now contains two parallel versions of the starter code so you can pick the level of guidance you prefer while working through the lesson.

## What's Inside
- `equation_solver_explained.py` - mirrors the FCC instructions line-by-line with extensive inline commentary, reminders, and tips. Use this version when you want extra context on every construct.
- `equation_interface_clean.py` - the same scaffolding without the walkthrough comments. Use it when you just need the interface skeleton or want a clean slate for your own notes.

## How to Use
1. Open `equation_solver_explained.py` while following Step 1 of the FCC lesson: <https://www.freecodecamp.org/learn/scientific-computing-with-python/learn-interfaces-by-building-an-equation-solver/step-1>. Read the comments before each block - they summarize the intent of the corresponding lesson step and explain why each piece of syntax is there.
2. When you're ready to build without the extra narration, switch to `equation_interface_clean.py`. It has the same structure, so you can copy over your implementations or retype them for practice.
3. Replace the placeholder `pass` statements with your own logic as you progress through the course challenges. Keep both files in sync if you like comparing the verbose and clean versions.

## Running the Files
Either script works with any modern Python 3.x environment:
```bash
python3 equation_solver_explained.py
# or
python3 equation_interface_clean.py
```
Both files currently define the interface and a stub implementation, so running them now mainly serves as a syntax check. As you complete the FCC project, executing either script will let you test your solver logic.

## Suggested Next Steps
- Implement `LinearEquation.solve()` and `.analyze()` once you reach the corresponding FCC tasks.
- Add more subclasses (quadratic, polynomial, etc.) to experiment with how abstract base classes enforce contracts.
- Keep expanding the inline commentary in the explained version, or add your own notes in the clean file, so future you has a handy reference.
