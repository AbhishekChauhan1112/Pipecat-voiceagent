ype /help <enter> to see a list of commands



+OK log level  [7]
2026-05-07 07:40:18.628555 93.70% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/888892@13.235.45.114 [00c25b6d-eebe-4e24-ad96-b23a45661f52]
2026-05-07 07:40:18.628555 93.70% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/888892@13.235.45.114) Running State Change CS_NEW (Cur 1 Tot 11888)
2026-05-07 07:40:18.628555 93.70% [INFO] sofia.c:10460 sofia/internal/888892@13.235.45.114 receiving invite from 199.127.61.12:57062 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 963258398-1268379939-2050393006
2026-05-07 07:40:18.628555 93.70% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:40:18.628555 93.70% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/888892@13.235.45.114) State NEW
2026-05-07 07:40:18.628555 93.70% [DEBUG] sofia.c:2419 detaching session 00c25b6d-eebe-4e24-ad96-b23a45661f52
2026-05-07 07:40:18.888598 93.73% [DEBUG] sofia.c:2532 Re-attaching to session 00c25b6d-eebe-4e24-ad96-b23a45661f52
2026-05-07 07:40:18.888598 93.73% [INFO] sofia.c:10460 sofia/internal/888892@13.235.45.114 receiving invite from 199.127.61.12:57062 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 963258398-1268379939-2050393006
2026-05-07 07:40:18.888598 93.73% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:40:18.888598 93.73% [WARNING] sofia_reg.c:3210 Can't find user [888892@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="888892" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:40:18.888598 93.73% [NOTICE] sofia.c:2417 Hangup sofia/internal/888892@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:40:18.908609 93.73% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/888892@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 11888)
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/888892@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/888892@13.235.45.114) State HANGUP
2026-05-07 07:40:18.908609 93.73% [DEBUG] mod_sofia.c:469 Channel sofia/internal/888892@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:59 sofia/internal/888892@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/888892@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/888892@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/888892@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 11888)
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/888892@13.235.45.114) State REPORTING
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:168 sofia/internal/888892@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/888892@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/888892@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_session.c:1744 Session 11888 (sofia/internal/888892@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:40:18.908609 93.73% [NOTICE] switch_core_session.c:1762 Session 11888 (sofia/internal/888892@13.235.45.114) Ended
2026-05-07 07:40:18.908609 93.73% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/888892@13.235.45.114 [CS_DESTROY]
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/888892@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 11888)
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/888892@13.235.45.114) State DESTROY
2026-05-07 07:40:18.908609 93.73% [DEBUG] mod_sofia.c:380 sofia/internal/888892@13.235.45.114 SOFIA DESTROY
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:175 sofia/internal/888892@13.235.45.114 Standard DESTROY
2026-05-07 07:40:18.908609 93.73% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/888892@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:40:22.788642 93.73% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/9100111323545114@13.235.45.114 [13a29b91-c918-487d-8237-bffe452c7ca4]
2026-05-07 07:40:22.788642 93.73% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/9100111323545114@13.235.45.114) Running State Change CS_NEW (Cur 1 Tot 11889)
2026-05-07 07:40:22.788642 93.73% [INFO] sofia.c:10460 sofia/internal/9100111323545114@13.235.45.114 receiving invite from 5.196.63.60:62238 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1151786333-2025968881-280422438
2026-05-07 07:40:22.788642 93.73% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 5.196.63.60:0.
2026-05-07 07:40:22.788642 93.73% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/9100111323545114@13.235.45.114) State NEW
2026-05-07 07:40:22.788642 93.73% [DEBUG] sofia.c:2419 detaching session 13a29b91-c918-487d-8237-bffe452c7ca4
2026-05-07 07:40:23.128590 93.73% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/1000@13.235.45.114 [f4d2cb35-75ae-4399-b838-1707c9fb0186]
2026-05-07 07:40:23.128590 93.73% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11890)
2026-05-07 07:40:23.128590 93.73% [INFO] sofia.c:10460 sofia/internal/1000@13.235.45.114 receiving invite from 86.107.100.98:50940 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: Tvo7i47hqX
2026-05-07 07:40:23.128590 93.73% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 86.107.100.98:0.
2026-05-07 07:40:23.128590 93.73% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/1000@13.235.45.114) State NEW
2026-05-07 07:40:23.128590 93.73% [DEBUG] sofia.c:2419 detaching session f4d2cb35-75ae-4399-b838-1707c9fb0186
2026-05-07 07:40:23.188496 93.73% [DEBUG] sofia.c:2532 Re-attaching to session f4d2cb35-75ae-4399-b838-1707c9fb0186
2026-05-07 07:40:23.208553 93.73% [INFO] sofia.c:10460 sofia/internal/1000@13.235.45.114 receiving invite from 86.107.100.98:50940 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: Tvo7i47hqX
2026-05-07 07:40:23.208553 93.73% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 86.107.100.98:0.
2026-05-07 07:40:23.208553 93.73% [DEBUG] sofia.c:7493 Channel sofia/internal/1000@13.235.45.114 entering state [received][100]
2026-05-07 07:40:23.208553 93.73% [DEBUG] sofia.c:7503 Remote SDP:
v=0
o=1000 496 2809 IN IP4 86.107.100.98
s=Talk
c=IN IP4 86.107.100.98
t=0 0
a=rtcp-xr:rcvr-rtt=all:10000 stat-summary=loss,dup,jitt,TTL voip-metrics
a=record:off
m=audio 44305 RTP/AVP 96 97 98 0 8 18 101 99 100
a=rtpmap:96 opus/48000/2
a=fmtp:96 useinbandfec=1
a=rtpmap:97 speex/16000
a=fmtp:97 vbr=on
a=rtpmap:98 speex/8000
a=fmtp:98 vbr=on
a=fmtp:18 annexb=yes
a=rtpmap:101 telephone-event/48000
a=rtpmap:99 telephone-event/16000
a=rtpmap:100 telephone-event/8000
a=rtcp:59090
a=rtcp-fb:* trr-int 1000
a=rtcp-fb:* ccm tmmbr

2026-05-07 07:40:23.208553 93.73% [DEBUG] sofia.c:7906 (sofia/internal/1000@13.235.45.114) State Change CS_NEW -> CS_INIT
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_INIT (Cur 2 Tot 11890)
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:624 (sofia/internal/1000@13.235.45.114) State INIT
2026-05-07 07:40:23.208553 93.73% [DEBUG] mod_sofia.c:97 sofia/internal/1000@13.235.45.114 SOFIA INIT
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:40 sofia/internal/1000@13.235.45.114 Standard INIT
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:48 (sofia/internal/1000@13.235.45.114) State Change CS_INIT -> CS_ROUTING
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:624 (sofia/internal/1000@13.235.45.114) State INIT going to sleep
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_ROUTING (Cur 2 Tot 11890)
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_channel.c:2399 (sofia/internal/1000@13.235.45.114) Callstate Change DOWN -> RINGING
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:640 (sofia/internal/1000@13.235.45.114) State ROUTING
2026-05-07 07:40:23.208553 93.73% [DEBUG] mod_sofia.c:158 sofia/internal/1000@13.235.45.114 SOFIA ROUTING
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:230 sofia/internal/1000@13.235.45.114 Standard ROUTING
2026-05-07 07:40:23.208553 93.73% [INFO] mod_dialplan_xml.c:639 Processing 1000 <1000>->7007 in context default
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->unloop] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [unloop] ${unroll_loops}(true) =~ /^true$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [unloop] ${sip_looped_call}() =~ /^true$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->tod_example] continue=true
Dialplan: sofia/internal/1000@13.235.45.114 Date/TimeMatch (FAIL) [tod_example] break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->holiday_example] continue=true
Dialplan: sofia/internal/1000@13.235.45.114 Date/TimeMatch (FAIL) [holiday_example] break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->global-intercept] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [global-intercept] destination_number(7007) =~ /^886$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->group-intercept] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [group-intercept] destination_number(7007) =~ /^\*8$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->intercept-ext] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [intercept-ext] destination_number(7007) =~ /^\*\*(\d+)$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->redial] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [redial] destination_number(7007) =~ /^(redial|870)$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->global] continue=true
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [global] ${call_debug}(false) =~ /^true$/ break=never
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [global] ${default_password}(Test1234) =~ /^1234$/ break=never
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [global] ${rtp_has_crypto}() =~ /^(AEAD_AES_256_GCM_8|AEAD_AES_128_GCM_8|AES_CM_256_HMAC_SHA1_80|AES_CM_192_HMAC_SHA1_80|AES_CM_128_HMAC_SHA1_80|AES_CM_256_HMAC_SHA1_32|AES_CM_192_HMAC_SHA1_32|AES_CM_128_HMAC_SHA1_32|AES_CM_128_NULL_AUTH)$/ break=never
Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [global] ${endpoint_disposition}(DELAYED NEGOTIATION) =~ /^(DELAYED NEGOTIATION)/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [global] ${switch_r_sdp}(v=0
o=1000 496 2809 IN IP4 86.107.100.98
s=Talk
c=IN IP4 86.107.100.98
t=0 0
a=rtcp-xr:rcvr-rtt=all:10000 stat-summary=loss,dup,jitt,TTL voip-metrics
a=record:off
m=audio 44305 RTP/AVP 96 97 98 0 8 18 101 99 100
a=rtpmap:96 opus/48000/2
a=fmtp:96 useinbandfec=1
a=rtpmap:97 speex/16000
a=fmtp:97 vbr=on
a=rtpmap:98 speex/8000
a=fmtp:98 vbr=on
a=fmtp:18 annexb=yes
a=rtpmap:101 telephone-event/48000
a=rtpmap:99 telephone-event/16000
a=rtpmap:100 telephone-event/8000
a=rtcp:59090
a=rtcp-fb:* trr-int 1000
a=rtcp-fb:* ccm tmmbr
) =~ /(AES_CM_128_HMAC_SHA1_32|AES_CM_128_HMAC_SHA1_80)/ break=never
Dialplan: sofia/internal/1000@13.235.45.114 Absolute Condition [global]
Dialplan: sofia/internal/1000@13.235.45.114 Action hash(insert/${domain_name}-spymap/${caller_id_number}/${uuid}) 
Dialplan: sofia/internal/1000@13.235.45.114 Action hash(insert/${domain_name}-last_dial/${caller_id_number}/${destination_number}) 
Dialplan: sofia/internal/1000@13.235.45.114 Action hash(insert/${domain_name}-last_dial/global/${uuid}) 
Dialplan: sofia/internal/1000@13.235.45.114 Action export(RFC2822_DATE=${strftime(%a, %d %b %Y %T %z)}) 
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->snom-demo-2] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [snom-demo-2] destination_number(7007) =~ /^9001$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->snom-demo-1] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [snom-demo-1] destination_number(7007) =~ /^9000$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->eavesdrop] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [eavesdrop] destination_number(7007) =~ /^88(\d{4})$|^\*0(.*)$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->eavesdrop] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [eavesdrop] destination_number(7007) =~ /^779$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->call_return] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [call_return] destination_number(7007) =~ /^\*69$|^869$|^lcr$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->del-group] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [del-group] destination_number(7007) =~ /^80(\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->add-group] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [add-group] destination_number(7007) =~ /^81(\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->call-group-simo] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [call-group-simo] destination_number(7007) =~ /^82(\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->call-group-order] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [call-group-order] destination_number(7007) =~ /^83(\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->extension-intercom] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [extension-intercom] destination_number(7007) =~ /^8(10[01][0-9])$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->Local_Extension] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [Local_Extension] destination_number(7007) =~ /^(10[01][0-9])$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->Local_Extension_Skinny] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [Local_Extension_Skinny] destination_number(7007) =~ /^(11[01][0-9])$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->group_dial_sales] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [group_dial_sales] destination_number(7007) =~ /^2000$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->group_dial_support] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [group_dial_support] destination_number(7007) =~ /^2001$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->group_dial_billing] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [group_dial_billing] destination_number(7007) =~ /^2002$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->operator] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [operator] destination_number(7007) =~ /^(operator|0)$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->vmain] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [vmain] destination_number(7007) =~ /^vmain$|^4000$|^\*98$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->sip_uri] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [sip_uri] destination_number(7007) =~ /^sip:(.*)$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->nb_conferences] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [nb_conferences] destination_number(7007) =~ /^(30\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->wb_conferences] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [wb_conferences] destination_number(7007) =~ /^(31\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->uwb_conferences] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [uwb_conferences] destination_number(7007) =~ /^(32\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->cdquality_conferences] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [cdquality_conferences] destination_number(7007) =~ /^(33\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->cdquality_stereo_conferences] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [cdquality_stereo_conferences] destination_number(7007) =~ /^(35\d{2}).*?-screen$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->conference-canvases] continue=true
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [conference-canvases] destination_number(7007) =~ /(35\d{2})-canvas-(\d+)/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->conf mod] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [conf mod] destination_number(7007) =~ /^6070-moderator$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->cdquality_conferences] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [cdquality_conferences] destination_number(7007) =~ /^(35\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->cdquality_conferences_720] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [cdquality_conferences_720] destination_number(7007) =~ /^(36\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->cdquality_conferences_480] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [cdquality_conferences_480] destination_number(7007) =~ /^(37\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->cdquality_conferences_320] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [cdquality_conferences_320] destination_number(7007) =~ /^(38\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->freeswitch_public_conf_via_sip] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [freeswitch_public_conf_via_sip] destination_number(7007) =~ /^9(888|8888|1616|3232)$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->mad_boss_intercom] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [mad_boss_intercom] destination_number(7007) =~ /^0911$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->mad_boss_intercom] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [mad_boss_intercom] destination_number(7007) =~ /^0912$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->mad_boss] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [mad_boss] destination_number(7007) =~ /^0913$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ivr_demo] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ivr_demo] destination_number(7007) =~ /^5000$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->dynamic_conference] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [dynamic_conference] destination_number(7007) =~ /^5001$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->rtp_multicast_page] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [rtp_multicast_page] destination_number(7007) =~ /^pagegroup$|^7243$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->park] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [park] destination_number(7007) =~ /^5900$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->unpark] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [unpark] destination_number(7007) =~ /^5901$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->valet_park] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [valet_park] destination_number(7007) =~ /^(6000)$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->valet_park] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [valet_park] destination_number(7007) =~ /^((?!6000)60\d{2})$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->park] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [park] source(mod_sofia) =~ /mod_sofia/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [park] destination_number(7007) =~ /park\+(\d+)/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->unpark] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [unpark] source(mod_sofia) =~ /mod_sofia/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [unpark] destination_number(7007) =~ /^parking$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->park] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [park] source(mod_sofia) =~ /mod_sofia/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [park] destination_number(7007) =~ /callpark/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->unpark] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [unpark] source(mod_sofia) =~ /mod_sofia/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [unpark] destination_number(7007) =~ /pickup/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->wait] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [wait] destination_number(7007) =~ /^wait$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->fax_receive] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [fax_receive] destination_number(7007) =~ /^9178$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->fax_transmit] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [fax_transmit] destination_number(7007) =~ /^9179$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ringback_180] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ringback_180] destination_number(7007) =~ /^9180$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ringback_183_uk_ring] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ringback_183_uk_ring] destination_number(7007) =~ /^9181$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ringback_183_music_ring] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ringback_183_music_ring] destination_number(7007) =~ /^9182$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ringback_post_answer_uk_ring] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ringback_post_answer_uk_ring] destination_number(7007) =~ /^9183$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ringback_post_answer_music] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ringback_post_answer_music] destination_number(7007) =~ /^9184$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ClueCon] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ClueCon] destination_number(7007) =~ /^9191$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->show_info] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [show_info] destination_number(7007) =~ /^9192$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->video_record] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [video_record] destination_number(7007) =~ /^9193$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->video_playback] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [video_playback] destination_number(7007) =~ /^9194$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->delay_echo] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [delay_echo] destination_number(7007) =~ /^9195$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->echo] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [echo] destination_number(7007) =~ /^9196$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->milliwatt] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [milliwatt] destination_number(7007) =~ /^9197$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->tone_stream] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [tone_stream] destination_number(7007) =~ /^9198$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->hold_music] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [hold_music] destination_number(7007) =~ /^9664$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->laugh break] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [laugh break] destination_number(7007) =~ /^9386$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->101] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [101] destination_number(7007) =~ /^101$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->pipecat_agent] continue=false
Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [pipecat_agent] destination_number(7007) =~ /^7007$/ break=on-false
Dialplan: sofia/internal/1000@13.235.45.114 Action lua(pipecat.lua) 
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:281 (sofia/internal/1000@13.235.45.114) State Change CS_ROUTING -> CS_EXECUTE
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:640 (sofia/internal/1000@13.235.45.114) State ROUTING going to sleep
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_EXECUTE (Cur 2 Tot 11890)
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:647 (sofia/internal/1000@13.235.45.114) State EXECUTE
2026-05-07 07:40:23.208553 93.73% [DEBUG] mod_sofia.c:213 sofia/internal/1000@13.235.45.114 SOFIA EXECUTE
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_state_machine.c:323 sofia/internal/1000@13.235.45.114 Standard EXECUTE
EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 hash(insert/172.31.38.106-spymap/1000/f4d2cb35-75ae-4399-b838-1707c9fb0186)
EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 hash(insert/172.31.38.106-last_dial/1000/7007)
EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 hash(insert/172.31.38.106-last_dial/global/f4d2cb35-75ae-4399-b838-1707c9fb0186)
EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 export(RFC2822_DATE=Thu, 07 May 2026 07:40:23 +0000)
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_channel.c:1334 EXPORT (export_vars) [RFC2822_DATE]=[Thu, 07 May 2026 07:40:23 +0000]
EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 lua(pipecat.lua)
2026-05-07 07:40:23.208553 93.73% [INFO] switch_cpp.cpp:1466 === PIPECAT AGENT STARTED uuid=f4d2cb35-75ae-4399-b838-1707c9fb0186 ===
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [opus:96:48000:20:0:1]/[opus:116:48000:20:0:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5588 Audio Codec Compare [opus:116:48000:20:0:1] ++++ is saved as a match
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [opus:96:48000:20:0:1]/[PCMU:0:8000:20:64000:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [opus:96:48000:20:0:1]/[PCMA:8:8000:20:64000:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:97:16000:20:0:1]/[opus:116:48000:20:0:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:97:16000:20:0:1]/[PCMU:0:8000:20:64000:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:97:16000:20:0:1]/[PCMA:8:8000:20:64000:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:98:8000:20:0:1]/[opus:116:48000:20:0:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:98:8000:20:0:1]/[PCMU:0:8000:20:64000:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:98:8000:20:0:1]/[PCMA:8:8000:20:64000:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMU:0:8000:20:64000:1]/[opus:116:48000:20:0:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMU:0:8000:20:64000:1]/[PCMU:0:8000:20:64000:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5588 Audio Codec Compare [PCMU:0:8000:20:64000:1] ++++ is saved as a match
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMU:0:8000:20:64000:1]/[PCMA:8:8000:20:64000:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMA:8:8000:20:64000:1]/[opus:116:48000:20:0:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMA:8:8000:20:64000:1]/[PCMU:0:8000:20:64000:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMA:8:8000:20:64000:1]/[PCMA:8:8000:20:64000:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5588 Audio Codec Compare [PCMA:8:8000:20:64000:1] ++++ is saved as a match
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [G729:18:8000:20:8000:1]/[opus:116:48000:20:0:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [G729:18:8000:20:8000:1]/[PCMU:0:8000:20:64000:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [G729:18:8000:20:8000:1]/[PCMA:8:8000:20:64000:1]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5438 Set telephone-event payload to 101@48000
2026-05-07 07:40:23.208553 93.73% [DEBUG] mod_opus.c:629 Opus encoder: set bitrate to local settings [72000bps]
2026-05-07 07:40:23.208553 93.73% [DEBUG] mod_opus.c:629 Opus encoder: set bitrate to local settings [72000bps]
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:3731 Set Codec sofia/internal/1000@13.235.45.114 opus/48000 20 ms 960 samples 0 bits 1 channels
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_codec.c:111 sofia/internal/1000@13.235.45.114 Original read codec set to opus:116
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5798 Set telephone-event payload to 101@48000
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:5856 sofia/internal/1000@13.235.45.114 Set 2833 dtmf send payload to 101 recv payload to 101
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:8660 AUDIO RTP [sofia/internal/1000@13.235.45.114] 172.31.38.106 port 26922 -> 86.107.100.98 port 44305 codec: 96 ms: 20
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_rtp.c:4566 Starting timer [soft] 960 bytes per 20ms
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:8881 Activating RTCP PORT 59090
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_rtp.c:4898 RTCP send rate is: 1000 and packet rate is: 20000 Remote Port: 59090
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_rtp.c:2692 Setting RTCP remote addr to 86.107.100.98:59090 2
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:8973 sofia/internal/1000@13.235.45.114 Set 2833 dtmf send payload to 101
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:8980 sofia/internal/1000@13.235.45.114 Set 2833 dtmf receive payload to 101
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:9003 sofia/internal/1000@13.235.45.114 Set rtp dtmf delay to 40
2026-05-07 07:40:23.208553 93.73% [NOTICE] sofia_media.c:90 Pre-Answer sofia/internal/1000@13.235.45.114!
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_channel.c:3585 (sofia/internal/1000@13.235.45.114) Callstate Change RINGING -> EARLY
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_core_media.c:8642 Audio params are unchanged for sofia/internal/1000@13.235.45.114.
2026-05-07 07:40:23.208553 93.73% [DEBUG] mod_sofia.c:914 Local SDP sofia/internal/1000@13.235.45.114:
v=0
o=FreeSWITCH 1778112701 1778112702 IN IP4 13.235.45.114
s=FreeSWITCH
c=IN IP4 13.235.45.114
t=0 0
m=audio 26922 RTP/AVP 96 101
a=rtpmap:96 opus/48000/2
a=fmtp:96 useinbandfec=1
a=rtpmap:101 telephone-event/48000
a=fmtp:101 0-15
a=ptime:20
a=sendrecv
a=rtcp:26923 IN IP4 13.235.45.114

2026-05-07 07:40:23.208553 93.73% [NOTICE] switch_cpp.cpp:704 Channel [sofia/internal/1000@13.235.45.114] has been answered
2026-05-07 07:40:23.208553 93.73% [DEBUG] switch_channel.c:3912 (sofia/internal/1000@13.235.45.114) Callstate Change EARLY -> ACTIVE
2026-05-07 07:40:23.208553 93.73% [DEBUG] sofia.c:7493 Channel sofia/internal/1000@13.235.45.114 entering state [completed][200]
2026-05-07 07:40:23.508568 93.73% [DEBUG] sofia.c:7493 Channel sofia/internal/1000@13.235.45.114 entering state [ready][200]
2026-05-07 07:40:23.508568 93.73% [DEBUG] switch_rtp.c:7128 Correct audio RTCP ip/port confirmed.
2026-05-07 07:40:23.608480 93.73% [DEBUG] switch_rtp.c:1934 rtcp_stats_init: audio ssrc[838991930] base_seq[0]
2026-05-07 07:40:23.608480 93.73% [DEBUG] switch_rtp.c:7698 Correct audio ip/port confirmed.
2026-05-07 07:40:23.728565 93.73% [INFO] switch_cpp.cpp:1466 Sending: uuid_audio_stream f4d2cb35-75ae-4399-b838-1707c9fb0186 start ws://127.0.0.1:8765 stereo 16000
2026-05-07 07:40:23.728565 93.73% [DEBUG] mod_audio_stream.c:151 mod_audio_stream cmd: f4d2cb35-75ae-4399-b838-1707c9fb0186 start ws://127.0.0.1:8765 stereo 16000
2026-05-07 07:40:23.728565 93.73% [DEBUG] mod_audio_stream.c:82 calling stream_session_init.
2026-05-07 07:40:23.728565 93.73% [DEBUG] audio_streamer_glue.cpp:485 (f4d2cb35-75ae-4399-b838-1707c9fb0186) resampling from 48000 to 16000
2026-05-07 07:40:23.728565 93.73% [DEBUG] audio_streamer_glue.cpp:496 (f4d2cb35-75ae-4399-b838-1707c9fb0186) stream_data_init
2026-05-07 07:40:23.728565 93.73% [DEBUG] mod_audio_stream.c:88 adding bug.
2026-05-07 07:40:23.728565 93.73% [DEBUG] switch_core_media_bug.c:976 Attaching BUG to sofia/internal/1000@13.235.45.114
2026-05-07 07:40:23.728565 93.73% [DEBUG] mod_audio_stream.c:92 setting bug private data.
2026-05-07 07:40:23.728565 93.73% [DEBUG] mod_audio_stream.c:95 exiting start_capture.
2026-05-07 07:40:23.728565 93.73% [INFO] switch_cpp.cpp:1466 Result: +OK Success

2026-05-07 07:40:23.788465 93.63% [DEBUG] switch_core_io.c:448 Setting BUG Codec opus:116
2026-05-07 07:40:23.788465 93.63% [DEBUG] mod_opus.c:629 Opus encoder: set bitrate to local settings [72000bps]
2026-05-07 07:40:27.688608 92.37% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/888892@13.235.45.114 [2dd3792a-c074-4412-b0e6-185d87dfda4a]
2026-05-07 07:40:27.688608 92.37% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/888892@13.235.45.114) Running State Change CS_NEW (Cur 3 Tot 11891)
2026-05-07 07:40:27.688608 92.37% [INFO] sofia.c:10460 sofia/internal/888892@13.235.45.114 receiving invite from 199.127.61.12:55735 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1977094592-1810129133-809857685
2026-05-07 07:40:27.688608 92.37% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:40:27.688608 92.37% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/888892@13.235.45.114) State NEW
2026-05-07 07:40:27.688608 92.37% [DEBUG] sofia.c:2419 detaching session 2dd3792a-c074-4412-b0e6-185d87dfda4a
2026-05-07 07:40:27.948550 92.37% [DEBUG] sofia.c:2532 Re-attaching to session 2dd3792a-c074-4412-b0e6-185d87dfda4a
2026-05-07 07:40:27.948550 92.37% [INFO] sofia.c:10460 sofia/internal/888892@13.235.45.114 receiving invite from 199.127.61.12:55735 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1977094592-1810129133-809857685
2026-05-07 07:40:27.948550 92.37% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:40:27.948550 92.37% [WARNING] sofia_reg.c:3210 Can't find user [888892@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="888892" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:40:27.948550 92.37% [NOTICE] sofia.c:2417 Hangup sofia/internal/888892@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:40:27.968585 92.37% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:40:27.968585 92.37% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/888892@13.235.45.114) Running State Change CS_HANGUP (Cur 3 Tot 11891)
2026-05-07 07:40:27.968585 92.37% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/888892@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:40:27.968585 92.37% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/888892@13.235.45.114) State HANGUP
2026-05-07 07:40:27.968585 92.37% [DEBUG] mod_sofia.c:469 Channel sofia/internal/888892@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:40:27.968585 92.37% [DEBUG] switch_core_state_machine.c:59 sofia/internal/888892@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:40:27.968585 92.37% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/888892@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:40:27.968585 92.37% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/888892@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:40:27.968585 92.37% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/888892@13.235.45.114) Running State Change CS_REPORTING (Cur 3 Tot 11891)
2026-05-07 07:40:27.988565 92.37% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/888892@13.235.45.114) State REPORTING
2026-05-07 07:40:27.988565 92.37% [DEBUG] switch_core_state_machine.c:168 sofia/internal/888892@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:40:27.988565 92.37% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/888892@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:40:27.988565 92.37% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/888892@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:40:27.988565 92.37% [DEBUG] switch_core_session.c:1744 Session 11891 (sofia/internal/888892@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:40:27.988565 92.37% [NOTICE] switch_core_session.c:1762 Session 11891 (sofia/internal/888892@13.235.45.114) Ended
2026-05-07 07:40:27.988565 92.37% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/888892@13.235.45.114 [CS_DESTROY]
2026-05-07 07:40:27.988565 92.37% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/888892@13.235.45.114) Running State Change CS_DESTROY (Cur 2 Tot 11891)
2026-05-07 07:40:27.988565 92.37% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/888892@13.235.45.114) State DESTROY
2026-05-07 07:40:27.988565 92.37% [DEBUG] mod_sofia.c:380 sofia/internal/888892@13.235.45.114 SOFIA DESTROY
2026-05-07 07:40:27.988565 92.37% [DEBUG] switch_core_state_machine.c:175 sofia/internal/888892@13.235.45.114 Standard DESTROY
2026-05-07 07:40:27.988565 92.37% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/888892@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:40:32.828509 93.83% [WARNING] switch_core_state_machine.c:684 13a29b91-c918-487d-8237-bffe452c7ca4 sofia/internal/9100111323545114@13.235.45.114 Abandoned
2026-05-07 07:40:32.828509 93.83% [NOTICE] switch_core_state_machine.c:687 Hangup sofia/internal/9100111323545114@13.235.45.114 [CS_NEW] [WRONG_CALL_STATE]
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/9100111323545114@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11891)
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/9100111323545114@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/9100111323545114@13.235.45.114) State HANGUP
2026-05-07 07:40:32.828509 93.83% [DEBUG] mod_sofia.c:469 Channel sofia/internal/9100111323545114@13.235.45.114 hanging up, cause: WRONG_CALL_STATE
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:59 sofia/internal/9100111323545114@13.235.45.114 Standard HANGUP, cause: WRONG_CALL_STATE
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/9100111323545114@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/9100111323545114@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/9100111323545114@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11891)
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/9100111323545114@13.235.45.114) State REPORTING
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:168 sofia/internal/9100111323545114@13.235.45.114 Standard REPORTING, cause: WRONG_CALL_STATE
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/9100111323545114@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/9100111323545114@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_session.c:1744 Session 11889 (sofia/internal/9100111323545114@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:40:32.828509 93.83% [NOTICE] switch_core_session.c:1762 Session 11889 (sofia/internal/9100111323545114@13.235.45.114) Ended
2026-05-07 07:40:32.828509 93.83% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/9100111323545114@13.235.45.114 [CS_DESTROY]
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/9100111323545114@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11891)
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/9100111323545114@13.235.45.114) State DESTROY
2026-05-07 07:40:32.828509 93.83% [DEBUG] mod_sofia.c:380 sofia/internal/9100111323545114@13.235.45.114 SOFIA DESTROY
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:175 sofia/internal/9100111323545114@13.235.45.114 Standard DESTROY
2026-05-07 07:40:32.828509 93.83% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/9100111323545114@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:40:39.388482 97.67% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/7305@13.235.45.114 [add3e641-9089-451f-a1f6-c363833f9d94]
2026-05-07 07:40:39.388482 97.67% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7305@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11892)
2026-05-07 07:40:39.388482 97.67% [INFO] sofia.c:10460 sofia/internal/7305@13.235.45.114 receiving invite from 199.127.61.12:61144 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1194948866-514999119-2042583813
2026-05-07 07:40:39.388482 97.67% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:40:39.388482 97.67% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/7305@13.235.45.114) State NEW
2026-05-07 07:40:39.388482 97.67% [DEBUG] sofia.c:2419 detaching session add3e641-9089-451f-a1f6-c363833f9d94
2026-05-07 07:40:39.628520 97.67% [DEBUG] sofia.c:2532 Re-attaching to session add3e641-9089-451f-a1f6-c363833f9d94
2026-05-07 07:40:39.648593 97.67% [INFO] sofia.c:10460 sofia/internal/7305@13.235.45.114 receiving invite from 199.127.61.12:61144 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1194948866-514999119-2042583813
2026-05-07 07:40:39.648593 97.67% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:40:39.648593 97.67% [WARNING] sofia_reg.c:3210 Can't find user [7305@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="7305" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:40:39.648593 97.67% [NOTICE] sofia.c:2417 Hangup sofia/internal/7305@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:40:39.668595 97.67% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7305@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11892)
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/7305@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/7305@13.235.45.114) State HANGUP
2026-05-07 07:40:39.668595 97.67% [DEBUG] mod_sofia.c:469 Channel sofia/internal/7305@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:59 sofia/internal/7305@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/7305@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/7305@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7305@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11892)
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/7305@13.235.45.114) State REPORTING
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:168 sofia/internal/7305@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/7305@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/7305@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_session.c:1744 Session 11892 (sofia/internal/7305@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:40:39.668595 97.67% [NOTICE] switch_core_session.c:1762 Session 11892 (sofia/internal/7305@13.235.45.114) Ended
2026-05-07 07:40:39.668595 97.67% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/7305@13.235.45.114 [CS_DESTROY]
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/7305@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11892)
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/7305@13.235.45.114) State DESTROY
2026-05-07 07:40:39.668595 97.67% [DEBUG] mod_sofia.c:380 sofia/internal/7305@13.235.45.114 SOFIA DESTROY
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:175 sofia/internal/7305@13.235.45.114 Standard DESTROY
2026-05-07 07:40:39.668595 97.67% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/7305@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:40:48.028579 97.67% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/7305@13.235.45.114 [9b758129-3598-4e41-88f8-4ec41b17efd5]
2026-05-07 07:40:48.028579 97.67% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7305@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11893)
2026-05-07 07:40:48.028579 97.67% [INFO] sofia.c:10460 sofia/internal/7305@13.235.45.114 receiving invite from 199.127.61.12:64414 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1765886487-172392801-1311691351
2026-05-07 07:40:48.028579 97.67% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:40:48.028579 97.67% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/7305@13.235.45.114) State NEW
2026-05-07 07:40:48.028579 97.67% [DEBUG] sofia.c:2419 detaching session 9b758129-3598-4e41-88f8-4ec41b17efd5
2026-05-07 07:40:48.288543 97.67% [DEBUG] sofia.c:2532 Re-attaching to session 9b758129-3598-4e41-88f8-4ec41b17efd5
2026-05-07 07:40:48.308574 97.67% [INFO] sofia.c:10460 sofia/internal/7305@13.235.45.114 receiving invite from 199.127.61.12:64414 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1765886487-172392801-1311691351
2026-05-07 07:40:48.308574 97.67% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:40:48.308574 97.67% [WARNING] sofia_reg.c:3210 Can't find user [7305@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="7305" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:40:48.308574 97.67% [NOTICE] sofia.c:2417 Hangup sofia/internal/7305@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:40:48.328513 97.67% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7305@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11893)
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/7305@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/7305@13.235.45.114) State HANGUP
2026-05-07 07:40:48.328513 97.67% [DEBUG] mod_sofia.c:469 Channel sofia/internal/7305@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:59 sofia/internal/7305@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/7305@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/7305@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7305@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11893)
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/7305@13.235.45.114) State REPORTING
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:168 sofia/internal/7305@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/7305@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/7305@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_session.c:1744 Session 11893 (sofia/internal/7305@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:40:48.328513 97.67% [NOTICE] switch_core_session.c:1762 Session 11893 (sofia/internal/7305@13.235.45.114) Ended
2026-05-07 07:40:48.328513 97.67% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/7305@13.235.45.114 [CS_DESTROY]
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/7305@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11893)
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/7305@13.235.45.114) State DESTROY
2026-05-07 07:40:48.328513 97.67% [DEBUG] mod_sofia.c:380 sofia/internal/7305@13.235.45.114 SOFIA DESTROY
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:175 sofia/internal/7305@13.235.45.114 Standard DESTROY
2026-05-07 07:40:48.328513 97.67% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/7305@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:40:55.048640 98.97% [WARNING] sofia_reg.c:3210 Can't find user [1020@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1020" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:40:56.688576 99.03% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/7305@13.235.45.114 [ab1521fe-2066-4f0e-9baa-b689c599abc5]
2026-05-07 07:40:56.688576 99.03% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7305@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11894)
2026-05-07 07:40:56.688576 99.03% [INFO] sofia.c:10460 sofia/internal/7305@13.235.45.114 receiving invite from 199.127.61.12:50801 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 31554017-839831228-2115151734
2026-05-07 07:40:56.688576 99.03% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:40:56.688576 99.03% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/7305@13.235.45.114) State NEW
2026-05-07 07:40:56.688576 99.03% [DEBUG] sofia.c:2419 detaching session ab1521fe-2066-4f0e-9baa-b689c599abc5
2026-05-07 07:40:56.948609 99.03% [DEBUG] sofia.c:2532 Re-attaching to session ab1521fe-2066-4f0e-9baa-b689c599abc5
2026-05-07 07:40:56.948609 99.03% [INFO] sofia.c:10460 sofia/internal/7305@13.235.45.114 receiving invite from 199.127.61.12:50801 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 31554017-839831228-2115151734
2026-05-07 07:40:56.948609 99.03% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:40:56.948609 99.03% [WARNING] sofia_reg.c:3210 Can't find user [7305@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="7305" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:40:56.948609 99.03% [NOTICE] sofia.c:2417 Hangup sofia/internal/7305@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:40:56.968592 99.03% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7305@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11894)
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/7305@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/7305@13.235.45.114) State HANGUP
2026-05-07 07:40:56.968592 99.03% [DEBUG] mod_sofia.c:469 Channel sofia/internal/7305@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:59 sofia/internal/7305@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/7305@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/7305@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7305@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11894)
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/7305@13.235.45.114) State REPORTING
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:168 sofia/internal/7305@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/7305@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/7305@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_session.c:1744 Session 11894 (sofia/internal/7305@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:40:56.968592 99.03% [NOTICE] switch_core_session.c:1762 Session 11894 (sofia/internal/7305@13.235.45.114) Ended
2026-05-07 07:40:56.968592 99.03% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/7305@13.235.45.114 [CS_DESTROY]
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/7305@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11894)
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/7305@13.235.45.114) State DESTROY
2026-05-07 07:40:56.968592 99.03% [DEBUG] mod_sofia.c:380 sofia/internal/7305@13.235.45.114 SOFIA DESTROY
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:175 sofia/internal/7305@13.235.45.114 Standard DESTROY
2026-05-07 07:40:56.968592 99.03% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/7305@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:40:59.928584 99.03% [WARNING] sofia_reg.c:3210 Can't find user [1021@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1021" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:07.148638 98.93% [WARNING] sofia_reg.c:3210 Can't find user [1022@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1022" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:11.368588 99.00% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/777788@13.235.45.114 [1ca48356-e0b7-412b-aa04-97602aa2f9ec]
2026-05-07 07:41:11.368588 99.00% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/777788@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11895)
2026-05-07 07:41:11.368588 99.00% [INFO] sofia.c:10460 sofia/internal/777788@13.235.45.114 receiving invite from 199.127.61.12:57331 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1383588849-1197912520-487696246
2026-05-07 07:41:11.368588 99.00% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:41:11.368588 99.00% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/777788@13.235.45.114) State NEW
2026-05-07 07:41:11.368588 99.00% [DEBUG] sofia.c:2419 detaching session 1ca48356-e0b7-412b-aa04-97602aa2f9ec
2026-05-07 07:41:11.628616 99.00% [DEBUG] sofia.c:2532 Re-attaching to session 1ca48356-e0b7-412b-aa04-97602aa2f9ec
2026-05-07 07:41:11.628616 99.00% [INFO] sofia.c:10460 sofia/internal/777788@13.235.45.114 receiving invite from 199.127.61.12:57331 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1383588849-1197912520-487696246
2026-05-07 07:41:11.628616 99.00% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:41:11.628616 99.00% [WARNING] sofia_reg.c:3210 Can't find user [777788@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="777788" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:11.628616 99.00% [NOTICE] sofia.c:2417 Hangup sofia/internal/777788@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:41:11.648623 99.00% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/777788@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11895)
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/777788@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/777788@13.235.45.114) State HANGUP
2026-05-07 07:41:11.648623 99.00% [DEBUG] mod_sofia.c:469 Channel sofia/internal/777788@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:59 sofia/internal/777788@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/777788@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/777788@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/777788@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11895)
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/777788@13.235.45.114) State REPORTING
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:168 sofia/internal/777788@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/777788@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/777788@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_session.c:1744 Session 11895 (sofia/internal/777788@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:41:11.648623 99.00% [NOTICE] switch_core_session.c:1762 Session 11895 (sofia/internal/777788@13.235.45.114) Ended
2026-05-07 07:41:11.648623 99.00% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/777788@13.235.45.114 [CS_DESTROY]
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/777788@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11895)
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/777788@13.235.45.114) State DESTROY
2026-05-07 07:41:11.648623 99.00% [DEBUG] mod_sofia.c:380 sofia/internal/777788@13.235.45.114 SOFIA DESTROY
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:175 sofia/internal/777788@13.235.45.114 Standard DESTROY
2026-05-07 07:41:11.648623 99.00% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/777788@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:41:12.068494 98.93% [WARNING] sofia_reg.c:3210 Can't find user [1023@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1023" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:17.548538 98.90% [WARNING] sofia_reg.c:3210 Can't find user [1024@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1024" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:20.208482 98.90% [WARNING] sofia_reg.c:3210 Can't find user [1025@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1025" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:20.988549 98.90% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/777788@13.235.45.114 [ac3cf4ab-7b75-4d15-b2d9-febe3c82fbb1]
2026-05-07 07:41:20.988549 98.90% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/777788@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11896)
2026-05-07 07:41:20.988549 98.90% [INFO] sofia.c:10460 sofia/internal/777788@13.235.45.114 receiving invite from 199.127.61.12:60412 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 935070767-1367758124-1273219628
2026-05-07 07:41:20.988549 98.90% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:41:20.988549 98.90% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/777788@13.235.45.114) State NEW
2026-05-07 07:41:20.988549 98.90% [DEBUG] sofia.c:2419 detaching session ac3cf4ab-7b75-4d15-b2d9-febe3c82fbb1
2026-05-07 07:41:21.228634 98.90% [DEBUG] sofia.c:2532 Re-attaching to session ac3cf4ab-7b75-4d15-b2d9-febe3c82fbb1
2026-05-07 07:41:21.248511 98.90% [INFO] sofia.c:10460 sofia/internal/777788@13.235.45.114 receiving invite from 199.127.61.12:60412 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 935070767-1367758124-1273219628
2026-05-07 07:41:21.248511 98.90% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:41:21.248511 98.90% [WARNING] sofia_reg.c:3210 Can't find user [777788@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="777788" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:21.248511 98.90% [NOTICE] sofia.c:2417 Hangup sofia/internal/777788@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:41:21.268525 98.90% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/777788@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11896)
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/777788@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/777788@13.235.45.114) State HANGUP
2026-05-07 07:41:21.268525 98.90% [DEBUG] mod_sofia.c:469 Channel sofia/internal/777788@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:59 sofia/internal/777788@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/777788@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/777788@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/777788@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11896)
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/777788@13.235.45.114) State REPORTING
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:168 sofia/internal/777788@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/777788@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/777788@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_session.c:1744 Session 11896 (sofia/internal/777788@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:41:21.268525 98.90% [NOTICE] switch_core_session.c:1762 Session 11896 (sofia/internal/777788@13.235.45.114) Ended
2026-05-07 07:41:21.268525 98.90% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/777788@13.235.45.114 [CS_DESTROY]
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/777788@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11896)
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/777788@13.235.45.114) State DESTROY
2026-05-07 07:41:21.268525 98.90% [DEBUG] mod_sofia.c:380 sofia/internal/777788@13.235.45.114 SOFIA DESTROY
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:175 sofia/internal/777788@13.235.45.114 Standard DESTROY
2026-05-07 07:41:21.268525 98.90% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/777788@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:41:25.508529 98.87% [WARNING] sofia_reg.c:3210 Can't find user [1026@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1026" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:29.988585 98.93% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/777788@13.235.45.114 [0c2d3d4f-4267-4b8b-b8dd-3ab3ec3eae62]
2026-05-07 07:41:29.988585 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/777788@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11897)
2026-05-07 07:41:29.988585 98.93% [INFO] sofia.c:10460 sofia/internal/777788@13.235.45.114 receiving invite from 199.127.61.12:62654 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 328108106-1014805324-1147139371
2026-05-07 07:41:29.988585 98.93% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:41:29.988585 98.93% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/777788@13.235.45.114) State NEW
2026-05-07 07:41:29.988585 98.93% [DEBUG] sofia.c:2419 detaching session 0c2d3d4f-4267-4b8b-b8dd-3ab3ec3eae62
2026-05-07 07:41:30.228613 98.93% [DEBUG] sofia.c:2532 Re-attaching to session 0c2d3d4f-4267-4b8b-b8dd-3ab3ec3eae62
2026-05-07 07:41:30.248479 98.93% [INFO] sofia.c:10460 sofia/internal/777788@13.235.45.114 receiving invite from 199.127.61.12:62654 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 328108106-1014805324-1147139371
2026-05-07 07:41:30.248479 98.93% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:41:30.248479 98.93% [WARNING] sofia_reg.c:3210 Can't find user [777788@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="777788" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:30.248479 98.93% [NOTICE] sofia.c:2417 Hangup sofia/internal/777788@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:41:30.268529 98.93% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/777788@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11897)
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/777788@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/777788@13.235.45.114) State HANGUP
2026-05-07 07:41:30.268529 98.93% [DEBUG] mod_sofia.c:469 Channel sofia/internal/777788@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:59 sofia/internal/777788@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/777788@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/777788@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/777788@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11897)
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/777788@13.235.45.114) State REPORTING
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:168 sofia/internal/777788@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/777788@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/777788@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_session.c:1744 Session 11897 (sofia/internal/777788@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:41:30.268529 98.93% [NOTICE] switch_core_session.c:1762 Session 11897 (sofia/internal/777788@13.235.45.114) Ended
2026-05-07 07:41:30.268529 98.93% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/777788@13.235.45.114 [CS_DESTROY]
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/777788@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11897)
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/777788@13.235.45.114) State DESTROY
2026-05-07 07:41:30.268529 98.93% [DEBUG] mod_sofia.c:380 sofia/internal/777788@13.235.45.114 SOFIA DESTROY
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:175 sofia/internal/777788@13.235.45.114 Standard DESTROY
2026-05-07 07:41:30.268529 98.93% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/777788@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:41:30.388519 98.93% [WARNING] sofia_reg.c:3210 Can't find user [1027@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1027" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:36.508555 99.00% [WARNING] sofia_reg.c:3210 Can't find user [1028@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1028" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:41.808629 99.00% [WARNING] sofia_reg.c:3210 Can't find user [1029@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1029" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:42.508564 99.00% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/7209@13.235.45.114 [d48ccf84-02d4-4913-bfbe-6d63191241a3]
2026-05-07 07:41:42.508564 99.00% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7209@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11898)
2026-05-07 07:41:42.508564 99.00% [INFO] sofia.c:10460 sofia/internal/7209@13.235.45.114 receiving invite from 199.127.61.12:53427 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 446369248-113448402-1619797045
2026-05-07 07:41:42.508564 99.00% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:41:42.508564 99.00% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/7209@13.235.45.114) State NEW
2026-05-07 07:41:42.508564 99.00% [DEBUG] sofia.c:2419 detaching session d48ccf84-02d4-4913-bfbe-6d63191241a3
2026-05-07 07:41:42.788627 99.00% [DEBUG] sofia.c:2532 Re-attaching to session d48ccf84-02d4-4913-bfbe-6d63191241a3
2026-05-07 07:41:42.788627 99.00% [INFO] sofia.c:10460 sofia/internal/7209@13.235.45.114 receiving invite from 199.127.61.12:53427 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 446369248-113448402-1619797045
2026-05-07 07:41:42.788627 99.00% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:41:42.788627 99.00% [WARNING] sofia_reg.c:3210 Can't find user [7209@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="7209" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:42.788627 99.00% [NOTICE] sofia.c:2417 Hangup sofia/internal/7209@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:41:42.808614 99.00% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7209@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11898)
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/7209@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/7209@13.235.45.114) State HANGUP
2026-05-07 07:41:42.808614 99.00% [DEBUG] mod_sofia.c:469 Channel sofia/internal/7209@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:59 sofia/internal/7209@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/7209@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/7209@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7209@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11898)
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/7209@13.235.45.114) State REPORTING
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:168 sofia/internal/7209@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/7209@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/7209@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_session.c:1744 Session 11898 (sofia/internal/7209@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:41:42.808614 99.00% [NOTICE] switch_core_session.c:1762 Session 11898 (sofia/internal/7209@13.235.45.114) Ended
2026-05-07 07:41:42.808614 99.00% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/7209@13.235.45.114 [CS_DESTROY]
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/7209@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11898)
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/7209@13.235.45.114) State DESTROY
2026-05-07 07:41:42.808614 99.00% [DEBUG] mod_sofia.c:380 sofia/internal/7209@13.235.45.114 SOFIA DESTROY
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:175 sofia/internal/7209@13.235.45.114 Standard DESTROY
2026-05-07 07:41:42.808614 99.00% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/7209@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:41:47.868518 98.93% [WARNING] sofia_reg.c:3210 Can't find user [1096@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1096" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:51.228553 98.93% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/7209@13.235.45.114 [37e82d34-74ed-4a5b-acb7-6a60af2652d5]
2026-05-07 07:41:51.228553 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7209@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11899)
2026-05-07 07:41:51.228553 98.93% [INFO] sofia.c:10460 sofia/internal/7209@13.235.45.114 receiving invite from 199.127.61.12:57051 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1819272831-1267770299-164082049
2026-05-07 07:41:51.228553 98.93% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:41:51.228553 98.93% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/7209@13.235.45.114) State NEW
2026-05-07 07:41:51.228553 98.93% [DEBUG] sofia.c:2419 detaching session 37e82d34-74ed-4a5b-acb7-6a60af2652d5
2026-05-07 07:41:51.468584 98.93% [DEBUG] sofia.c:2532 Re-attaching to session 37e82d34-74ed-4a5b-acb7-6a60af2652d5
2026-05-07 07:41:51.488833 98.93% [INFO] sofia.c:10460 sofia/internal/7209@13.235.45.114 receiving invite from 199.127.61.12:57051 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1819272831-1267770299-164082049
2026-05-07 07:41:51.488833 98.93% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:41:51.488833 98.93% [WARNING] sofia_reg.c:3210 Can't find user [7209@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="7209" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:51.488833 98.93% [NOTICE] sofia.c:2417 Hangup sofia/internal/7209@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7209@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11899)
2026-05-07 07:41:51.488833 98.93% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/7209@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/7209@13.235.45.114) State HANGUP
2026-05-07 07:41:51.488833 98.93% [DEBUG] mod_sofia.c:469 Channel sofia/internal/7209@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:59 sofia/internal/7209@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/7209@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/7209@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7209@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11899)
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/7209@13.235.45.114) State REPORTING
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:168 sofia/internal/7209@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/7209@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/7209@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_session.c:1744 Session 11899 (sofia/internal/7209@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:41:51.488833 98.93% [NOTICE] switch_core_session.c:1762 Session 11899 (sofia/internal/7209@13.235.45.114) Ended
2026-05-07 07:41:51.488833 98.93% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/7209@13.235.45.114 [CS_DESTROY]
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/7209@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11899)
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/7209@13.235.45.114) State DESTROY
2026-05-07 07:41:51.488833 98.93% [DEBUG] mod_sofia.c:380 sofia/internal/7209@13.235.45.114 SOFIA DESTROY
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:175 sofia/internal/7209@13.235.45.114 Standard DESTROY
2026-05-07 07:41:51.488833 98.93% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/7209@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:41:52.268657 98.93% [WARNING] sofia_reg.c:3210 Can't find user [1097@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1097" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:56.808557 98.93% [WARNING] sofia_reg.c:3210 Can't find user [1098@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1098" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:41:59.808602 98.93% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/7209@13.235.45.114 [4e5fa4c8-1d8e-4164-9ddc-640e90e13d98]
2026-05-07 07:41:59.808602 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7209@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11900)
2026-05-07 07:41:59.808602 98.93% [INFO] sofia.c:10460 sofia/internal/7209@13.235.45.114 receiving invite from 199.127.61.12:58700 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 54578067-449313809-582395166
2026-05-07 07:41:59.808602 98.93% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:41:59.808602 98.93% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/7209@13.235.45.114) State NEW
2026-05-07 07:41:59.808602 98.93% [DEBUG] sofia.c:2419 detaching session 4e5fa4c8-1d8e-4164-9ddc-640e90e13d98
2026-05-07 07:42:00.068648 98.93% [DEBUG] sofia.c:2532 Re-attaching to session 4e5fa4c8-1d8e-4164-9ddc-640e90e13d98
2026-05-07 07:42:00.088607 98.93% [INFO] sofia.c:10460 sofia/internal/7209@13.235.45.114 receiving invite from 199.127.61.12:58700 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 54578067-449313809-582395166
2026-05-07 07:42:00.088607 98.93% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:42:00.088607 98.93% [WARNING] sofia_reg.c:3210 Can't find user [7209@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="7209" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:00.088607 98.93% [NOTICE] sofia.c:2417 Hangup sofia/internal/7209@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:42:00.108885 98.93% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7209@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11900)
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/7209@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/7209@13.235.45.114) State HANGUP
2026-05-07 07:42:00.108885 98.93% [DEBUG] mod_sofia.c:469 Channel sofia/internal/7209@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:59 sofia/internal/7209@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/7209@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/7209@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/7209@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11900)
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/7209@13.235.45.114) State REPORTING
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:168 sofia/internal/7209@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/7209@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/7209@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_session.c:1744 Session 11900 (sofia/internal/7209@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:42:00.108885 98.93% [NOTICE] switch_core_session.c:1762 Session 11900 (sofia/internal/7209@13.235.45.114) Ended
2026-05-07 07:42:00.108885 98.93% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/7209@13.235.45.114 [CS_DESTROY]
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/7209@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11900)
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/7209@13.235.45.114) State DESTROY
2026-05-07 07:42:00.108885 98.93% [DEBUG] mod_sofia.c:380 sofia/internal/7209@13.235.45.114 SOFIA DESTROY
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:175 sofia/internal/7209@13.235.45.114 Standard DESTROY
2026-05-07 07:42:00.108885 98.93% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/7209@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:42:02.308502 98.80% [WARNING] sofia_reg.c:3210 Can't find user [1099@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1099" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:06.268570 98.73% [WARNING] sofia_reg.c:3210 Can't find user [100@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="100" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:10.268561 98.77% [WARNING] sofia_reg.c:3210 Can't find user [101@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="101" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:13.188579 98.73% [WARNING] sofia_reg.c:3210 Can't find user [102@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="102" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:14.068496 98.77% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/3908@13.235.45.114 [8668ae52-2d55-4392-9358-ac383dad4f54]
2026-05-07 07:42:14.068496 98.77% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/3908@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11901)
2026-05-07 07:42:14.068496 98.77% [INFO] sofia.c:10460 sofia/internal/3908@13.235.45.114 receiving invite from 199.127.61.12:64772 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 351300966-908276116-319886810
2026-05-07 07:42:14.068496 98.77% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:42:14.068496 98.77% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/3908@13.235.45.114) State NEW
2026-05-07 07:42:14.068496 98.77% [DEBUG] sofia.c:2419 detaching session 8668ae52-2d55-4392-9358-ac383dad4f54
2026-05-07 07:42:14.308589 98.77% [DEBUG] sofia.c:2532 Re-attaching to session 8668ae52-2d55-4392-9358-ac383dad4f54
2026-05-07 07:42:14.328555 98.77% [INFO] sofia.c:10460 sofia/internal/3908@13.235.45.114 receiving invite from 199.127.61.12:64772 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 351300966-908276116-319886810
2026-05-07 07:42:14.328555 98.77% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:42:14.328555 98.77% [WARNING] sofia_reg.c:3210 Can't find user [3908@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="3908" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:14.328555 98.77% [NOTICE] sofia.c:2417 Hangup sofia/internal/3908@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:42:14.348533 98.77% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/3908@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11901)
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/3908@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/3908@13.235.45.114) State HANGUP
2026-05-07 07:42:14.348533 98.77% [DEBUG] mod_sofia.c:469 Channel sofia/internal/3908@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:59 sofia/internal/3908@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/3908@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/3908@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/3908@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11901)
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/3908@13.235.45.114) State REPORTING
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:168 sofia/internal/3908@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/3908@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/3908@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_session.c:1744 Session 11901 (sofia/internal/3908@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:42:14.348533 98.77% [NOTICE] switch_core_session.c:1762 Session 11901 (sofia/internal/3908@13.235.45.114) Ended
2026-05-07 07:42:14.348533 98.77% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/3908@13.235.45.114 [CS_DESTROY]
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/3908@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11901)
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/3908@13.235.45.114) State DESTROY
2026-05-07 07:42:14.348533 98.77% [DEBUG] mod_sofia.c:380 sofia/internal/3908@13.235.45.114 SOFIA DESTROY
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:175 sofia/internal/3908@13.235.45.114 Standard DESTROY
2026-05-07 07:42:14.348533 98.77% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/3908@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:42:18.608701 98.80% [WARNING] sofia_reg.c:3210 Can't find user [103@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="103" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:22.488481 98.80% [NOTICE] sofia.c:1065 Hangup sofia/internal/1000@13.235.45.114 [CS_EXECUTE] [NORMAL_CLEARING]
2026-05-07 07:42:22.488481 98.80% [DEBUG] mod_audio_stream.c:151 mod_audio_stream cmd: f4d2cb35-75ae-4399-b838-1707c9fb0186 stop
2026-05-07 07:42:22.488481 98.80% [ERR] mod_audio_stream.c:233 Error locating session f4d2cb35-75ae-4399-b838-1707c9fb0186
2026-05-07 07:42:22.488481 98.80% [INFO] switch_cpp.cpp:1466 === PIPECAT AGENT ENDED ===
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_cpp.cpp:1210 sofia/internal/1000@13.235.45.114 destroy/unlink session from object
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_session.c:2979 sofia/internal/1000@13.235.45.114 skip receive message [APPLICATION_EXEC_COMPLETE] (channel is hungup already)
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:647 (sofia/internal/1000@13.235.45.114) State EXECUTE going to sleep
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 11901)
2026-05-07 07:42:22.488481 98.80% [INFO] mod_audio_stream.c:34 Got SWITCH_ABC_TYPE_CLOSE.
2026-05-07 07:42:22.488481 98.80% [DEBUG] audio_streamer_glue.cpp:889 (f4d2cb35-75ae-4399-b838-1707c9fb0186) stream_session_cleanup
2026-05-07 07:42:22.488481 98.80% [DEBUG] audio_streamer_glue.cpp:41 disconnecting...
2026-05-07 07:42:22.488481 98.80% [INFO] audio_streamer_glue.cpp:502 f4d2cb35-75ae-4399-b838-1707c9fb0186 destroy_tech_pvt
2026-05-07 07:42:22.488481 98.80% [INFO] audio_streamer_glue.cpp:921 (f4d2cb35-75ae-4399-b838-1707c9fb0186) stream_session_cleanup: connection closed
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_media_bug.c:1326 Removing BUG from sofia/internal/1000@13.235.45.114
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/1000@13.235.45.114) Callstate Change ACTIVE -> HANGUP
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/1000@13.235.45.114) State HANGUP
2026-05-07 07:42:22.488481 98.80% [DEBUG] mod_sofia.c:469 Channel sofia/internal/1000@13.235.45.114 hanging up, cause: NORMAL_CLEARING
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:59 sofia/internal/1000@13.235.45.114 Standard HANGUP, cause: NORMAL_CLEARING
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/1000@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/1000@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 11901)
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/1000@13.235.45.114) State REPORTING
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:168 sofia/internal/1000@13.235.45.114 Standard REPORTING, cause: NORMAL_CLEARING
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/1000@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/1000@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_session.c:1744 Session 11890 (sofia/internal/1000@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:42:22.488481 98.80% [NOTICE] switch_core_session.c:1762 Session 11890 (sofia/internal/1000@13.235.45.114) Ended
2026-05-07 07:42:22.488481 98.80% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/1000@13.235.45.114 [CS_DESTROY]
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/1000@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 11901)
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1000@13.235.45.114) State DESTROY
2026-05-07 07:42:22.488481 98.80% [DEBUG] mod_sofia.c:380 sofia/internal/1000@13.235.45.114 SOFIA DESTROY
2026-05-07 07:42:22.488481 98.80% [DEBUG] mod_opus.c:735 Opus decoder stats: Frames[0] PLC[0] FEC[0]
2026-05-07 07:42:22.488481 98.80% [DEBUG] mod_opus.c:750 Opus encoder stats: Frames[0] Bytes encoded[0] Encoded length ms[0] Average encoded bitrate bps[0]
2026-05-07 07:42:22.488481 98.80% [DEBUG] mod_opus.c:735 Opus decoder stats: Frames[0] PLC[0] FEC[0]
2026-05-07 07:42:22.488481 98.80% [DEBUG] mod_opus.c:750 Opus encoder stats: Frames[0] Bytes encoded[0] Encoded length ms[0] Average encoded bitrate bps[0]
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:175 sofia/internal/1000@13.235.45.114 Standard DESTROY
2026-05-07 07:42:22.488481 98.80% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1000@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:42:23.348460 98.77% [WARNING] sofia_reg.c:3210 Can't find user [104@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="104" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:23.568558 98.77% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/3908@13.235.45.114 [9e094c08-39ce-47ba-8464-85fcd15f3d7d]
2026-05-07 07:42:23.568558 98.77% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/3908@13.235.45.114) Running State Change CS_NEW (Cur 1 Tot 11902)
2026-05-07 07:42:23.568558 98.77% [INFO] sofia.c:10460 sofia/internal/3908@13.235.45.114 receiving invite from 199.127.61.12:52071 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 483185643-249574701-448523539
2026-05-07 07:42:23.568558 98.77% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:42:23.568558 98.77% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/3908@13.235.45.114) State NEW
2026-05-07 07:42:23.568558 98.77% [DEBUG] sofia.c:2419 detaching session 9e094c08-39ce-47ba-8464-85fcd15f3d7d
2026-05-07 07:42:23.808457 98.77% [DEBUG] sofia.c:2532 Re-attaching to session 9e094c08-39ce-47ba-8464-85fcd15f3d7d
2026-05-07 07:42:23.828470 98.77% [INFO] sofia.c:10460 sofia/internal/3908@13.235.45.114 receiving invite from 199.127.61.12:52071 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 483185643-249574701-448523539
2026-05-07 07:42:23.828470 98.77% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:42:23.828470 98.77% [WARNING] sofia_reg.c:3210 Can't find user [3908@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="3908" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:23.828470 98.77% [NOTICE] sofia.c:2417 Hangup sofia/internal/3908@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:42:23.848458 98.77% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/3908@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 11902)
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/3908@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/3908@13.235.45.114) State HANGUP
2026-05-07 07:42:23.848458 98.77% [DEBUG] mod_sofia.c:469 Channel sofia/internal/3908@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:59 sofia/internal/3908@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/3908@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/3908@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/3908@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 11902)
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/3908@13.235.45.114) State REPORTING
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:168 sofia/internal/3908@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/3908@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/3908@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_session.c:1744 Session 11902 (sofia/internal/3908@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:42:23.848458 98.77% [NOTICE] switch_core_session.c:1762 Session 11902 (sofia/internal/3908@13.235.45.114) Ended
2026-05-07 07:42:23.848458 98.77% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/3908@13.235.45.114 [CS_DESTROY]
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/3908@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 11902)
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/3908@13.235.45.114) State DESTROY
2026-05-07 07:42:23.848458 98.77% [DEBUG] mod_sofia.c:380 sofia/internal/3908@13.235.45.114 SOFIA DESTROY
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:175 sofia/internal/3908@13.235.45.114 Standard DESTROY
2026-05-07 07:42:23.848458 98.77% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/3908@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:42:27.128678 98.77% [WARNING] sofia_reg.c:3210 Can't find user [105@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="105" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:31.168619 98.90% [WARNING] sofia_reg.c:3210 Can't find user [106@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="106" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:32.648636 98.93% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/3908@13.235.45.114 [6d1f49d9-f7fb-4cb8-a90e-cb2c381ceb38]
2026-05-07 07:42:32.648636 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/3908@13.235.45.114) Running State Change CS_NEW (Cur 1 Tot 11903)
2026-05-07 07:42:32.648636 98.93% [INFO] sofia.c:10460 sofia/internal/3908@13.235.45.114 receiving invite from 199.127.61.12:54813 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1044735469-1985989533-1032777189
2026-05-07 07:42:32.648636 98.93% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:42:32.648636 98.93% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/3908@13.235.45.114) State NEW
2026-05-07 07:42:32.648636 98.93% [DEBUG] sofia.c:2419 detaching session 6d1f49d9-f7fb-4cb8-a90e-cb2c381ceb38
2026-05-07 07:42:32.908563 98.97% [DEBUG] sofia.c:2532 Re-attaching to session 6d1f49d9-f7fb-4cb8-a90e-cb2c381ceb38
2026-05-07 07:42:32.908563 98.97% [INFO] sofia.c:10460 sofia/internal/3908@13.235.45.114 receiving invite from 199.127.61.12:54813 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1044735469-1985989533-1032777189
2026-05-07 07:42:32.908563 98.97% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:42:32.908563 98.97% [WARNING] sofia_reg.c:3210 Can't find user [3908@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="3908" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:32.908563 98.97% [NOTICE] sofia.c:2417 Hangup sofia/internal/3908@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:42:32.928636 98.97% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/3908@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 11903)
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/3908@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/3908@13.235.45.114) State HANGUP
2026-05-07 07:42:32.928636 98.97% [DEBUG] mod_sofia.c:469 Channel sofia/internal/3908@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:59 sofia/internal/3908@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/3908@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/3908@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/3908@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 11903)
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/3908@13.235.45.114) State REPORTING
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:168 sofia/internal/3908@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/3908@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/3908@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_session.c:1744 Session 11903 (sofia/internal/3908@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:42:32.928636 98.97% [NOTICE] switch_core_session.c:1762 Session 11903 (sofia/internal/3908@13.235.45.114) Ended
2026-05-07 07:42:32.928636 98.97% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/3908@13.235.45.114 [CS_DESTROY]
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/3908@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 11903)
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/3908@13.235.45.114) State DESTROY
2026-05-07 07:42:32.928636 98.97% [DEBUG] mod_sofia.c:380 sofia/internal/3908@13.235.45.114 SOFIA DESTROY
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:175 sofia/internal/3908@13.235.45.114 Standard DESTROY
2026-05-07 07:42:32.928636 98.97% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/3908@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:42:33.188776 98.97% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/9110111323545114@13.235.45.114 [5137bf15-6a61-4937-ba04-a19c032c457f]
2026-05-07 07:42:33.188776 98.97% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/9110111323545114@13.235.45.114) Running State Change CS_NEW (Cur 1 Tot 11904)
2026-05-07 07:42:33.188776 98.97% [INFO] sofia.c:10460 sofia/internal/9110111323545114@13.235.45.114 receiving invite from 5.196.63.60:56340 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 60546054-133662437-551859887
2026-05-07 07:42:33.188776 98.97% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 5.196.63.60:0.
2026-05-07 07:42:33.188776 98.97% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/9110111323545114@13.235.45.114) State NEW
2026-05-07 07:42:33.188776 98.97% [DEBUG] sofia.c:2419 detaching session 5137bf15-6a61-4937-ba04-a19c032c457f
2026-05-07 07:42:35.208471 99.00% [WARNING] sofia_reg.c:3210 Can't find user [107@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="107" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:39.108585 98.93% [WARNING] sofia_reg.c:3210 Can't find user [108@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="108" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:43.108586 98.97% [WARNING] sofia_reg.c:3210 Can't find user [109@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="109" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:43.228571 98.97% [WARNING] switch_core_state_machine.c:684 5137bf15-6a61-4937-ba04-a19c032c457f sofia/internal/9110111323545114@13.235.45.114 Abandoned
2026-05-07 07:42:43.228571 98.97% [NOTICE] switch_core_state_machine.c:687 Hangup sofia/internal/9110111323545114@13.235.45.114 [CS_NEW] [WRONG_CALL_STATE]
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/9110111323545114@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 11904)
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/9110111323545114@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/9110111323545114@13.235.45.114) State HANGUP
2026-05-07 07:42:43.228571 98.97% [DEBUG] mod_sofia.c:469 Channel sofia/internal/9110111323545114@13.235.45.114 hanging up, cause: WRONG_CALL_STATE
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:59 sofia/internal/9110111323545114@13.235.45.114 Standard HANGUP, cause: WRONG_CALL_STATE
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/9110111323545114@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/9110111323545114@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/9110111323545114@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 11904)
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/9110111323545114@13.235.45.114) State REPORTING
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:168 sofia/internal/9110111323545114@13.235.45.114 Standard REPORTING, cause: WRONG_CALL_STATE
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/9110111323545114@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/9110111323545114@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_session.c:1744 Session 11904 (sofia/internal/9110111323545114@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:42:43.228571 98.97% [NOTICE] switch_core_session.c:1762 Session 11904 (sofia/internal/9110111323545114@13.235.45.114) Ended
2026-05-07 07:42:43.228571 98.97% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/9110111323545114@13.235.45.114 [CS_DESTROY]
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/9110111323545114@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 11904)
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/9110111323545114@13.235.45.114) State DESTROY
2026-05-07 07:42:43.228571 98.97% [DEBUG] mod_sofia.c:380 sofia/internal/9110111323545114@13.235.45.114 SOFIA DESTROY
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:175 sofia/internal/9110111323545114@13.235.45.114 Standard DESTROY
2026-05-07 07:42:43.228571 98.97% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/9110111323545114@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:42:45.048616 98.93% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/18898@13.235.45.114 [4659f331-4b01-4f92-a4fa-03047e16f57f]
2026-05-07 07:42:45.048616 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/18898@13.235.45.114) Running State Change CS_NEW (Cur 1 Tot 11905)
2026-05-07 07:42:45.048616 98.93% [INFO] sofia.c:10460 sofia/internal/18898@13.235.45.114 receiving invite from 199.127.61.12:60573 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1902708720-2055273546-665760462
2026-05-07 07:42:45.048616 98.93% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:42:45.048616 98.93% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/18898@13.235.45.114) State NEW
2026-05-07 07:42:45.048616 98.93% [DEBUG] sofia.c:2419 detaching session 4659f331-4b01-4f92-a4fa-03047e16f57f
2026-05-07 07:42:45.288656 98.93% [DEBUG] sofia.c:2532 Re-attaching to session 4659f331-4b01-4f92-a4fa-03047e16f57f
2026-05-07 07:42:45.308640 98.93% [INFO] sofia.c:10460 sofia/internal/18898@13.235.45.114 receiving invite from 199.127.61.12:60573 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1902708720-2055273546-665760462
2026-05-07 07:42:45.308640 98.93% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:42:45.308640 98.93% [WARNING] sofia_reg.c:3210 Can't find user [18898@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="18898" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:42:45.308640 98.93% [NOTICE] sofia.c:2417 Hangup sofia/internal/18898@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:42:45.328611 98.93% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/18898@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 11905)
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/18898@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/18898@13.235.45.114) State HANGUP
2026-05-07 07:42:45.328611 98.93% [DEBUG] mod_sofia.c:469 Channel sofia/internal/18898@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:59 sofia/internal/18898@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/18898@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/18898@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/18898@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 11905)
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/18898@13.235.45.114) State REPORTING
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:168 sofia/internal/18898@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/18898@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/18898@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_session.c:1744 Session 11905 (sofia/internal/18898@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:42:45.328611 98.93% [NOTICE] switch_core_session.c:1762 Session 11905 (sofia/internal/18898@13.235.45.114) Ended
2026-05-07 07:42:45.328611 98.93% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/18898@13.235.45.114 [CS_DESTROY]
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/18898@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 11905)
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/18898@13.235.45.114) State DESTROY
2026-05-07 07:42:45.328611 98.93% [DEBUG] mod_sofia.c:380 sofia/internal/18898@13.235.45.114 SOFIA DESTROY
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:175 sofia/internal/18898@13.235.45.114 Standard DESTROY
2026-05-07 07:42:45.328611 98.93% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/18898@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:42:46.948631 98.90% [WARNING] sofia_reg.c:3210 Can't find user [110@172.31.38.106] from 5.39.101.60