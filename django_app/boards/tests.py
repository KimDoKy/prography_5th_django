from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Post, Comment
import os

class CreatPostTestCase(TestCase):

    def setUp(self):
        self.author = User.objects.create_user(username='tester')
        self.title = 'test title'
        self.content = 'test content'
        self.path = os.getcwd()
        self.photo = SimpleUploadedFile(name='test.jpg',
                                        content=open(self.path+'/boards/test.jpg', 'rb').read(),
                                        content_type='image/jpg')
        self.comment = 'test comment'

    def test_write_post(self):
        old_count = Post.objects.count()
        post = Post(title=self.title,
                    content=self.content,
                    author=self.author,
                    photo=self.photo)
        post.save()
        new_count = Post.objects.count()
        self.assertNotEqual(old_count, new_count)

    def test_write_comment(self):
        post = Post(title=self.title,
                    content=self.content,
                    author=self.author,
                    photo=self.photo)
        post.save()
        old_count = Comment.objects.count()
        comment = Comment.objects.create(post=post,
                                         author=self.author,
                                         message=self.comment)
        comment.save()
        new_count = Comment.objects.count()
        self.assertNotEqual(old_count, new_count)

    # 테스트 완료후 테스트에 사용된 임시 이미지 파일 모두 제거
    def tearDown(self):
        for files in os.listdir(self.path):
            if files[-3:] == 'jpg':
                os.remove(self.path+'/'+files)

