from rest_framework import serializers
from .utils import format_seconds
from .models import (
    BookAuthor, BookCategory,
    Book, UserBookProgress,
    AudioBook, AudioSection,
    AudioUnit, UserAudiobookProgress,
    LibrarySearchHistory
)

class BookListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'cover_image',
            'is_required',
            'pages',
            'author'
        )


class AudiobookListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    duration = serializers.SerializerMethodField()

    class Meta:
        model = AudioBook
        fields = (
            'id',
            'title',
            'cover_image',
            'is_required',
            'author',
            'duration'
        )

    def get_duration(self, obj):
        return obj.duration // 60


class AuthorSerializer(serializers.ModelSerializer):
    books = BookListSerializer(many=True)
    audiobooks = AudiobookListSerializer(many=True)

    class Meta:
        model = BookAuthor
        fields = (
            'id', 
            'full_name', 
            'birth_date', 
            'country',
            'about',
            'avatar',
            'books',
            'audiobooks'
        )


class BookUnreadDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'cover_image',
            'author',
            'category',
            'publication_year',
            'is_required',
            'description',
            'bonus_points',
            'language',
            'deadline',
            'pages'
        )


class BookReadInDetailSerializer(serializers.ModelSerializer):
    book = BookUnreadDetailSerializer()

    class Meta:
        model = UserBookProgress
        fields = (
            'id',
            'book',
            'last_page',
            'percentage'
        )
    

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = (
            'id', 
            'title', 
            'author', 
            'cover_image', 
            'book_file'
        )
        

class BookFileSerializer(serializers.ModelSerializer):
    book = BookSerializer()

    class Meta:
        model = UserBookProgress
        fields = ('id', 'last_page', 'percentage', 'book')


class BookReadProgressSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserBookProgress
        fields = (
            'id',
            'profile',
            'book',
            'last_page'
        )


class AudiobookUnlistenedDetailSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    category = serializers.StringRelatedField()
    duration = serializers.SerializerMethodField()

    class Meta:
        model = AudioBook
        fields = (
            'id',
            'title',
            'cover_image',
            'publication_year',
            'author',
            'category',
            'is_required',
            'description',
            'bonus_points',
            'language',
            'duration'
        )

    def get_duration(self, obj):
        return format_seconds(obj.duration)


class AudiobookListenedDetailSerializer(serializers.ModelSerializer):
    audiobook = AudiobookUnlistenedDetailSerializer()
    duration_so_far = serializers.SerializerMethodField()

    class Meta:
        model = UserAudiobookProgress
        fields = (
            'id',
            'audiobook',
            'duration_so_far',
            'percentage'
        )

    def get_duration_so_far(self, obj):
        return format_seconds(obj.duration_so_far)

        
class AudiobookUnitSerializer(serializers.ModelSerializer):
    duration = serializers.SerializerMethodField()

    class Meta:
        model = AudioUnit
        fields = ('id', 'duration', 'name', 'audio_file')

    def get_duration(self, obj):
        return format_seconds(obj.duration)
    

class AudioSectionSerializer(serializers.ModelSerializer):
    units = AudiobookUnitSerializer(many=True)

    class Meta:
        model = AudioSection
        fields = ('id', 'name', 'name', 'units')


class AudiobookSerializer(serializers.ModelSerializer):
    sections = AudioSectionSerializer(many=True)
    author = serializers.StringRelatedField()
    duration = serializers.SerializerMethodField()

    class Meta:
        model = AudioBook
        fields = ('id', 'title', 'author', 'cover_image', 'duration', 'sections')

    def get_duration(self, obj):
        return format_seconds(obj.duration)
    

class AudiobookFileSerializer(serializers.ModelSerializer):
    audiobook = AudiobookSerializer()

    class Meta:
        model = UserAudiobookProgress
        fields = (
            'id',
            'listened_duration',
            'duration_so_far',
            'audio_unit',
            'audiobook'
        )


class AudiobookListenProgressSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = UserAudiobookProgress
        fields = (
            'id',
            'profile',
            'audiobook',
            'audio_unit',
            'listened_duration'
        )

        
class PopularCategoriesSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()

    class Meta:
        model = BookCategory
        fields = ('id', 'name', 'icon', 'books_count')

    def get_books_count(self, obj):
        return obj.books.count() + obj.audiobooks.count()
    

class CategoryDetailSerializer(serializers.ModelSerializer):
    books_count = serializers.SerializerMethodField()
    books = BookListSerializer(many=True)
    audiobooks = AudiobookListSerializer(many=True)

    class Meta:
        model = BookCategory
        fields = (
            'id', 
            'name', 
            'icon', 
            'books_count',
            'books',
            'audiobooks'
        )

    def get_books_count(self, obj):
        return obj.books.count() + obj.audiobooks.count()
    