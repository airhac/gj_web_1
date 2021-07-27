from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:#Meta 클래스를 하나 작성 해주어야한다. 장고가 이 모델폼을 찾는다.
        #Meta 정보라는 것을 이미지에 있어서 이미지 데이터 말고 이미지 외 이미지관련 정보
        model = Profile
        fields = ['image', 'nickname', 'message']# user의 값을 안들고 오는 이유는 client에서 안받아도 되는 정보
