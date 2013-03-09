# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Demo.description'
        db.alter_column(u'app_demo', 'description', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Demo.title'
        db.alter_column(u'app_demo', 'title', self.gf('django.db.models.fields.CharField')(max_length=255))

    def backwards(self, orm):

        # Changing field 'Demo.description'
        db.alter_column(u'app_demo', 'description', self.gf('django.db.models.fields.CharField')(max_length=144))

        # Changing field 'Demo.title'
        db.alter_column(u'app_demo', 'title', self.gf('django.db.models.fields.CharField')(max_length=15))

    models = {
        u'app.comment': {
            'Meta': {'object_name': 'Comment'},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'demo': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['app.Demo']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'app.demo': {
            'Meta': {'object_name': 'Demo'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'demos'", 'to': u"orm['app.Event']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'presenter': ('django.db.models.fields.CharField', [], {'max_length': '40'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'app.event': {
            'Meta': {'object_name': 'Event'},
            'current_demo': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'presenting_events'", 'null': 'True', 'to': u"orm['app.Demo']"}),
            'datetime': ('django.db.models.fields.DateTimeField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_current': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'venue': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']