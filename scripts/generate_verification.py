import pathlib,re,json,collections,sys
root=pathlib.Path(__file__).resolve().parents[1];sys.path.insert(0,str(root/'scripts'))
from update_authored_data import plain
mappings=json.loads((root/'scripts/authored-table-mappings.json').read_text())['units']
paths=root/'docs/upgrade'; records={p.stem:json.loads(p.read_text()) for p in (root/'docs/.vitepress/theme/assets/unit-data').glob('*.json')}
# Pending state and its reason live alongside each value. Regenerating the
# checklist therefore drops fields as soon as a reviewed value replaces them.
OUTDATED='暂列更新前数值'
m=[]
for unit, record in records.items():
 for table in record.get('tables', []):
  for row in table.get('rows', []):
   for field, cell in zip(table.get('headers', []), row):
    if cell.get('verification') not in ('pending', 'outdated'): continue
    reason=cell.get('verificationReason') if cell['verification'] == 'pending' else OUTDATED
    if not reason: raise ValueError(f'Missing pending reason: {unit} {table["sourceTableIndex"]} {row[0]["value"]} {field}')
    m.append({'unit': unit, 'table': table['sourceTableIndex'], 'level': row[0]['value'], 'field': field, 'reason': reason})
labels=collections.defaultdict(set)
for unit,plans in mappings.items():
 for plan in plans:
  if plan.get('keepOriginal'):continue
  for src in [plan,*plan.get('additionalSourceTables',[])]:
   headers=src['sourceHeaders'];t=src['sourceTableIndex']
   for output,spec in src['columns'].items():
    target=re.sub(r'[①-⑳#*]', '', plain(plan['headers'][int(output)]))
    if any(x in target for x in ('经验','日均','回本')):continue
    cols=[]
    if isinstance(spec,int):cols=[spec]
    elif isinstance(spec,dict):
     if 'sum' in spec:cols=spec['sum']
     for k in ('multiply','duration','percentOffset'):
      if k in spec:cols.append(spec[k])
     if 'join' in spec:cols+=spec['join']
     if 'requirement' in spec:cols.append(headers.index(spec['requirement']))
    for c in cols:
     if c is not None and c<len(headers):labels[(unit,t,headers[c])].add(target)
manual={'Build Cost':'升级费用','Build Time':'升级时间'}
for field,zh in manual.items():labels[('0487-Pet-House',3,field)].add(zh)
# The level-13 Hero Hall's empty unlocked hero and 4 slots are player-provided.
groups=collections.defaultdict(lambda:collections.defaultdict(set))
for item in m:
 unit=item['unit'];field=item['field'];t=item['table'];ls=labels.get((unit,t,field),set())
 if not ls:continue
 table=next((t for t in records[unit]['tables'] if t['sourceTableIndex']==item['table']),None)
 row=next((r for r in table['rows'] if r[0]['value']==item['level']),None) if table else None
 cell=row[table['headers'].index(field)] if row and field in table['headers'] else {}
 if 'confirmedTownHall' in cell: ls={x for x in ls if '所需大本等级' not in x}
 if not ls:continue
 level=item['level'];prefix='⚡' if any(p.get('levelPrefix')=='⚡' and p['sourceTableIndex']==t for plan in mappings.get(unit,[]) for p in plan.get('additionalSourceTables',[])) else ''
 if prefix:level=prefix+str(level)
 groups[item['reason']][(unit,str(level))].update(ls)
# Group levels when all displayed fields are the same.
def format_levels(levels):
 nums=sorted({int(x) for x in levels if str(x).isdigit()}); other=sorted({str(x) for x in levels if not str(x).isdigit()}); out=[]
 for n in nums:
  if out and isinstance(out[-1],list) and n==out[-1][-1]+1:out[-1].append(n)
  else:out.append([n])
 out=[str(g[0]) if len(g)==1 else f'{g[0]}–{g[-1]}' for g in out]
 return '、'.join(out+other)
def rows(reason):
 reverse=collections.defaultdict(list)
 for (u,level),fields in groups[reason].items():reverse[(u,tuple(sorted(fields)))].append(level)
 result=[]
 for (u,fields),levels in sorted(reverse.items(),key=lambda x:(x[0][0],str(x[1][0]))):
  s=(paths/(u+'.md')).read_text(); title=re.search(r'^navTitle:\s*"?([^"\n]+)',s,re.M); title=title[1] if title else records[u]['title']
  result.append(f'| [{title}](/upgrade/{u}) | {format_levels(levels)} | {"、".join(fields)} |')
 return result
sections=[('新增等级','新增等级尚待官方、Wiki 或玩家核实'),('旧等级费用与时间','旧等级调整尚待官方、Wiki 或玩家核实'),('新增属性与 2026 年 10 月调整','新增字段尚待官方、Wiki 或玩家核实'),('2026 年 10 月调整','2026 年 10 月调整尚待官方、Wiki 或玩家核实'),('可能需要更新（暂列更新前数值，页面以 * 标出）',OUTDATED)]
lines = [
    '---',
    'title: "待更新数据核对清单"',
    'module: verification',
    'canonical: /verification',
    'robots: noindex, nofollow',
    'hasUpdateTime: false',
    '---',
    '',
    '以下是官方公告、Wiki 和 ClashKing 游戏数据目前都还没有提供的字段，以及暂列旧数值、可能需要更新的字段。已收到玩家核实的结果会在对应页面注明“玩家提供”。',
    '',
    '## 已查过、仍需核实的重点',
    '',
]

def pending(unit, level=None, field=None):
 return any(item['reason'] != OUTDATED and item['unit'] == unit and (level is None or item['level'] == level)
            and (field is None or item['field'] == field) for item in m)

def pending_page_row(unit, level):
 page = (paths/(unit+'.md')).read_text()
 return re.search(rf'^\|\s*{level}\s*\|[^\n]*待更新', page, re.M) is not None

def pending_property(unit, name):
 page = (paths/(unit+'.md')).read_text()
 return f'pKey="{name}" pValue="待更新"' in page

if pending_page_row('0407-Clan-Castle', 19):
 lines.append('- [19 本宝库容量](/upgrade/0407-Clan-Castle)：金币、圣水、黑水的基础容量；不同部落等级的容量可以据加成换算。11 月 17 日复查的 Wiki 表仍只列到 18 本。')
for unit, level, name, checked in [
 ('0404-Gold-Storage', 20, '储金罐', '11 月 17 日'),
 ('0405-Elixir-Storage', 20, '圣水瓶', '11 月 16 日'),
 ('0406-Dark-Elixir-Storage', 14, '暗黑重油罐', '11 月 16 日'),
]:
 if pending(unit, level):
  lines.append(f'- [{level} 级{name}](/upgrade/{unit})：新增等级的容量及其他尚未更新的属性。{checked}查看时，Wiki 升级表尚未列出新增等级。')
if pending_page_row('0385-Skeleton-Trap', 6):
 lines.append('- [6 级骷髅陷阱](/upgrade/0385-Skeleton-Trap)：召唤骷髅的数量和等级，以及页面标为待更新的其他字段。11 月 17 日复查的 Wiki 表仍只列到 5 级。')
heroes = [(unit, name) for unit, name in [
 ('0202-Grand-Warden', '大守护者'), ('0203-Royal-Champion', '飞盾战神'),
 ('0204-Minion-Prince', '亡灵王子'), ('0205-Dragon-Duke', '飞龙公爵'),
] if pending(unit)]
if heroes:
 links = '、'.join(f'[{name}](/upgrade/{unit})' for unit, name in heroes)
 lines.append(f'- {links}：部分等级的升级费用、时间和属性。11 月 17 日查看时，Wiki 升级表仍是此次更新前的数据。')
for unit, level, name in [('0082-Valkyrie', 13, '瓦基丽武神'), ('0080-Minion', 15, '亡灵'), ('0013-Ruin-Witch', 5, '废墟女巫')]:
 if pending(unit, level):
  lines.append(f'- [{level} 级{name}](/upgrade/{unit})：新增等级的升级费用、时间和属性。11 月 17 日查看时，Wiki 升级表尚未列出新增等级。')
if pending('0004-Wall-Breaker', 15, 'Damage when destroyed vs. Walls'):
 lines.append('- [15 级炸弹人](/upgrade/0004-Wall-Breaker)：死亡后对城墙造成的伤害。11 月 17 日 Wiki 升级表将该项列为问号。')
if pending('0314-Multi-Archer-Tower', 5, 'Hitpoints'):
 lines.append('- [5 级多人箭塔](/upgrade/0314-Multi-Archer-Tower)：生命值。11 月 17 日 Wiki 表写 5,400，此前候选记录为 5,900，两者有差异，需以游戏内为准。')
siege_levels = [(unit, level, name) for unit, level, name in [
 ('0240-Wall-Wrecker', 6, '攻城战车 6 级'), ('0241-Battle-Blimp', 6, '攻城飞艇 6 级'),
 ('0242-Stone-Slammer', 6, '攻城气球 6 级'), ('0243-Siege-Barracks', 5, '攻城训练营 5 级'),
 ('0243-Siege-Barracks', 6, '攻城训练营 6 级'), ('0244-Log-Launcher', 5, '攻城滚木车 5 级'),
 ('0244-Log-Launcher', 6, '攻城滚木车 6 级'), ('0245-Flame-Flinger', 5, '攻城烈焰车 5 级'),
 ('0246-Battle-Drill', 6, '攻城钻机 6 级'),
] if pending(unit, level)]
if siege_levels:
 links = '、'.join(f'[{name}](/upgrade/{unit})' for unit, level, name in siege_levels)
 lines.append(f'- {links}：升级费用和时间。11 月 17 日查看时，Wiki 升级表仍显示此次调整前的数值。')

properties = [(unit, name, field) for unit, name, field in [
 ('0180-Poison-Spell', '毒药法术', '作用半径'),
 ('0204-Minion-Prince', '亡灵王子', '攻击距离'),
 ('0205-Dragon-Duke', '飞龙公爵', '攻击距离'),
 ('0289-Angry-Jelly', '愤怒水母', '攻击距离'),
 ('0014-Ruin-Knight', '废墟骑士', '移动速度'),
] if pending_property(unit, field)]
if properties:
 lines += ['', '## 其他待核对的单位属性', '']
 lines += [f'- [{name}](/upgrade/{unit})：{field}。' for unit, name, field in properties]
# Values written directly on a page (tables without a data mapping, unit
# properties) are not in the per-unit data files; scan pages so they are listed too.
from update_authored_data import parse_tables
listed = {(unit, field) for unit, _, field in properties}
page_items = []
for page in sorted(paths.glob('*.md')):
 unit, text = page.stem, page.read_text()
 if '待更新' not in text:
  continue
 title = re.search(r'^navTitle:\s*"?([^"\n]+)', text, re.M)
 title = title[1] if title else unit
 plans = mappings.get(unit, [])
 for index, table in enumerate(parse_tables(text)):
  if index < len(plans) and not plans[index].get('keepOriginal'):
   continue
  heading = re.findall(r'imgAlt="([^"]+)"', text[:table['start']])
  heading = heading[-1] if heading else title
  levels = [plain(r[0]) for r in table['rows'] if any('待更新' in c for c in r)]
  fields = sorted({plain(table['headers'][i]) for r in table['rows'] for i, c in enumerate(r) if '待更新' in c})
  if levels:
   page_items.append(f'| [{title}](/upgrade/{unit}) | {heading}：{"、".join(levels)} 级 | {"、".join(fields)} |')
 for name in re.findall(r'pKey="([^"]+)" pValue="待更新', text):
  if (unit, name) not in listed:
   page_items.append(f'| [{title}](/upgrade/{unit}) | — | {name} |')
if page_items:
 lines += ['', '## 页面内直接列出的数据', '', '这些数值写在页面表格或属性栏中，不在单位数据文件里。', '', '| 单位 | 位置 | 待核对字段 |', '| --- | --- | --- |', *page_items]
lines += ['', '下面清单按单位和等级列出当前暂未展示的字段。带 ⚡ 的行是已经移除的超级充能历史，不能再从当前游戏界面核实；经验、日均消耗等可计算值不需要单独核实。']
count=0
for heading,reason in sections:
 items=rows(reason); count+=len(items)
 if not items:continue
 lines+=['',f'## {heading}','','| 单位 | 等级 | 待核对字段 |','| --- | --- | --- |',*items]
result = '\n'.join(lines) + '\n'
destination = root/'docs/verification.md'
if '--check' in sys.argv:
 if destination.read_text() != result:
  raise SystemExit('待更新清单与数据不一致；请运行 python3 scripts/generate_verification.py')
else:
 destination.write_text(result)
print('rows',count,'units',len({u for reason in groups.values() for u,_ in reason}),'manifest',len(m))
