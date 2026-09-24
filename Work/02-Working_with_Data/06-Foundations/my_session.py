# coding: utf-8
- `A` → Insert cell Above
- `B` → Insert cell Below
- `D D` → Delete a cell
- `M` → Change to Markdown cell
- `Y` → Change to Code cell
- `Shift + Enter` → Run cell and move to next
- `Ctrl + Enter` (`Cmd + Enter` on Mac) → Run cell, stay put
- `Alt + Enter` (`Option + Enter` on Mac) → Run cell and insert a new one below
# Save history to a file
get_ipython().run_line_magic('save', 'my_session.py 1-5')
