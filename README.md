-----------------------------------------
✅ 1st Time: Push Django Project to GitHub
-----------------------------------------

# Step 1: Go to your project folder
cd E:/Coding/Djangohp/anshp

# Step 2: Initialize Git
git init

# Step 3: Add .gitignore file (optional but recommended)
# (Create .gitignore file and add Django rules)

# Step 4: Add all files to Git
git add .

# Step 5: Make your first commit
git commit -m "Initial commit"

# Step 6: Add GitHub repo URL
git remote add origin https://github.com/yourusername/your-repo-name.git

# Step 7: Set branch to main (if needed)
git branch -M main

# Step 8: Push to GitHub
git push -u origin main


-------------------------------------------------
🔄 Future Updates: After Making Any Code Changes
-------------------------------------------------

# Step 1: Add changes to staging area
git add .

# Step 2: Commit changes with a message
git commit -m "Updated: your message here"

# Step 3: Push changes to GitHub
git push


-------------------------------
📝 Tip: Sample .gitignore for Django
-------------------------------
__pycache__/
*.pyc
*.pyo
*.pyd
*.sqlite3
*.log
env/
venv/
*.env
.DS_Store
*.idea/
*.vscode/
staticfiles/
media/


-----------------------------------------
✅ Notes:
-----------------------------------------
- Use `git status` to check what files changed.
- Always commit with a clear message.
- Replace "yourusername/your-repo-name.git" with your actual GitHub repo URL.
