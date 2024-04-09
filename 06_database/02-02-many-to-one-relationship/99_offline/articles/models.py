from django.db import models
from django.conf import settings
# django에서는 User 모델을 '직접' 참조하지 않는다.
# from accounts.models import User


# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    '''
        Comment 입장에서는 본인이 참조할 Article class가 상단부에 정의가 되어 
        있기 떄문에, 정의된 Article class 자체를 첫번째 변수에 인자로 넘겨주면 된다.

        그런데, 만약 더 복잡한 형태의 관계를 형성해야 한다면,
        class의 선언 위치와 관계 없이도, 충분히 관계를 맺을 수 있어야 될 것 같다.
        예를들어서

        class Article
        class Comment
        class Reservation
        class Recommend

        이런식으로 다수의 클래스 들이 있는데,
        Article과 Recomment가 1:N
        Recomment와 Reservation이 1:N
        Resvation과 Comment가 1:N
        위와 같이 복잡한 관계로 형성되어 있으면
        class의 선언 순서를 신경써서 정의를 하는 것이 아니라...
        'app_name.model_name' 형태의 문자열로도, FK(to=value) 삳용할 수 있다.
    '''
    # article = models.ForeignKey('articles.Article', on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    '''
        User 모델은 특별해서 settings.AUTH_USER_MODEL로 작성하는 것이 아니다.
        다른 app에 있는 모델 User에 대한 정보를 'accounts.User' 형식으로 작성한다.
        근데, User 모델의 위치 (활성화 할 User)는 이미 settings.py에서 적었었다.
        그리고, 만약 활성화 할 User 모델이 변경된다 하더라도, 
        settings.AUTH_USER_MODEL을 수정하면, User와 관계 맺고 있는 모든 Model들에
        동시에 적용될 수 있기 때문에 우리는 그 변수에 담긴 값을 할당한다.
    '''
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
