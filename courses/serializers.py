from rest_framework import serializers

from accounts.models import Courses, Lessons, LessonFile, Modules

from .models import Article, Comment, Notification


class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'image', 'name', 'slug', 'is_active']
        read_only_fields = ['slug']


class CourseRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = ['id', 'image', 'name', 'created_at', 'is_active']


class ModulesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Modules
        fields = ['id', 'file', 'name', 'slug']
        read_only_fields = ['slug']


class ModuleRetrieveSerializer(serializers.ModelSerializer):
    lessons = serializers.SerializerMethodField()

    class Meta:
        model = Modules
        fields = ['id', 'file', 'name', 'description', 'created_at', 'updated_at', 'course', 'lessons']

    def get_lessons(self, obj):
        lessons = obj.lessons.all()
        return LessonsListSerializer(lessons, many=True).data


class LessonsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lessons
        fields = ['id', 'title', 'slug', 'module']


class LessonRetrieveSerializer(serializers.ModelSerializer):
    module_name = serializers.CharField(source='module.name', read_only=True)

    class Meta:
        model = Lessons
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'module', 'module_name']


class LessonFilesSerializer(serializers.ModelSerializer):
    lesson_title = serializers.CharField(source='lesson.title', read_only=True)

    class Meta:
        model = LessonFile
        fields = ['id', 'lesson', 'lesson_title', 'file']


class ArticleSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username')
    class Meta:
        model = Article
        fields = ['id', 'author', 'author_name','title', 'content', 'image', 'created_at', 'updated_at']


class CommentSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username')
    article_name = serializers.CharField(source='article.title')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'author_name', 'article_name', 'article', 'content']
        read_only_fields = ['author', 'author_name', 'article_name']


class NotificationListSerializer(serializers.ModelSerializer):
    to_name = serializers.CharField(source='to.username')
    class Meta:
        model = Notification
        fields = ['id', 'to', 'to_name', 'content']


class NotificationRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'to', 'banner', 'content', 'is_read', 'sent_at']
    


    
