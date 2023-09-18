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


class AuthorWithBooksSerializer(serializers.ModelSerializer):
    books = BookListSerializer(many=True)

    class Meta:
        model = BookAuthor
        fields = (
            'id', 
            'full_name', 
            'birth_date', 
            'country',
            'about',
            'avatar',
            'books'
        )


class AuthorWithAudiobooksSerializer(serializers.ModelSerializer):
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
            'audiobooks'
        )


class BookUnreadDetailSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'cover_image',
            'category',
            'publication_year',
            'is_required',
            'description',
            'bonus_points',
            'language',
            'deadline',
            'pages',
            'author'
        )

    def get_author(self, obj):
        author = obj.author
        books = BookListSerializer(author.books.exclude(pk=obj.id), many=True)
        author = AuthorWithAudiobooksSerializer(author).data
        author["books"] = books.data
        return author


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
    author = serializers.SerializerMethodField()
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
    
    def get_author(self, obj):
        author = obj.author
        audiobooks = AudiobookListSerializer(author.audiobooks.exclude(pk=obj.id), many=True)
        author = AuthorWithBooksSerializer(author).data
        author["audiobooks"] = audiobooks.data
        return author


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
    

class LibraryListSerializer(serializers.ModelSerializer):
    pages = serializers.IntegerField()
    duration = serializers.SerializerMethodField()
    type = serializers.CharField()
    author = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'cover_image',
            'is_required',
            'pages',
            'duration',
            'type'
        )

    def get_duration(self, obj):
        return obj.duration // 60 if obj.duration else None


class ViewedListSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()
    percentage = serializers.IntegerField()
    type = serializers.CharField()

    class Meta:
        model = Book
        fields = (
            'id',
            'title',
            'author',
            'cover_image',
            'is_required',
            'percentage',
            'type'
        )
