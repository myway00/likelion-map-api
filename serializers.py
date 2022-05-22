from rest_framework import serializers
from snippets.models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES


class SnippetSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    #django form의 widget=widgets.Textarea
    #html 파일을 렌더링 할 때 필드 flag는 
    # 또한 특정 환경에서 serializer가 어떻게 보여지는지 설정할 수 있다.
    # HTML로 rendering할 때 이 코드는
    #  Form에서 widget=widgets.Textarea와 유사
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

#data를 deserializing 할 때 save()를 호출해서 저장 가능
# save 는 instance가 존재하면 update를, 그렇지 않으면 create를 해줍니다!
    def create(self, validated_data):
    #self : 객체의 인스턴스 그 자체  즉, 객체 자기 자신을 참조하는 매개변수
    #validated_data : 지금 이 serializer가 data를 받고, 이에 대한 is_valid()결과가 true라면
    #시리얼라이저는 validated_data 를 반환해요! 
    # (시리얼라이저의 필드를 시리얼라이즈 한 유효 데이터)
        return Snippet.objects.create(**validated_data)

    def update(self, instance, validated_data):
        
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']
