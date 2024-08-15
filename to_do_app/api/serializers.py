from rest_framework import serializers
from to_do_list.models import Task
from users.models import User


class TaskSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Task
        fields = ["id", "username", "user_id", "title", "is_completed",  'user']

    def get_username(self, obj):
        return obj.user.username if obj.user else None


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "date_joined", "is_superuser", "first_name", "last_name"]