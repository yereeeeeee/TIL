# GIT

Working directory / staging area / Repository

Working dir 에 있는 파일 중 사용할 것만
Staging area에 올려놓고,

올려놓은 파일의 변동사항만 tracking(기록)

기록 내용(변동 사항)은 repository로 이동 후 staging area는 비움

---
- `git init` : git으로 관리 시작 
- `git add {file name}` : staging area에 등록 (tracking 시작)
- `git commit -m "version name"` : commit으로 version 등록
- `git config --global user.###` : user 설정
- `git config --global --list` : 설정 목록 확인
- `git status` : 변동 사항 유무 등 상태 확인
- Repository == .git 폴더
- version 마다 고유값 부여 (`git log`에서 확인 가능, 최신버전을 위에 보여준다.)
- `git log --oneline` : 한 줄에 commit 확인 가능

  - commit 시 변동 사항만 넣어 놓는 걸로


---
- commit은 언제 찍는 게 좋을까? 쉬는시간 마다 `add commit` 추천

---

- 변동사항이 있으면 `git add`로 추가해주고 `git status` 확인( = staging area에 올려주기)

      changes not staged for commit: 이후 내용은 working directory에서 수정사항이 있었으나 staging area로 보내지지 않은 내용을 알려줌
- `git add`가 다 끝나고 `git status` 확인 후 이상이 없다면 `git commit -m`

- `git commit --amend` : commit 내용 수정 (Vi)

        -- INSERT -- : 삽입 모드 (push 'i')
        :wq : (삽입 모드 아닌 상태에서) 종료

- `git add .` : 현재 폴더에 발생한 모든 변동사항 add
- `git remote add origin {주소(URL)}` : git에 원격 저장소 등록 (= origin이라고 하는 {주소}에 git을 등록하겠다.) / 지울땐 `add` 대신 `remove`
- `git remote -v` : remote 리스트 확인
- `git push origin master` : 업로드(최초 업로드 이후 `git push`만 입력해도 업로드 되도록 설정 가능)
  
        자격 증명 관리자에서 github 연결 관리 가능
        git lab 도 같은 방법으로 가능하나 origin 대신 gitlab이라는 이름 사용
        git hub는 origin! git lab은 gitlab!

- `git clone {원격 저장소 주소}` : 저장된 파일 다운로드
- `git remote rename {원래 이름} {수정될 이름}`
- `git pull {저장소} master` : push된 파일 불러오기

---
---
# 하루 루틴
## pull - 수정 - 저장 - add - commit - push
> `git pull origin master`
> 
> `start .`
> 
> `code {}`
> 
> `ctrl + s`
> 
> `git status`
> 
> `git add .`
> 
> `git commit -m "###"`
> 
> `git push origin master`
---
---

1. 강의장에서 새 파일 생성
2. add commit push (gitlab으로 푸시)
--- 
3. 집 git pull
1. 집에서 새 파일 생성
2. add commit push
---
6. 강의장에서 git pull gitlab master
---
---

# 오류 발생
## 강의장에서 push를 안하고 갔을 때
> 집에서 push를 하고 강의장에서 pull을 하면 버전이 달라진다.
> 
> 그때는 다른 merge 창이 뜬다.

## pull을 안했을 때
> rejected 될 수 있다.
>
> error msg가 뜰 예정
>
> pull 하고 merge
>
> (이름 바꾸고 싶으면 insert - {이름 변경} - esc - : wq)
>

## pull을 안 한 파일에 덮어 썼을 때
> conflict
>
> 파일을 확인하면 변경 사항 선택 가능함
>

---
---
# .gitignore
> GIT으로 관리하지 않을 파일 목록을 적어둔 텍스트 파일 
>
> 파일명, 폴더명, 경로/파일명 >> 상대 경로
>
> ※ .git 폴더와 같은 위치에 .gitignore를 만드는 게 좋음
>
> gitignore.io 사이트 참고
> (windows, vscode, python, django, vue, vue.js, pycharm)
>
> 처음에 git 셋팅 시
> 1. `git init`
> 2. `.gitignore`