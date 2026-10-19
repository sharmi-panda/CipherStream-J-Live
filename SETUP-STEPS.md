# How to add this kit to your CipherStream repo

1. Unzip the kit on your computer.
2. Open https://github.com/sharmi-panda/CipherStream-J-Live and sign in.
3. Click "Add file", then "Upload files". Drag `mkdocs.yml` and the `docs` folder (it includes the `images` folder) into the page. Wait until every file is listed, then click "Commit changes".
4. Click "Add file", then "Create new file". In the name box, type `.github/workflows/docs.yml` (typing the slashes creates the folders). Open `.github/workflows/docs.yml` from the kit, copy everything, paste it into the editor, and click "Commit changes".
5. Open the "Actions" tab and wait for "Deploy docs" to show a green tick. If it does not start by itself, click "Deploy docs" on the left, then "Run workflow".
6. Open Settings, then Pages. Under "Build and deployment", set Source to "Deploy from a branch", choose the `gh-pages` branch and the `/ (root)` folder, and click Save.
7. After a minute, open https://sharmi-panda.github.io/CipherStream-J-Live/ and check every page and screenshot.

If the Actions run fails with a permissions error: open Settings, then Actions, then General, set "Workflow permissions" to "Read and write permissions", save, and run the workflow again.
