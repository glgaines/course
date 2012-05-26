# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Test'
        db.create_table('s_test_test', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('comments', self.gf('tinymce.models.HTMLField')(default='', blank=True)),
            ('test_result', self.gf('tinymce.models.HTMLField')(default='', blank=True)),
        ))
        db.send_create_signal('s_test', ['Test'])

        # Adding model 'TestQuestion'
        db.create_table('s_test_testquestion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(related_name='questions', to=orm['s_test.Test'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('comment', self.gf('tinymce.models.HTMLField')(default='', blank=True)),
            ('position', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_multiple', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('s_test', ['TestQuestion'])

        # Adding model 'TestAnswer'
        db.create_table('s_test_testanswer', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.related.ForeignKey')(related_name='answers', to=orm['s_test.TestQuestion'])),
            ('content', self.gf('tinymce.models.HTMLField')()),
            ('weight', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('s_test', ['TestAnswer'])

        # Adding model 'TestScale'
        db.create_table('s_test_testscale', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(related_name='scales', to=orm['s_test.Test'])),
            ('start', self.gf('django.db.models.fields.IntegerField')()),
            ('end', self.gf('django.db.models.fields.IntegerField')()),
            ('comment', self.gf('tinymce.models.HTMLField')()),
        ))
        db.send_create_signal('s_test', ['TestScale'])

        # Adding model 'TestResult'
        db.create_table('s_test_testresult', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('test', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['s_test.Test'])),
            ('result', self.gf('tinymce.models.HTMLField')()),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('email', self.gf('django.db.models.fields.EmailField')(default='', max_length=75, blank=True)),
        ))
        db.send_create_signal('s_test', ['TestResult'])


    def backwards(self, orm):
        # Deleting model 'Test'
        db.delete_table('s_test_test')

        # Deleting model 'TestQuestion'
        db.delete_table('s_test_testquestion')

        # Deleting model 'TestAnswer'
        db.delete_table('s_test_testanswer')

        # Deleting model 'TestScale'
        db.delete_table('s_test_testscale')

        # Deleting model 'TestResult'
        db.delete_table('s_test_testresult')


    models = {
        's_test.test': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Test'},
            'comments': ('tinymce.models.HTMLField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'test_result': ('tinymce.models.HTMLField', [], {'default': "''", 'blank': 'True'})
        },
        's_test.testanswer': {
            'Meta': {'ordering': "('weight',)", 'object_name': 'TestAnswer'},
            'content': ('tinymce.models.HTMLField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'answers'", 'to': "orm['s_test.TestQuestion']"}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        's_test.testquestion': {
            'Meta': {'ordering': "('position',)", 'object_name': 'TestQuestion'},
            'comment': ('tinymce.models.HTMLField', [], {'default': "''", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_multiple': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'position': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'questions'", 'to': "orm['s_test.Test']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        's_test.testresult': {
            'Meta': {'object_name': 'TestResult'},
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "''", 'max_length': '75', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'result': ('tinymce.models.HTMLField', [], {}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['s_test.Test']"})
        },
        's_test.testscale': {
            'Meta': {'object_name': 'TestScale'},
            'comment': ('tinymce.models.HTMLField', [], {}),
            'end': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'start': ('django.db.models.fields.IntegerField', [], {}),
            'test': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'scales'", 'to': "orm['s_test.Test']"})
        }
    }

    complete_apps = ['s_test']