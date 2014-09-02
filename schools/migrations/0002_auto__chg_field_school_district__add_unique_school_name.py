# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'School.district'
        db.alter_column(u'schools_school', 'district', self.gf('django.contrib.gis.db.models.fields.PolygonField')(null=True))
        # Adding unique constraint on 'School', fields ['name']
        db.create_unique(u'schools_school', ['name'])


    def backwards(self, orm):
        # Removing unique constraint on 'School', fields ['name']
        db.delete_unique(u'schools_school', ['name'])


        # Changing field 'School.district'
        db.alter_column(u'schools_school', 'district', self.gf('django.contrib.gis.db.models.fields.PolygonField')(default='None'))

    models = {
        u'schools.school': {
            'Meta': {'object_name': 'School'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'choice_zone': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True'}),
            'district': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'magnet': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'priority_zone': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True'}),
            'walk_zone': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True'}),
            'year_round': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['schools']