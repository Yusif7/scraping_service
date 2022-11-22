…or create a new repository on the command line
echo "# scraping_service" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Yusif7/scraping_service.git
git push -u origin main


…or push an existing repository from the command line
git remote add origin https://github.com/Yusif7/scraping_service.git
git branch -M main
git push -u origin main


Git status
The Git status command gives us all the necessary information about the current branch. 
Git add . - for everything
Git commit - Once we reach a certain point in development, we want to save our changes 
Git push - After committing your changes, the next thing you want to do is send your changes to the remote server. 
Git revert - Sometimes we need to undo the changes that we've made.