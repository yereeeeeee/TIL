# Git Undoing

## add 하기 전
`git restore {파일명}`

## add 한 뒤
`git rm --cashed {제거하고자 하는 파일명}`
- add 된 파일을 commit 하려는 목록에서 제거할 수 있음

## commit명 변경
`git commit --amend` => `vim`에서 수정 => `git log --oneline`에서 변경된 commit명 확인

## 이전 commit으로 돌아가는 법
1. `git reset --soft {gitID}` : commit 하기 직전으로 돌려준다. (add는 했을 때) (staging)
2. `git reset --mixed {gitID}` : 중간 (unstaging)
3. `git reset --hard {gitID}` : working directory에 있는 내용까지 사라진다.
4. `git revert {gitID}` : 해당 단계의 commit만 수정/삭제 된다. (이후 단계에는 영향을 미치지 않음) (단, commit 관리가 잘 되어있어야 함)

- 다 사라지는 건 아니고 `git reflog`에 남아있음
