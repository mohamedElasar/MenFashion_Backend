from django.contrib.auth import get_user_model,authenticate


from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """serializers for the models object"""

    class Meta:
        model = get_user_model()
        fields = ['id','email','username','password']
        read_only_fields = ('id',)

        extra_kwargs = {'password':{'min_length':5}}

    def create(self,validated_data):
        """create new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)



class AuthTokenSerializer(serializers.Serializer):
    """serializers for the user authentication object"""

    # email = serializers.CharField()
    username = serializers.CharField()
    password = serializers.CharField(
    style = {'input_type':'password'},
    trim_whitespace = False
    )

    def validate(self,attrs):
        # email = attrs.get('email')
        password = attrs.get('password')
        username = attrs.get('username')
        user = authenticate(
             request=self.context.get('request'),
             # email = email,
             password = password,
             username = username,

             )

        if not user:
            msg = ('unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg,code = 'authentication')

        attrs['user'] = user
        return attrs
