from pathlib import Path
import re,json
from html import escape
ROOT=Path(__file__).resolve().parent
OUT=ROOT/'api-md'
HTML=ROOT/'api-reference.html'

def G(label,prefix,*children): return {'t':'g','l':label,'p':prefix,'c':list(children)}
def L(label,rel,*aliases): return {'t':'l','l':label,'r':rel,'a':[label,*aliases]}

NAV=[
 G('产品介绍','guide',
  L('产品概述','intro.md'),
  G('场景方案','scenes',L('单聊/私信','private.md'),L('多人群聊','group.md'),L('系统通知','sys_notice.md'),L('直播聊天室','chatroom.md')),
  G('服务部署','deploy',L('历史版本','releasenodes.md'),L('一键部署','quickdeploy.md'),L('手动部署','manualdeploy.md')),
 ),
 G('客户端集成','client',
  L('SDK 引入','import.md'),
  G('快速开始','quickstart',
   L('Android','android.md'),L('iOS','ios.md'),
   G('JavaScript','web',L('使用 Vue 集成','quickstart.md'),L('通过 Script 引入集成','quickstart_normal.md'),L('发送文件','send_file.md'),L('Electorn 集成','electron.md')),
   L('鸿蒙Harmony','harmony.md'),
  ),
  G('SDK 文档','sdkintro',
   L('会话结构','conversation.mdx'),
   G('消息结构','msg',L('消息对象','message.mdx'),L('文本消息','text.mdx'),L('合并消息','merge.mdx'),L('语音消息','voice.mdx'),L('图片消息','image.mdx'),L('文件消息','file.mdx'),L('视频消息','video.mdx')),
   L('初始化','init.mdx'),
   G('监听相关','watcher',L('连接监听','connect.mdx'),L('会话监听','conversation.mdx'),L('消息监听','message.mdx')),
   L('连接方法','connect.mdx'),
   G('会话相关','conversation',L('获取会话列表','get_all.md'),L('获取单个会话','get_one.md')),
   G('会话草稿','conversation/draft',L('获取会话草稿','draft_get.md'),L('删除会话草稿','draft_remove.md'),L('设置会话草稿','draft_set.md')),
   G('会话操作','conversation/operator',L('插入指定会话','insert.md'),L('标记会话状态','mark_unread.md'),L('删除指定会话','remove.md'),L('获取置顶会话','get_top_all.md'),L('设置会话置顶','settop.md'),L('获取全局免打扰','get_disturb_all.md'),L('设置全局免打扰','set_disturb_all.md'),L('设置单个会话免打扰','disturb.md')),
   G('会话标签','conversation/tag',L('创建标签','add.md'),L('销毁标签','destroy.md'),L('标签事件监听','event.md'),L('获取标签列表','get.md'),L('向标签里添加会话','add_convers.md'),L('从标签里删除会话','remove_convers.md'),L('获取标签会话列表','get_convers.md')),
   G('未读数','conversation/unread',L('获取会话未读总数','get_total_unread.md'),L('清空会话未读总数','clear_total_unread.md'),L('清空单个会话未读数','clear_unread.md')),
   G('消息相关','message',
    G('消息发送','msg_send',L('发送消息','send.md'),L('发送文件','send_file.md'),L('发送图片','send_image.md'),L('发送视频','send_video.md'),L('发送语音','send_voice.md'),L('群发助手','send_mass.md'),L('合并转发','send_merge.md'),L('发送自定义消息','custom.md')),
    G('历史消息','histories',L('获取历史消息','get_all.md'),L('获取 @ 消息','get_mentions.md'),L('清空历史消息','clear.md'),L('删除历史消息','remove.md'),L('获取消息上下文','get_context.md'),L('通过 Id 获取历史消息','get_by_ids.md')),
    G('消息操作','operator',L('修改消息','update.md'),L('设置已读','read.md'),L('撤回消息','recall.md'),L('本地消息搜索','his_lc_search.md'),L('修改本地消息扩展','update_lc_attr.md')),
    G('消息回应','reaction',L('回应事件监听','event.md'),L('添加消息回应','add.md'),L('删除消息回应','remove.md')),
    G('消息置顶','settop',L('置顶监听','event.md'),L('设置置顶','set.md'),L('查询置顶','query.md')),
    G('消息收藏','favorite',L('添加收藏','add.md'),L('移除收藏','remove.md'),L('查询收藏','query.md')),
    L('消息订阅','msg_subscribe.md'),
   ),
   G('聊天室相关','chatroom',L('聊天室监听','event.md'),L('加入聊天室','join.md'),L('加入并创建聊天室','joincreate.md'),L('退出聊天室','quit.md'),L('设置属性','set_kvs.md'),L('删除属性','remove_kvs.md'),L('获取全部属性','get_all_kvs.md'),L('获取指定属性','get_kvs.md'),L('发送聊天室消息','send.md')),
   G('枚举相关','enum',L('Android','android.mdx'),L('iOS','ios.mdx'),L('Web','web.md')),
   G('状态码','status_code',L('Android','android.mdx'),L('iOS','ios.mdx'),L('Web','web.mdx')),
   G('音视频通话','call',L('初始化','init.md'),L('通话实体','callsession.md'),L('来电监听','receivecall.md'),L('发起通话','makecall.md'),L('事件监听','watcher.md'),L('通话结束消息','finishmessage.md')),
   L('日志相关','log.mdx'),
  ),
  G('推送集成','push',L('Android 集成','android.md'),L('iOS 普通推送','ios.md'),L('iOS VoIP 推送','ios_voip.md')),
  G('用户信息','busserver',
   L('接口说明','api.md'),
   G('注册登录','login',L('账号注册','register.md'),L('短信验证码','smssend.md'),L('短验登录','smslogin.md'),L('邮箱验证码','emailsend.md'),L('邮箱登录','emaillogin.md'),L('登录二维码','getloginqr.md'),L('检查扫码状态','checkqr.md'),L('扫码确认','confirmqr.md')),
   G('用户相关','users',L('获取用户信息','qryuserinfo.md'),L('更新用户信息','upduserinfo.md'),L('更新用户设置','updusersettings.md'),L('搜索用户','search.md')),
   G('用户黑名单','users/blockusers',L('添加用户黑名单','addblockusers.md'),L('移除用户黑名单','delblockusers.md'),L('查询黑名单用户列表','qryblockusers.md')),
   G('好友相关','friends',L('申请添加好友','applyfriend.md'),L('处理好友申请','confirmfriend.md'),L('好友申请列表','friendapplications.md'),L('移除好友','delfriend.md'),L('好友列表','friendlist.md'),L('好友搜索','friendsearch.md')),
   G('群组相关','groups',
    G('群组管理','groupmanage',L('创建群组','creategroup.md'),L('更新群组信息','updategroup.md'),L('解散群组','dissolvegroup.md'),L('查询群信息','qrygroupinfo.md'),L('查询加入的群列表','qrymygroups.md'),L('搜索加入的群','searchmygroups.md')),
    G('群组设置','groupsetting',L('变更群主','chgowner.md'),L('设置群禁言','grpmute.md'),L('设置入群验证类型','setgrpverifytype.md'),L('新人入群是否可查看历史消息','sethismsgvisible.md'),L('设置群公告','setgrpannouncement.md'),L('查询群公告','getgrpannouncement.md'),L('设置群昵称','setgrpdisplayname.md'),L('设置群成员禁言','setgrpmembersmute.md')),
    G('成员管理','membermanage',L('邀请入群','invitemember.md'),L('退出群组','quitgroup.md'),L('移除群成员','delmember.md'),L('查询群成员列表','qrygroupmembers.md'),L('申请入群','memberapply.md'),L('搜索群成员','membersearch.md'),L('检查是否群成员','membercheck.md')),
    G('群管理员','groupadmins',L('添加管理员','addadmin.md'),L('移除管理员','deladmin.md'),L('查询群管理员列表','qrygroupmembers.md')),
   ),
   G('Bot相关','bots',L('Bot列表','botlist.md')),
   G('AI助理相关','assistants',L('新增提示词','promptadd.md'),L('更新提示词','promptupdate.md'),L('删除提示词','promptdel.md'),L('批量删除提示词','promptbatchdel.md'),L('查询提示词','promptlist.md'),L('智能回复','aianswer.md')),
   G('Telegram Bot相关','telebots',L('Bot列表','botlist.md'),L('添加Bot','botadd.md'),L('移除Bot','botdel.md')),
   G('朋友圈相关','posts',L('发布帖子','postadd.md'),L('帖子列表','postlist.md'),L('发布评论','postcommentadd.md'),L('评论列表','postcommentlist.md')),
   G('翻译相关','translates',L('翻译','translate.md')),G('文件相关','files',L('上传token','filetoken.md')),G('信息反馈','feedbacks',L('上报反馈','addfeedback.md')),G('工作台','applications',L('应用列表','applist.md')),
   G('消息操作','msgopt',L('管理员撤回消息','recallmsg.md'),L('管理员删除消息','delmsgs.md')),L('状态码','status.md'),
  ),
 ),
 G('服务端集成','server',
  L('接口说明','api.md'),
  G('用户相关','user',G('禁发私聊消息','globalmute',L('添加禁发单聊消息用户','addgrpglobalmute.md'),L('删除禁发单聊消息用户','delpriglobalmute.md'),L('查询禁发单聊消息用户','qrypriglobalmute.md')),L('注册用户','register.md'),L('封禁用户','addbanuser.md'),L('解禁用户','unbanuser.md'),L('查询封禁列表','qrybanusers.md'),L('查询在线状态','useronlinestatus.md'),L('设置单聊禁言','addblockuser.md'),L('解除单聊禁言','unblockuser.md'),L('单聊禁言列表','qryblockusers.md'),L('更新用户信息','updateuser.md'),L('查询用户信息','qryuserinfo.md'),L('踢用户下线','kickuser.md')),
  G('消息相关','message',L('发送单聊消息','privatemsg.md'),G('流式消息','streammsg',L('创建流式消息','sendstreammsg.md','发送流式消息')),L('发送群聊消息','groupmsg.md'),L('发送系统消息','sysmsg.md'),L('发送群发消息','groupcastmsg.md'),L('发送广播消息','broadcastmsg.md'),L('发送聊天室消息','chatroommsg.md'),L('发送聊天室广播消息','chatroombrdmsg.md'),L('标记消息已读','markread.md')),
  G('群组相关','group',L('创建群组','groupcreate.md'),L('解散群组','groupdissolve.md'),L('更新群信息','updategroup.md'),L('查询群信息','qrygroupinfo.md'),L('设置群禁言','groupmute.md'),L('更新群设置','groupsetting.md'),L('添加群成员','groupaddmember.md'),L('移除群成员','groupdelmember.md'),L('查询群成员','qrygroupmember.md'),L('设置群成员禁言','groupmembermute.md'),L('设置群成员白名单','groupmemberallow.md'),L('按成员 ID 查询信息','qrygroupmemberbyids.md'),L('设置群成员属性','groupmemberatt.md')),
  G('会话相关','convers',L('设置免打扰','undisturbconvers.md'),L('删除会话','delconvers.md'),L('添加会话','addconver.md'),L('查询全局会话列表','qryconvers.md'),L('清理未读数','clearunread.md'),L('设置置顶状态','topconvers.md')),
  G('历史消息','hismsg',L('删除消息','delhismsgs.md'),L('消息撤回','recallmsg.md'),L('清空历史消息','cleanhismsgs.md'),L('查询历史消息','qryhismsgs.md'),L('消息修改','modifyhismsgs.md'),L('导入历史消息','importhismsg.md')),
  G('消息订阅','subscription',L('上下线订阅','onlineofflinesub.md'),L('聊天消息订阅','msgsub.md')),L('消息回调','msgcallback/msgcallback.md'),
  G('敏感词相关','sensitivewords',L('添加敏感词','addsensitivewords.md'),L('删除敏感词','delsensitivewords.md'),L('查询敏感词','qrysensitivewords.md')),
  G('标签推送','push',L('添加用户标签','addusertags.md'),L('删除用户标签','delusertags.md'),L('清空用户标签','clearusertags.md'),L('清除用户标签','qryusertags.md'),L('全员/标签推送','pushwithtags.md')),
  G('聊天室相关','chatroom',L('创建聊天室','createchatroom.md'),L('销毁聊天室','destroychatroom.md'),L('查询聊天室信息','qrychrminfo.md')),
  G('聊天室属性','chatroom/chrmatt',L('设置聊天室属性','addchrmatt.md'),L('删除聊天室属性','delchrmatt.md'),L('查询聊天室指定属性','qrychrmatt.md'),L('查询聊天室全量属性','listchrmatt.md')),
  G('聊天室禁言','chatroom/chrmmute',L('设置聊天室全局禁言','chrmglobalmute.md','聊天室禁言')),
  G('聊天室成员禁言','chatroom/chrmmute',L('添加聊天室成员禁言','addchrmmute.md'),L('移除聊天室成员禁言','delchrmmute.md'),L('查询禁言的聊天室成员','qrychrmmute.md')),
  G('聊天室封禁','chatroom/chrmban',L('添加聊天室成员封禁','addchrmban.md'),L('移除聊天室成员封禁','delchrmban.md'),L('查询封禁的聊天室成员','qrychrmban.md')),
  G('聊天室白名单','chatroom/chrmallow',L('添加聊天室成员白名单','addchrmallow.md'),L('移除聊天室成员白名单','delchrmallow.md'),L('查询聊天室成员白名单','qrychrmallow.md')),
  G('好友相关','friend',L('添加好友','addfriend.md'),L('删除好友','delfriend.md'),L('查询好友列表','qryfriends.md'),L('设置好友备注名','setdisplayname.md')),L('状态码','status.md'),
 )]

TPL='''<!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"/><meta name="viewport" content="width=device-width, initial-scale=1.0"/><meta name="description" content="API reference built from local docs."/><title>API Reference | IMJunggle</title><link rel="icon" href="image/logo.svg" type="image/svg+xml" sizes="any"/><link rel="stylesheet" href="style.css"/></head><body class="page-api-docs"><header class="api-ref-topbar"><a class="api-ref-brand" href="docs.html" target="_top"><img class="api-ref-brand-mark" src="image/logo.svg" alt="" width="28" height="28" decoding="async"/><span class="api-ref-brand-text">Documentation</span></a><nav class="api-ref-topnav" aria-label="Docs navigation"><a href="docs.html" target="_top">文档中心</a><a href="developers.html" target="_top">Developers</a><a href="product.html" target="_top">Product</a></nav></header><div class="api-ref-shell"><aside class="api-sidebar api-md-tree" aria-label="Reference tree"><div class="api-sidebar-heading"><p class="api-sidebar-kicker">API Reference</p><h1 class="api-sidebar-title">文档目录</h1></div>__TREE__</aside><main class="api-doc-main"><div class="api-doc-chrome"><h1 id="api-doc-title" class="api-doc-title">API Reference</h1><p id="api-md-current" class="api-md-current"></p></div><article id="api-md-content" class="doc-juggle-body markdown api-md-content"></article></main></div><script id="api-md-index-data" type="application/json">__IDX__</script><script src="https://cdn.jsdelivr.net/npm/marked@11.2.0/marked.min.js"></script><script>(function(){var tree=document.querySelector('.api-md-tree'),content=document.getElementById('api-md-content'),current=document.getElementById('api-md-current'),titleEl=document.getElementById('api-doc-title'),raw=document.getElementById('api-md-index-data');if(!tree||!content||!raw||!titleEl)return;var docs=[];try{docs=JSON.parse((raw.textContent||'[]').replace(/^\uFEFF/,'').trim())}catch(e){}var by=Object.create(null);docs.forEach(function(d){by[d.path]=d});if(!docs.length||!window.marked){content.innerHTML='<p>Docs index or markdown renderer failed to load.</p>';return;}marked.setOptions({mangle:false,headerIds:true,breaks:true,gfm:true});var parseMd=function(md){var fn=typeof marked.parse==='function'?marked.parse.bind(marked):marked;return fn(md||'')};function esc(s){return String(s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}function escA(s){return String(s).replace(/&/g,'&amp;').replace(/"/g,'&quot;')}function tabH(x){var m=x.match(/values=\{\s*\[([\s\S]*?)\]\s*\}/),a=[];if(m){var r=/\{\s*label:\s*['"]([^'"]+)['"]\s*,\s*value:\s*['"]([^'"]+)['"]\s*,?\s*\}/g,y;while((y=r.exec(m[1])))a.push({label:y[1],value:y[2]})}return a}function tabB(x){var i=x.replace(/^<Tabs\b[^>]*>/i,'').replace(/<\/Tabs>\s*$/i,''),o={},r=/<TabItem\s+value=["']([^"']+)["']>\s*([\s\S]*?)\s*<\/TabItem>/gi,y;while((y=r.exec(i)))o[y[1]]=y[2].trim();return o}function tabHtml(x){var h=tabH(x),b=tabB(x),k=Object.keys(b);if(!k.length)return null;if(!h.length)h=k.map(function(v){return{label:v,value:v}});var p=['<div class="mdx-tabs" role="region" aria-label="Tabs"><div class="mdx-tab-bar" role="tablist">'];h.forEach(function(v,i){p.push('<button type="button" class="mdx-tab-btn'+(i? '':' is-active')+'" role="tab" aria-selected="'+(i?'false':'true')+'" data-mdx-tab="'+escA(v.value)+'">'+esc(v.label)+'</button>')});p.push('</div><div class="mdx-tab-panels">');h.forEach(function(v,i){p.push('<div class="mdx-tab-panel'+(i?'':' is-active')+'" role="tabpanel" data-mdx-panel="'+escA(v.value)+'"'+(i?' hidden':'')+'>'+parseMd(b[v.value]||'')+'</div>')});p.push('</div></div>');return p.join('')}function render(md){var r=/<Tabs\b[^>]*>[\s\S]*?<\/Tabs>/gi,o=[],l=0,m;while((m=r.exec(md))){o.push(parseMd(md.slice(l,m.index)));o.push(tabHtml(m[0])||parseMd(m[0]));l=r.lastIndex}o.push(parseMd(md.slice(l)));return o.join('')}function strip(md){if(!md||md.indexOf('---')!==0)return md;var e=md.indexOf('\n---',3);return e===-1?md:md.slice(e+4).replace(/^\s+/,'')}function dir(p){var i=p.lastIndexOf('/');return i===-1?'':p.slice(0,i+1)}function res(base,rel){if(!rel||/^(https?:)?\/\//i.test(rel)||rel.startsWith('data:')||rel.startsWith('#'))return rel;var s=dir(base).split('/').filter(Boolean);rel.split('/').forEach(function(part){if(!part||part=='.')return;if(part=='..')s.pop();else s.push(part)});return s.join('/')}function active(path){tree.querySelectorAll('a.is-active').forEach(function(a){a.classList.remove('is-active')});var link=tree.querySelector('a[data-doc-path="'+path.replace(/"/g,'&quot;')+'"]');if(link){link.classList.add('is-active');var p=link.parentElement;while(p&&tree.contains(p)){if(p.tagName==='DETAILS')p.open=true;p=p.parentElement}}}function rewrite(path){content.querySelectorAll('img[src]').forEach(function(img){var src=res(path,img.getAttribute('src'));if(src)img.setAttribute('src',src)});content.querySelectorAll('a[href]').forEach(function(a){var href=a.getAttribute('href');if(!href||href.startsWith('#'))return;var rr=res(path,href);if(!rr)return;if(/\.mdx?($|#|\?)/i.test(rr)){a.setAttribute('href','#'+encodeURIComponent(rr));a.setAttribute('data-doc-path',rr);a.removeAttribute('target')}else if(/^(https?:)?\/\//i.test(rr)){a.setAttribute('href',rr);a.setAttribute('target','_blank');a.setAttribute('rel','noopener noreferrer')}else a.setAttribute('href',rr)})}function openDoc(path,push){if(!path)return;fetch(path).then(function(r){if(!r.ok)throw new Error('HTTP '+r.status);return r.text()}).then(function(md){content.innerHTML=render(strip(md||''))||'<p>No content was produced for this page.</p>';rewrite(path);var meta=by[path]||{};titleEl.textContent=meta.navLabel||meta.title||path;current.textContent=path}).catch(function(err){content.innerHTML='<p>Failed to load markdown: '+String(err)+'</p>'});active(path);if(push!==false)try{history.replaceState(null,'','#'+encodeURIComponent(path))}catch(e){}}document.addEventListener('click',function(e){var b=e.target.closest('.mdx-tab-btn');if(b&&content.contains(b)){var root=b.closest('.mdx-tabs');if(root){var v=b.getAttribute('data-mdx-tab');root.querySelectorAll('.mdx-tab-btn').forEach(function(x){var on=x===b;x.classList.toggle('is-active',on);x.setAttribute('aria-selected',on?'true':'false')});root.querySelectorAll('.mdx-tab-panel').forEach(function(p){var on=p.getAttribute('data-mdx-panel')===v;if(on)p.removeAttribute('hidden');else p.setAttribute('hidden','');p.classList.toggle('is-active',on)})}return}var a=e.target.closest('a[data-doc-path]');if(!a)return;e.preventDefault();openDoc(a.getAttribute('data-doc-path'),true)});window.addEventListener('hashchange',function(){var h=decodeURIComponent((location.hash||'').slice(1)||'');if(h)openDoc(h,false)});var initial=decodeURIComponent((location.hash||'').slice(1)||'');openDoc(by[initial]?initial:docs[0].path,false)})();</script></body></html>'''
def title_of(p):
    t=p.read_text(encoding='utf-8')
    m=re.search(r'^title:\s*(.+)$',t,re.M)
    return m.group(1).strip().strip('"\'') if m else p.stem

def norm(s): return re.sub(r'[\s\-_/|()（）【】\[\]·,.:：]+','',s).lower()
def ok(title,aliases):
    t=norm(title)
    return any((a:=norm(x)) and (t==a or a in t or t in a) for x in aliases)

def docs():
    out=[]
    for p in sorted(OUT.rglob('*')):
        if p.is_file() and p.suffix.lower() in {'.md','.mdx'}:
            out.append({'path':p.relative_to(ROOT).as_posix(),'title':title_of(p)})
    return out

def filt(nodes,base,by):
    out=[]
    for n in nodes:
        prefix=(base+'/'+n['p']).strip('/') if n['t']=='g' else base
        if n['t']=='l':
            path=f'api-md/{base}/{n["r"]}'.replace('//','/')
            d=by.get(path)
            if d and ok(d['title'],n['a']):
                out.append({'t':'l','l':n['l'],'path':path,'ok':True})
            else:
                out.append({'t':'l','l':n['l'],'path':'','ok':False})
        else:
            kids=filt(n['c'],prefix,by)
            out.append({'t':'g','l':n['l'],'c':kids})
    return out

def html(nodes,d=0):
    cls='api-md-tree-root' if d==0 else 'api-md-tree-branch'
    s=[f'<ul class="{cls}">']
    for n in nodes:
        if n['t']=='g':
            s+=['<li>',f'<details class="api-md-group"{" open" if d<1 else ""}><summary>{escape(n["l"])}</summary>',html(n['c'],d+1),'</details>','</li>']
        else:
            if n.get('ok'):
                s.append(f'<li><a href="#{escape(n["path"])}" data-doc-path="{escape(n["path"])}">{escape(n["l"])}</a></li>')
            else:
                s.append(f'<li><span class="api-md-missing" aria-disabled="true" title="No matching local markdown file found">{escape(n["l"])}</span></li>')
    s.append('</ul>')
    return ''.join(s)

def leaves(nodes):
    out=[]
    for n in nodes:
        out += ([n] if n['t']=='l' and n.get('ok') else []) if n['t']=='l' else leaves(n['c'])
    return out

def main():
    d=docs(); by={x['path']:x for x in d}; nav=filt(NAV,'',by); navmap={x['path']:x['l'] for x in leaves(nav)}
    idx=[{'path':x['path'],'title':x['title'],'navLabel':navmap.get(x['path'],x['title'])} for x in d]
    HTML.write_text(TPL.replace('__TREE__',html(nav)).replace('__IDX__',json.dumps(idx,ensure_ascii=False)),encoding='utf-8')
    print('docs',len(d),'leafs',len(navmap))

if __name__=='__main__': main()
