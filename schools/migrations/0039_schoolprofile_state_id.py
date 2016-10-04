# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations

def insert_state_ids(apps, schema_editor):
    id_map = {
            189: "320304",
            207: "320306",
            179: "320308",
            200: "320316",
            237: "32C000",
            180: "320374",
            222: "320317",
            208: "320318",
            197: "320319",
            226: "320322",
            211: "320323",
            202: "320313",
            212: "320310",
            209: "320363",
            201: "320315",
            186: "320344",
            213: "320332",
            228: "320347",
            188: "320366",
            206: "320320",
            238: "32M000",
            239: "32B000",
            205: "320324",
            223: "320325",
            187: "320701",
            204: "320328",
            229: "320329",
            184: "320327",
            227: "320336",
            224: "320309",
            192: "320312",
            240: "32D000",
            196: "320341",
            216: "320339",
            221: "320342",
            178: "320340",
            220: "320343",
            177: "320348",
            241: "32A000",
            210: "320352",
            225: "320353",
            214: "320354",
            181: "320355",
            199: "320356",
            195: "320360",
            194: "320362",
            190: "320364",
            234: "32Q000",
            235: "32N000",
            203: "320365",
            183: "320367",
            182: "320370",
            219: "320369",
            185: "320338",
            231: "320368",
            191: "320372",
            217: "320376",
            236: "32K000",
            242: "32P000",
            218: "320314",
            243: "32L000",
            198: "320388",
            215: "320400",
            193: "320346",
        }
    school_profile = apps.get_model("schools", "schoolprofile")
    for school in school_profile.objects.all():
        if school.school_id in id_map:
            school.state_id = id_map[school.school_id]
        else:
            school.state_id = ""
        school.save()

class Migration(migrations.Migration):
    dependencies = [
            ('schools', '0038_schoolprofile_feeder_school_info'),
            ]

    operations = [
            migrations.AddField(
                model_name='schoolprofile',
                name='state_id',
                field=models.CharField(blank=True, null=True, max_length=6),
                ),
            migrations.RunPython(insert_state_ids)
            ]
