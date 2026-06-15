from rest_framework import serializers

from projects.models import Task


class TaskDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class TaskUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = (
            'name',
            'description',
            'status',
            'priority',
            'project',
            'created_at',
            'due_date',
            'tags',
            'assignee',
            'created_by',
        )
