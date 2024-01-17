폴더에서 `git bash 열기`

`pip install notebook`

`jupyter notebook` > 웹 페이지 열림

종료할 때는 웹 페이지에서 `File` > `Shut down`

다시 켤 때는 `jupyter notebook`
> 오류가 나면 작업관리자에서 jupyter notebook 찾아서 종료

---

## 활용법
파이썬을 사용할 수 있는 가상환경
실행할 코드 블락을 설정할 수 있다.

> 포커싱 해제 된 상태에서 `a` : 윗 줄에 코드 블락 생성
>
> 포커싱 해제 된 상태에서 `b` : 해당 블럭 아래에 코드 블럭 생성
> 
> `esc` : 포커싱 해제
> 
> `dd` : 해당 블럭 삭제
>
> 코드 블럭에서 `m` : 마크다운으로 변경
>
> 마크다운에서 `y` : 코드 블럭으로 변경
>
> `ctrl + enter` : 해당 코드 블럭 실행

## 장점
코드 단계 별로 확인 가능

단, 실행 순서 주의 (왼쪽 대괄호)

Kernel 의 restart 기능 활용하여 순서 다시 설정 

> ! 저장 따로 해줘야 함 !


# nb 명령어로 jupyter notebook 실행 (git bash에서)
1. `$ vim ~/.bashrc`
2. `alias nb="jupyter notebook"`
3. `source ~/.bashrc`
4. `nb`