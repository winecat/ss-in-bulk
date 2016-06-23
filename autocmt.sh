git add ss.php ss.sh README.md autocmt.sh .gitignore

echo '请给本次提交的写上有意义的注释':
read comments

git commit -m "$comments"

git push origin master

