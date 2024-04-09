from django.shortcuts import render
from .forms import CustomUserCreationForm

# Create your views here.
def signup(request):
    # GET 요청, POST요청 조건 분기
    if request.method == 'POST':
        pass
    else:
        # 사용자가 회원가입을 위한 
        # 데이터를 입력할 form을 렌더링
        # django가 기존에 제공하는 UserCreationForm은 auth.User를 기준으로 만들어졌다.
        # 그래서 Meta class에 있는 model 정보가 auth.User에서 accounts.User로 바꿔야함.
        form = CustomUserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)