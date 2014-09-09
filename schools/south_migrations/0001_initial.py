# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'School'
        db.create_table('schools_school', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('level', self.gf('django.db.models.fields.IntegerField')(default=4)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('zip_code', self.gf('django.db.models.fields.CharField')(max_length=5)),
            ('magnet', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('year_round', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('location', self.gf('django.contrib.gis.db.models.fields.PointField')()),
            ('district', self.gf('django.contrib.gis.db.models.fields.PolygonField')()),
            ('walk_zone', self.gf('django.contrib.gis.db.models.fields.PolygonField')(null=True)),
            ('choice_zone', self.gf('django.contrib.gis.db.models.fields.PolygonField')(null=True)),
            ('priority_zone', self.gf('django.contrib.gis.db.models.fields.PolygonField')(null=True)),
        ))
        db.send_create_signal('schools', ['School'])


    def backwards(self, orm):
        # Deleting model 'School'
        db.delete_table('schools_school')


    models = {
        'schools.school': {
            'Meta': {'object_name': 'School'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'choice_zone': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True'}),
            'district': ('django.contrib.gis.db.models.fields.PolygonField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'level': ('django.db.models.fields.IntegerField', [], {'default': '4'}),
            'location': ('django.contrib.gis.db.models.fields.PointField', [], {}),
            'magnet': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'priority_zone': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True'}),
            'walk_zone': ('django.contrib.gis.db.models.fields.PolygonField', [], {'null': 'True'}),
            'year_round': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'zip_code': ('django.db.models.fields.CharField', [], {'max_length': '5'})
        }
    }

    complete_apps = ['schools']