# How to Contribute

## How to work
1. Clone
2. For first push `git push -u origin main`
3. To update the changes 
   ```bash
   git add .
   git commit -m "Your message"
   git push
   ```
4. To know the branch
  - `git branch`
5. Link to your remote GitHub repo
  - `git remote add origin <repo-url>`

### For every new Visit
1. Open your project folder in VS Code.
2. Check if your folder is connected to a GitHub repo:
   ```bash
   git remote -v
   ```
    - If you see your GitHub URL, you’re connected.
    - If not, connect using
    - ```bash
        git remote add origin <repo-url>
      ```
  3. Check you current brach `git branch`
  4. Pull the latest changes `git pull`
  5. Make your code changes
  6. Stage commit and push your changes
   - ```bash 
        git add .
        git commit -m "Your message"
        git push
   ```
