from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        # fields = ('title', 'content',)
        exclude = ('user',)

'''
    form의 역할을 잘 생각하면 당연한 이야기다.
    form의 역할은 사용자가 입력할 data를 작성할 공간 input을 마련하는것.
    근데, 사용자가 작성 안해도 되거나 작성하면 안되는 내용들은
    field에서 생략해서 제공하는게 맞다.

    로그인 한 유저가, 자기가 누군지 직접 다시 선택해서 요청해야하면 불편하다.
    그리고, 다른 유저 명을 선택하면 조작이 가능하다.
    그럼 당연히, 게시글, 댓글 작성시 어느 유저가 작성하는지를 사용자가 선택하는건
    이상하다.
'''
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)
