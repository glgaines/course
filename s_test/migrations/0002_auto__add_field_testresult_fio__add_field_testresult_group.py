# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'TestResult.fio'
        db.add_column('s_test_testresult', 'fio',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)

        # Adding field 'TestResult.group'
        db.add_column('s_test_testresult', 'group',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'TestResult.fio'
        db.delete_column('s_test_testresult', 'fio')

        # Deleting field 'TestResult.group'
        db.delete_column('s_test_testresult', 'group')


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
            'fio': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'group': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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