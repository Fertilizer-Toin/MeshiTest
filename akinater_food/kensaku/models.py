from django.db import models
# Create your models here.
class choices(models.Model):
    foods_id = models.IntegerField(primary_key=True)
    food_name = models.CharField('食材の名前',max_length=40)
    taste = models.IntegerField('味')
    group = models.CharField('ジャンル',max_length=25)
    texture = models.CharField('食感',max_length=255)
    Allergy = models.CharField('アレルギー物質',max_length=50)
    temperature = models.IntegerField('温度')
    Halal = models.BooleanField('ハラル') #ハラルだったらTrue,ハラルじゃなかったらfalse
    volume = models.IntegerField('腹持ちの良さ')
    Prefecture = models.IntegerField('何県のあれか',default=0)
    calorie = models.IntegerField('カロリー')
    meat = models.BooleanField('肉入りかどうか')
    fish = models.BooleanField('魚入りかどうか')
    season = models.IntegerField('旬')
    major_or_minor  = models.BooleanField('有名かどうか')
    difficulty  = models.IntegerField('難度')
    rice_or_bread = models.IntegerField('パンかご飯かそれいがいか',default=0)
    def __str__(self):
        return self.food_name
