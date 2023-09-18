from rest_framework import serializers

from apps.tests.models import Test, Question, QuestionContent, Variant


class VariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Variant
        fields = (
            'name',
            'order',
            'is_answer',
        )


class QuestionContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionContent
        fields = (
            'file',
        )


class QuestionSerializer(serializers.ModelSerializer):
    question_content = QuestionContentSerializer(many=True)
    question_variant = VariantSerializer(many=True)

    class Meta:
        model = Question
        fields = (
            'type',
            'name',
            'order',
            'question_content',
            'question_variant'
        )


class TestSerializer(serializers.ModelSerializer):
    test_question = QuestionSerializer(many=True)

    class Meta:
        model = Test
        fields = (
            'title',
            'duration_time',
            'order',
            'is_resubmit',
            'test_question'
        )
