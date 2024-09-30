# Deploy the docs to the `docs` branch.

git branch -D docs-preview
git checkout -b docs-preview
sed -i '' '/dist/d' .gitignore
npm run build
git add .
git commit -m "Update docs"
git push origin docs-preview -f
git checkout -