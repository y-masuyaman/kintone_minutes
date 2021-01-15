from django.db import models


class Minutes(models.Model):

    # 対応日時　date型
    meeting_date = models.DateField(verbose_name="対応日時")

    # 対応内容　choice型
    MEETING_PURPOSE_CHOICES = (
        ('商談', '商談'),
        ('電話', '電話'),
        ('その他', 'その他'),
    )
    meeting_purpose = models.CharField(verbose_name="対応内容", max_length=10, choices=MEETING_PURPOSE_CHOICES)

    # 検討ランク　choice型
    MEETING_RANK_CHOICES = (
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    )
    meeting_rank = models.CharField(verbose_name="検討ランク", max_length=10, choices=MEETING_RANK_CHOICES)

    # 商談メモ text とりあえず5000上限
    meeting_contents = models.TextField(verbose_name='商談メモ', max_length="5000")

    # アクションアイテム text とりあえず5000上限
    meeting_next_action = models.TextField(verbose_name='次のアクション', max_length="5000")

    # 作成日時と更新日時
    created_at = models.DateTimeField('作成日時', auto_now_add=True)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.meeting_contents
