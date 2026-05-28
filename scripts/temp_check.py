# -*- coding: utf-8 -*-
import sys, json, os
sys.stdout.reconfigure(encoding='utf-8')
staging = 'work/movie_rec_bot/9_PACKAGER__STAGING'

# Map skill id -> name
skill_dir = os.path.join(staging, 'Skill')
skill_map = {}
for f in sorted(os.listdir(skill_dir)):
    d = json.load(open(os.path.join(skill_dir, f), encoding='utf-8'))
    skill_map[d['id']] = d['name']

# Show nodes with resolved skill names
node_dir = os.path.join(staging, 'DialogNode')
for f in sorted(os.listdir(node_dir)):
    d = json.load(open(os.path.join(node_dir, f), encoding='utf-8'))
    n = d['name']
    sid = d.get('skill_id', 'NONE')
    sname = skill_map.get(sid, 'UNKNOWN')
    print(f'{n:55s} -> {sname} ({sid})')
