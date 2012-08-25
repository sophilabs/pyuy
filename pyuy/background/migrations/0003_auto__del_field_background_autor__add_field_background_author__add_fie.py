# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Background.autor'
        db.delete_column('background_background', 'autor')

        # Adding field 'Background.author'
        db.add_column('background_background', 'author',
                      self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Background.box_css_class'
        db.add_column('background_background', 'box_css_class',
                      self.gf('django.db.models.fields.CharField')(default='std-box', max_length=20),
                      keep_default=False)


        # Changing field 'Background.source'
        db.alter_column('background_background', 'source', self.gf('django.db.models.fields.URLField')(max_length=200, null=True))

    def backwards(self, orm):
        # Adding field 'Background.autor'
        db.add_column('background_background', 'autor',
                      self.gf('django.db.models.fields.CharField')(default='Author', max_length=30),
                      keep_default=False)

        # Deleting field 'Background.author'
        db.delete_column('background_background', 'author')

        # Deleting field 'Background.box_css_class'
        db.delete_column('background_background', 'box_css_class')


        # Changing field 'Background.source'
        db.alter_column('background_background', 'source', self.gf('django.db.models.fields.URLField')(default='', max_length=200))

    models = {
        'background.background': {
            'Meta': {'object_name': 'Background'},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'box_css_class': ('django.db.models.fields.CharField', [], {'default': "'std-box'", 'max_length': '20'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '6'}),
            'order': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'place': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'source': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        }
    }

    complete_apps = ['background']