Type /help <enter> to see a list of commands



+OK log level  [7]
2026-05-07 07:25:59.288578 95.27% [WARNING] sofia_reg.c:3210 Can't find user [110@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="110" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:00.148936 97.00% [WARNING] switch_core_state_machine.c:684 11fc4783-88ad-4c70-839f-59c681a44ba9 sofia/internal/9020111323545114@13.235.45.114 Abandoned
2026-05-07 07:26:00.148936 97.00% [NOTICE] switch_core_state_machine.c:687 Hangup sofia/internal/9020111323545114@13.235.45.114 [CS_NEW] [WRONG_CALL_STATE]
2026-05-07 07:26:00.148936 97.00% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/9020111323545114@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 11794)
2026-05-07 07:26:00.148936 97.00% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/9020111323545114@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:26:00.148936 97.00% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/9020111323545114@13.235.45.114) State HANGUP
2026-05-07 07:26:00.148936 97.00% [DEBUG] mod_sofia.c:469 Channel sofia/internal/9020111323545114@13.235.45.114 hanging up, cause: WRONG_CALL_STATE
2026-05-07 07:26:00.148936 97.00% [DEBUG] switch_core_state_machine.c:59 sofia/internal/9020111323545114@13.235.45.114 Standard HANGUP, cause: WRONG_CALL_STATE
2026-05-07 07:26:00.148936 97.00% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/9020111323545114@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:26:00.148936 97.00% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/9020111323545114@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:26:00.148936 97.00% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/9020111323545114@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 11794)
2026-05-07 07:26:00.148936 97.00% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/9020111323545114@13.235.45.114) State REPORTING
2026-05-07 07:26:00.148936 97.00% [DEBUG] switch_core_state_machine.c:168 sofia/internal/9020111323545114@13.235.45.114 Standard REPORTING, cause: WRONG_CALL_STATE
2026-05-07 07:26:00.148936 97.00% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/9020111323545114@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:26:00.168787 97.00% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/9020111323545114@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:26:00.168787 97.00% [DEBUG] switch_core_session.c:1744 Session 11793 (sofia/internal/9020111323545114@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:26:00.168787 97.00% [NOTICE] switch_core_session.c:1762 Session 11793 (sofia/internal/9020111323545114@13.235.45.114) Ended
2026-05-07 07:26:00.168787 97.00% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/9020111323545114@13.235.45.114 [CS_DESTROY]
2026-05-07 07:26:00.168787 97.00% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/9020111323545114@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 11794)
2026-05-07 07:26:00.168787 97.00% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/9020111323545114@13.235.45.114) State DESTROY
2026-05-07 07:26:00.168787 97.00% [DEBUG] mod_sofia.c:380 sofia/internal/9020111323545114@13.235.45.114 SOFIA DESTROY
2026-05-07 07:26:00.168787 97.00% [DEBUG] switch_core_state_machine.c:175 sofia/internal/9020111323545114@13.235.45.114 Standard DESTROY
2026-05-07 07:26:00.168787 97.00% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/9020111323545114@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:26:02.128563 98.87% [WARNING] sofia_reg.c:3210 Can't find user [102@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="102" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:05.568624 98.83% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/4600@13.235.45.114 [d9a1112d-688e-4e5e-9e14-1c642fd3f71b]
2026-05-07 07:26:05.568624 98.83% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/4600@13.235.45.114) Running State Change CS_NEW (Cur 1 Tot 11795)
2026-05-07 07:26:05.568624 98.83% [INFO] sofia.c:10460 sofia/internal/4600@13.235.45.114 receiving invite from 199.127.61.12:58781 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 91992751-1773451447-399178682
2026-05-07 07:26:05.568624 98.83% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:26:05.568624 98.83% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/4600@13.235.45.114) State NEW
2026-05-07 07:26:05.568624 98.83% [DEBUG] sofia.c:2419 detaching session d9a1112d-688e-4e5e-9e14-1c642fd3f71b
2026-05-07 07:26:05.808605 98.83% [DEBUG] sofia.c:2532 Re-attaching to session d9a1112d-688e-4e5e-9e14-1c642fd3f71b
2026-05-07 07:26:05.828602 98.83% [INFO] sofia.c:10460 sofia/internal/4600@13.235.45.114 receiving invite from 199.127.61.12:58781 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 91992751-1773451447-399178682
2026-05-07 07:26:05.828602 98.83% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:26:05.828602 98.83% [WARNING] sofia_reg.c:3210 Can't find user [4600@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="4600" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:05.828602 98.83% [NOTICE] sofia.c:2417 Hangup sofia/internal/4600@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:26:05.848458 98.83% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/4600@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 11795)
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/4600@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/4600@13.235.45.114) State HANGUP
2026-05-07 07:26:05.848458 98.83% [DEBUG] mod_sofia.c:469 Channel sofia/internal/4600@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:59 sofia/internal/4600@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/4600@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/4600@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/4600@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 11795)
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/4600@13.235.45.114) State REPORTING
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:168 sofia/internal/4600@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/4600@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/4600@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_session.c:1744 Session 11795 (sofia/internal/4600@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:26:05.848458 98.83% [NOTICE] switch_core_session.c:1762 Session 11795 (sofia/internal/4600@13.235.45.114) Ended
2026-05-07 07:26:05.848458 98.83% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/4600@13.235.45.114 [CS_DESTROY]
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/4600@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 11795)
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/4600@13.235.45.114) State DESTROY
2026-05-07 07:26:05.848458 98.83% [DEBUG] mod_sofia.c:380 sofia/internal/4600@13.235.45.114 SOFIA DESTROY
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:175 sofia/internal/4600@13.235.45.114 Standard DESTROY
2026-05-07 07:26:05.848458 98.83% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/4600@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:26:05.908656 98.83% [WARNING] sofia_reg.c:3210 Can't find user [103@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="103" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:07.468546 98.80% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/1000@13.235.45.114 [d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4]
2026-05-07 07:26:07.468546 98.80% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_NEW (Cur 1 Tot 11796)
2026-05-07 07:26:07.468546 98.80% [INFO] sofia.c:10460 sofia/internal/1000@13.235.45.114 receiving invite from 86.107.100.98:58213 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: FNc8XM4r8a
2026-05-07 07:26:07.468546 98.80% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 86.107.100.98:0.
2026-05-07 07:26:07.468546 98.80% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/1000@13.235.45.114) State NEW
2026-05-07 07:26:07.468546 98.80% [DEBUG] sofia.c:2419 detaching session d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4
2026-05-07 07:26:07.548624 98.80% [DEBUG] sofia.c:2532 Re-attaching to session d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4
2026-05-07 07:26:07.548624 98.80% [INFO] sofia.c:10460 sofia/internal/1000@13.235.45.114 receiving invite from 86.107.100.98:58213 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: FNc8XM4r8a
2026-05-07 07:26:07.548624 98.80% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 86.107.100.98:0.
2026-05-07 07:26:07.548624 98.80% [DEBUG] sofia.c:7493 Channel sofia/internal/1000@13.235.45.114 entering state [received][100]
2026-05-07 07:26:07.548624 98.80% [DEBUG] sofia.c:7503 Remote SDP:
v=0
o=1000 3154 2204 IN IP4 86.107.100.98
s=Talk
c=IN IP4 86.107.100.98
t=0 0
a=rtcp-xr:rcvr-rtt=all:10000 stat-summary=loss,dup,jitt,TTL voip-metrics
a=record:off
m=audio 60109 RTP/AVP 96 97 98 0 8 18 101 99 100
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
a=rtcp:41059
a=rtcp-fb:* trr-int 1000
a=rtcp-fb:* ccm tmmbr

2026-05-07 07:26:07.548624 98.80% [DEBUG] sofia.c:7906 (sofia/internal/1000@13.235.45.114) State Change CS_NEW -> CS_INIT
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_INIT (Cur 1 Tot 11796)
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:624 (sofia/internal/1000@13.235.45.114) State INIT
2026-05-07 07:26:07.548624 98.80% [DEBUG] mod_sofia.c:97 sofia/internal/1000@13.235.45.114 SOFIA INIT
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:40 sofia/internal/1000@13.235.45.114 Standard INIT
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:48 (sofia/internal/1000@13.235.45.114) State Change CS_INIT -> CS_ROUTING
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:624 (sofia/internal/1000@13.235.45.114) State INIT going to sleep
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_ROUTING (Cur 1 Tot 11796)
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_channel.c:2399 (sofia/internal/1000@13.235.45.114) Callstate Change DOWN -> RINGING
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:640 (sofia/internal/1000@13.235.45.114) State ROUTING
2026-05-07 07:26:07.548624 98.80% [DEBUG] mod_sofia.c:158 sofia/internal/1000@13.235.45.114 SOFIA ROUTING
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:230 sofia/internal/1000@13.235.45.114 Standard ROUTING
2026-05-07 07:26:07.548624 98.80% [INFO] mod_dialplan_xml.c:639 Processing 1000 <1000>->7007 in context default
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
o=1000 3154 2204 IN IP4 86.107.100.98
s=Talk
c=IN IP4 86.107.100.98
t=0 0
a=rtcp-xr:rcvr-rtt=all:10000 stat-summary=loss,dup,jitt,TTL voip-metrics
a=record:off
m=audio 60109 RTP/AVP 96 97 98 0 8 18 101 99 100
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
a=rtcp:41059
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
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:281 (sofia/internal/1000@13.235.45.114) State Change CS_ROUTING -> CS_EXECUTE
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:640 (sofia/internal/1000@13.235.45.114) State ROUTING going to sleep
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_EXECUTE (Cur 1 Tot 11796)
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:647 (sofia/internal/1000@13.235.45.114) State EXECUTE
2026-05-07 07:26:07.548624 98.80% [DEBUG] mod_sofia.c:213 sofia/internal/1000@13.235.45.114 SOFIA EXECUTE
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_state_machine.c:323 sofia/internal/1000@13.235.45.114 Standard EXECUTE
EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 hash(insert/172.31.38.106-spymap/1000/d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4)
EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 hash(insert/172.31.38.106-last_dial/1000/7007)
EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 hash(insert/172.31.38.106-last_dial/global/d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4)
EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 export(RFC2822_DATE=Thu, 07 May 2026 07:26:07 +0000)
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_channel.c:1334 EXPORT (export_vars) [RFC2822_DATE]=[Thu, 07 May 2026 07:26:07 +0000]
EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 lua(pipecat.lua)
2026-05-07 07:26:07.548624 98.80% [INFO] switch_cpp.cpp:1466 === PIPECAT AGENT STARTED uuid=d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4 ===
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [opus:96:48000:20:0:1]/[opus:116:48000:20:0:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5588 Audio Codec Compare [opus:116:48000:20:0:1] ++++ is saved as a match
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [opus:96:48000:20:0:1]/[PCMU:0:8000:20:64000:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [opus:96:48000:20:0:1]/[PCMA:8:8000:20:64000:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:97:16000:20:0:1]/[opus:116:48000:20:0:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:97:16000:20:0:1]/[PCMU:0:8000:20:64000:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:97:16000:20:0:1]/[PCMA:8:8000:20:64000:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:98:8000:20:0:1]/[opus:116:48000:20:0:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:98:8000:20:0:1]/[PCMU:0:8000:20:64000:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:98:8000:20:0:1]/[PCMA:8:8000:20:64000:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMU:0:8000:20:64000:1]/[opus:116:48000:20:0:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMU:0:8000:20:64000:1]/[PCMU:0:8000:20:64000:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5588 Audio Codec Compare [PCMU:0:8000:20:64000:1] ++++ is saved as a match
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMU:0:8000:20:64000:1]/[PCMA:8:8000:20:64000:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMA:8:8000:20:64000:1]/[opus:116:48000:20:0:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMA:8:8000:20:64000:1]/[PCMU:0:8000:20:64000:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMA:8:8000:20:64000:1]/[PCMA:8:8000:20:64000:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5588 Audio Codec Compare [PCMA:8:8000:20:64000:1] ++++ is saved as a match
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [G729:18:8000:20:8000:1]/[opus:116:48000:20:0:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [G729:18:8000:20:8000:1]/[PCMU:0:8000:20:64000:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [G729:18:8000:20:8000:1]/[PCMA:8:8000:20:64000:1]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5438 Set telephone-event payload to 101@48000
2026-05-07 07:26:07.548624 98.80% [DEBUG] mod_opus.c:629 Opus encoder: set bitrate to local settings [72000bps]
2026-05-07 07:26:07.548624 98.80% [DEBUG] mod_opus.c:629 Opus encoder: set bitrate to local settings [72000bps]
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:3731 Set Codec sofia/internal/1000@13.235.45.114 opus/48000 20 ms 960 samples 0 bits 1 channels
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_codec.c:111 sofia/internal/1000@13.235.45.114 Original read codec set to opus:116
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5798 Set telephone-event payload to 101@48000
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:5856 sofia/internal/1000@13.235.45.114 Set 2833 dtmf send payload to 101 recv payload to 101
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:8660 AUDIO RTP [sofia/internal/1000@13.235.45.114] 172.31.38.106 port 18528 -> 86.107.100.98 port 60109 codec: 96 ms: 20
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_rtp.c:4566 Starting timer [soft] 960 bytes per 20ms
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:8881 Activating RTCP PORT 41059
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_rtp.c:4898 RTCP send rate is: 1000 and packet rate is: 20000 Remote Port: 41059
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_rtp.c:2692 Setting RTCP remote addr to 86.107.100.98:41059 2
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:8973 sofia/internal/1000@13.235.45.114 Set 2833 dtmf send payload to 101
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:8980 sofia/internal/1000@13.235.45.114 Set 2833 dtmf receive payload to 101
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:9003 sofia/internal/1000@13.235.45.114 Set rtp dtmf delay to 40
2026-05-07 07:26:07.548624 98.80% [NOTICE] sofia_media.c:90 Pre-Answer sofia/internal/1000@13.235.45.114!
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_channel.c:3585 (sofia/internal/1000@13.235.45.114) Callstate Change RINGING -> EARLY
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_core_media.c:8642 Audio params are unchanged for sofia/internal/1000@13.235.45.114.
2026-05-07 07:26:07.548624 98.80% [DEBUG] mod_sofia.c:914 Local SDP sofia/internal/1000@13.235.45.114:
v=0
o=FreeSWITCH 1778120239 1778120240 IN IP4 13.235.45.114
s=FreeSWITCH
c=IN IP4 13.235.45.114
t=0 0
m=audio 18528 RTP/AVP 96 101
a=rtpmap:96 opus/48000/2
a=fmtp:96 useinbandfec=1
a=rtpmap:101 telephone-event/48000
a=fmtp:101 0-15
a=ptime:20
a=sendrecv
a=rtcp:18529 IN IP4 13.235.45.114

2026-05-07 07:26:07.548624 98.80% [NOTICE] switch_cpp.cpp:704 Channel [sofia/internal/1000@13.235.45.114] has been answered
2026-05-07 07:26:07.548624 98.80% [DEBUG] switch_channel.c:3912 (sofia/internal/1000@13.235.45.114) Callstate Change EARLY -> ACTIVE
2026-05-07 07:26:07.548624 98.80% [DEBUG] sofia.c:7493 Channel sofia/internal/1000@13.235.45.114 entering state [completed][200]
2026-05-07 07:26:07.948551 98.77% [DEBUG] switch_rtp.c:7128 Correct audio RTCP ip/port confirmed.
2026-05-07 07:26:07.968641 98.77% [DEBUG] sofia.c:7493 Channel sofia/internal/1000@13.235.45.114 entering state [ready][200]
2026-05-07 07:26:08.048629 98.77% [INFO] switch_cpp.cpp:1466 Sending: uuid_audio_stream d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4 start ws://127.0.0.1:8765 mono 16000
2026-05-07 07:26:08.048629 98.77% [DEBUG] mod_audio_stream.c:151 mod_audio_stream cmd: d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4 start ws://127.0.0.1:8765 mono 16000
2026-05-07 07:26:08.048629 98.77% [DEBUG] mod_audio_stream.c:82 calling stream_session_init.
2026-05-07 07:26:08.048629 98.77% [DEBUG] audio_streamer_glue.cpp:485 (d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4) resampling from 48000 to 16000
2026-05-07 07:26:08.048629 98.77% [DEBUG] audio_streamer_glue.cpp:496 (d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4) stream_data_init
2026-05-07 07:26:08.048629 98.77% [DEBUG] mod_audio_stream.c:88 adding bug.
2026-05-07 07:26:08.048629 98.77% [DEBUG] switch_core_media_bug.c:976 Attaching BUG to sofia/internal/1000@13.235.45.114
2026-05-07 07:26:08.048629 98.77% [DEBUG] mod_audio_stream.c:92 setting bug private data.
2026-05-07 07:26:08.048629 98.77% [DEBUG] mod_audio_stream.c:95 exiting start_capture.
2026-05-07 07:26:08.048629 98.77% [INFO] switch_cpp.cpp:1466 Result: +OK Success

2026-05-07 07:26:08.128555 98.77% [DEBUG] switch_rtp.c:1934 rtcp_stats_init: audio ssrc[4096831846] base_seq[0]
2026-05-07 07:26:08.128555 98.77% [DEBUG] switch_rtp.c:7698 Correct audio ip/port confirmed.
2026-05-07 07:26:08.128555 98.77% [DEBUG] switch_core_io.c:448 Setting BUG Codec opus:116
2026-05-07 07:26:08.128555 98.77% [DEBUG] mod_opus.c:629 Opus encoder: set bitrate to local settings [72000bps]
2026-05-07 07:26:08.208455 98.77% [WARNING] sofia_reg.c:3210 Can't find user [104@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="104" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:09.808580 97.17% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/'or''='@13.235.45.114 [92f35c33-39e8-4d08-bd16-310253224802]
2026-05-07 07:26:09.808580 97.17% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/'or''='@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11797)
2026-05-07 07:26:09.808580 97.17% [INFO] sofia.c:10460 sofia/internal/'or''='@13.235.45.114 receiving invite from 107.152.36.33:53781 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 749203647-432021227-73991099
2026-05-07 07:26:09.808580 97.17% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 107.152.36.33:0.
2026-05-07 07:26:09.808580 97.17% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/'or''='@13.235.45.114) State NEW
2026-05-07 07:26:09.808580 97.17% [DEBUG] sofia.c:2419 detaching session 92f35c33-39e8-4d08-bd16-310253224802
2026-05-07 07:26:10.068583 97.17% [DEBUG] sofia.c:2532 Re-attaching to session 92f35c33-39e8-4d08-bd16-310253224802
2026-05-07 07:26:10.088614 97.17% [INFO] sofia.c:10460 sofia/internal/'or''='@13.235.45.114 receiving invite from 107.152.36.33:53781 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 749203647-432021227-73991099
2026-05-07 07:26:10.088614 97.17% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 107.152.36.33:0.
2026-05-07 07:26:10.088614 97.17% [WARNING] sofia_reg.c:3210 Can't find user ['or''='@172.31.38.106] from 107.152.36.33
You must define a domain called '172.31.38.106' in your directory and add a user with the id="'or''='" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:10.088614 97.17% [NOTICE] sofia.c:2417 Hangup sofia/internal/'or''='@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:26:10.108594 97.17% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/'or''='@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11797)
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/'or''='@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/'or''='@13.235.45.114) State HANGUP
2026-05-07 07:26:10.108594 97.17% [DEBUG] mod_sofia.c:469 Channel sofia/internal/'or''='@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:59 sofia/internal/'or''='@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/'or''='@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/'or''='@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/'or''='@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11797)
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/'or''='@13.235.45.114) State REPORTING
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:168 sofia/internal/'or''='@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/'or''='@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/'or''='@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_session.c:1744 Session 11797 (sofia/internal/'or''='@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:26:10.108594 97.17% [NOTICE] switch_core_session.c:1762 Session 11797 (sofia/internal/'or''='@13.235.45.114) Ended
2026-05-07 07:26:10.108594 97.17% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/'or''='@13.235.45.114 [CS_DESTROY]
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/'or''='@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11797)
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/'or''='@13.235.45.114) State DESTROY
2026-05-07 07:26:10.108594 97.17% [DEBUG] mod_sofia.c:380 sofia/internal/'or''='@13.235.45.114 SOFIA DESTROY
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:175 sofia/internal/'or''='@13.235.45.114 Standard DESTROY
2026-05-07 07:26:10.108594 97.17% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/'or''='@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:26:11.848604 96.67% [WARNING] sofia_reg.c:3210 Can't find user [105@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="105" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:14.328553 96.20% [WARNING] sofia_reg.c:3210 Can't find user [106@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="106" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:17.668589 95.47% [WARNING] sofia_reg.c:3210 Can't find user [107@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="107" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:17.948601 95.23% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/444446@13.235.45.114 [2dcb6f69-7577-4975-989f-e37c30ce0950]
2026-05-07 07:26:17.948601 95.23% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/444446@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11798)
2026-05-07 07:26:17.948601 95.23% [INFO] sofia.c:10460 sofia/internal/444446@13.235.45.114 receiving invite from 199.127.61.12:50062 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 2136869733-1946061777-781850869
2026-05-07 07:26:17.948601 95.23% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:26:17.948601 95.23% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/444446@13.235.45.114) State NEW
2026-05-07 07:26:17.948601 95.23% [DEBUG] sofia.c:2419 detaching session 2dcb6f69-7577-4975-989f-e37c30ce0950
2026-05-07 07:26:18.228530 95.23% [DEBUG] sofia.c:2532 Re-attaching to session 2dcb6f69-7577-4975-989f-e37c30ce0950
2026-05-07 07:26:18.228530 95.23% [INFO] sofia.c:10460 sofia/internal/444446@13.235.45.114 receiving invite from 199.127.61.12:50062 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 2136869733-1946061777-781850869
2026-05-07 07:26:18.228530 95.23% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:26:18.228530 95.23% [WARNING] sofia_reg.c:3210 Can't find user [444446@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="444446" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:18.228530 95.23% [NOTICE] sofia.c:2417 Hangup sofia/internal/444446@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:26:18.248618 95.23% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/444446@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11798)
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/444446@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/444446@13.235.45.114) State HANGUP
2026-05-07 07:26:18.248618 95.23% [DEBUG] mod_sofia.c:469 Channel sofia/internal/444446@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:59 sofia/internal/444446@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/444446@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/444446@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/444446@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11798)
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/444446@13.235.45.114) State REPORTING
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:168 sofia/internal/444446@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/444446@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/444446@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_session.c:1744 Session 11798 (sofia/internal/444446@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:26:18.248618 95.23% [NOTICE] switch_core_session.c:1762 Session 11798 (sofia/internal/444446@13.235.45.114) Ended
2026-05-07 07:26:18.248618 95.23% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/444446@13.235.45.114 [CS_DESTROY]
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/444446@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11798)
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/444446@13.235.45.114) State DESTROY
2026-05-07 07:26:18.248618 95.23% [DEBUG] mod_sofia.c:380 sofia/internal/444446@13.235.45.114 SOFIA DESTROY
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:175 sofia/internal/444446@13.235.45.114 Standard DESTROY
2026-05-07 07:26:18.248618 95.23% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/444446@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:26:20.368569 94.73% [WARNING] sofia_reg.c:3210 Can't find user [108@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="108" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:23.808597 93.80% [WARNING] sofia_reg.c:3210 Can't find user [100@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="100" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:26.348645 93.30% [WARNING] sofia_reg.c:3210 Can't find user [101@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="101" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:27.548565 93.07% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/444446@13.235.45.114 [17fb4294-8420-4521-891a-099eb8453ea0]
2026-05-07 07:26:27.548565 93.07% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/444446@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11799)
2026-05-07 07:26:27.548565 93.07% [INFO] sofia.c:10460 sofia/internal/444446@13.235.45.114 receiving invite from 199.127.61.12:53729 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1392847420-2054612700-420239451
2026-05-07 07:26:27.548565 93.07% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:26:27.548565 93.07% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/444446@13.235.45.114) State NEW
2026-05-07 07:26:27.548565 93.07% [DEBUG] sofia.c:2419 detaching session 17fb4294-8420-4521-891a-099eb8453ea0
2026-05-07 07:26:27.828601 92.80% [DEBUG] sofia.c:2532 Re-attaching to session 17fb4294-8420-4521-891a-099eb8453ea0
2026-05-07 07:26:27.828601 92.80% [INFO] sofia.c:10460 sofia/internal/444446@13.235.45.114 receiving invite from 199.127.61.12:53729 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1392847420-2054612700-420239451
2026-05-07 07:26:27.828601 92.80% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:26:27.828601 92.80% [WARNING] sofia_reg.c:3210 Can't find user [444446@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="444446" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:27.828601 92.80% [NOTICE] sofia.c:2417 Hangup sofia/internal/444446@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:26:27.848540 92.80% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/444446@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11799)
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/444446@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/444446@13.235.45.114) State HANGUP
2026-05-07 07:26:27.848540 92.80% [DEBUG] mod_sofia.c:469 Channel sofia/internal/444446@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:59 sofia/internal/444446@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/444446@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/444446@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/444446@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11799)
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/444446@13.235.45.114) State REPORTING
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:168 sofia/internal/444446@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/444446@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/444446@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_session.c:1744 Session 11799 (sofia/internal/444446@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:26:27.848540 92.80% [NOTICE] switch_core_session.c:1762 Session 11799 (sofia/internal/444446@13.235.45.114) Ended
2026-05-07 07:26:27.848540 92.80% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/444446@13.235.45.114 [CS_DESTROY]
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/444446@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11799)
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/444446@13.235.45.114) State DESTROY
2026-05-07 07:26:27.848540 92.80% [DEBUG] mod_sofia.c:380 sofia/internal/444446@13.235.45.114 SOFIA DESTROY
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:175 sofia/internal/444446@13.235.45.114 Standard DESTROY
2026-05-07 07:26:27.848540 92.80% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/444446@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:26:29.928528 92.30% [WARNING] sofia_reg.c:3210 Can't find user [102@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="102" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:33.868581 91.37% [WARNING] sofia_reg.c:3210 Can't find user [103@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="103" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:36.688626 90.70% [WARNING] sofia_reg.c:3210 Can't find user [104@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="104" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:37.028624 90.43% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/444446@13.235.45.114 [01b90c91-b8d9-4453-963a-b35a831d49d9]
2026-05-07 07:26:37.028624 90.43% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/444446@13.235.45.114) Running State Change CS_NEW (Cur 2 Tot 11800)
2026-05-07 07:26:37.028624 90.43% [INFO] sofia.c:10460 sofia/internal/444446@13.235.45.114 receiving invite from 199.127.61.12:55422 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1661294862-910153926-1960971005
2026-05-07 07:26:37.028624 90.43% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:26:37.028624 90.43% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/444446@13.235.45.114) State NEW
2026-05-07 07:26:37.028624 90.43% [DEBUG] sofia.c:2419 detaching session 01b90c91-b8d9-4453-963a-b35a831d49d9
2026-05-07 07:26:37.288605 90.43% [DEBUG] sofia.c:2532 Re-attaching to session 01b90c91-b8d9-4453-963a-b35a831d49d9
2026-05-07 07:26:37.288605 90.43% [INFO] sofia.c:10460 sofia/internal/444446@13.235.45.114 receiving invite from 199.127.61.12:55422 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 1661294862-910153926-1960971005
2026-05-07 07:26:37.288605 90.43% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:26:37.288605 90.43% [WARNING] sofia_reg.c:3210 Can't find user [444446@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="444446" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:37.288605 90.43% [NOTICE] sofia.c:2417 Hangup sofia/internal/444446@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:26:37.308474 90.43% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/444446@13.235.45.114) Running State Change CS_HANGUP (Cur 2 Tot 11800)
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/444446@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/444446@13.235.45.114) State HANGUP
2026-05-07 07:26:37.308474 90.43% [DEBUG] mod_sofia.c:469 Channel sofia/internal/444446@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:59 sofia/internal/444446@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/444446@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/444446@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/444446@13.235.45.114) Running State Change CS_REPORTING (Cur 2 Tot 11800)
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/444446@13.235.45.114) State REPORTING
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:168 sofia/internal/444446@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/444446@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/444446@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_session.c:1744 Session 11800 (sofia/internal/444446@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:26:37.308474 90.43% [NOTICE] switch_core_session.c:1762 Session 11800 (sofia/internal/444446@13.235.45.114) Ended
2026-05-07 07:26:37.308474 90.43% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/444446@13.235.45.114 [CS_DESTROY]
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/444446@13.235.45.114) Running State Change CS_DESTROY (Cur 1 Tot 11800)
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/444446@13.235.45.114) State DESTROY
2026-05-07 07:26:37.308474 90.43% [DEBUG] mod_sofia.c:380 sofia/internal/444446@13.235.45.114 SOFIA DESTROY
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:175 sofia/internal/444446@13.235.45.114 Standard DESTROY
2026-05-07 07:26:37.308474 90.43% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/444446@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:26:37.468577 90.43% [NOTICE] sofia.c:1065 Hangup sofia/internal/1000@13.235.45.114 [CS_EXECUTE] [NORMAL_CLEARING]
2026-05-07 07:26:37.468577 90.43% [DEBUG] mod_audio_stream.c:151 mod_audio_stream cmd: d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4 stop
2026-05-07 07:26:37.468577 90.43% [ERR] mod_audio_stream.c:233 Error locating session d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4
2026-05-07 07:26:37.468577 90.43% [INFO] switch_cpp.cpp:1466 === PIPECAT AGENT ENDED ===
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_cpp.cpp:1210 sofia/internal/1000@13.235.45.114 destroy/unlink session from object
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_session.c:2979 sofia/internal/1000@13.235.45.114 skip receive message [APPLICATION_EXEC_COMPLETE] (channel is hungup already)
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:647 (sofia/internal/1000@13.235.45.114) State EXECUTE going to sleep
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 11800)
2026-05-07 07:26:37.468577 90.43% [INFO] mod_audio_stream.c:34 Got SWITCH_ABC_TYPE_CLOSE.
2026-05-07 07:26:37.468577 90.43% [DEBUG] audio_streamer_glue.cpp:889 (d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4) stream_session_cleanup
2026-05-07 07:26:37.468577 90.43% [DEBUG] audio_streamer_glue.cpp:41 disconnecting...
2026-05-07 07:26:37.468577 90.43% [INFO] audio_streamer_glue.cpp:502 d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4 destroy_tech_pvt
2026-05-07 07:26:37.468577 90.43% [INFO] audio_streamer_glue.cpp:921 (d0ddc190-2e1d-4dd0-a3ad-b1aeccdc3da4) stream_session_cleanup: connection closed
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_media_bug.c:1326 Removing BUG from sofia/internal/1000@13.235.45.114
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/1000@13.235.45.114) Callstate Change ACTIVE -> HANGUP
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/1000@13.235.45.114) State HANGUP
2026-05-07 07:26:37.468577 90.43% [DEBUG] mod_sofia.c:469 Channel sofia/internal/1000@13.235.45.114 hanging up, cause: NORMAL_CLEARING
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:59 sofia/internal/1000@13.235.45.114 Standard HANGUP, cause: NORMAL_CLEARING
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/1000@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/1000@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 11800)
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/1000@13.235.45.114) State REPORTING
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:168 sofia/internal/1000@13.235.45.114 Standard REPORTING, cause: NORMAL_CLEARING
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/1000@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/1000@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_session.c:1744 Session 11796 (sofia/internal/1000@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:26:37.468577 90.43% [NOTICE] switch_core_session.c:1762 Session 11796 (sofia/internal/1000@13.235.45.114) Ended
2026-05-07 07:26:37.468577 90.43% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/1000@13.235.45.114 [CS_DESTROY]
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/1000@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 11800)
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1000@13.235.45.114) State DESTROY
2026-05-07 07:26:37.468577 90.43% [DEBUG] mod_sofia.c:380 sofia/internal/1000@13.235.45.114 SOFIA DESTROY
2026-05-07 07:26:37.468577 90.43% [DEBUG] mod_opus.c:735 Opus decoder stats: Frames[0] PLC[0] FEC[0]
2026-05-07 07:26:37.468577 90.43% [DEBUG] mod_opus.c:750 Opus encoder stats: Frames[0] Bytes encoded[0] Encoded length ms[0] Average encoded bitrate bps[0]
2026-05-07 07:26:37.468577 90.43% [DEBUG] mod_opus.c:735 Opus decoder stats: Frames[0] PLC[0] FEC[0]
2026-05-07 07:26:37.468577 90.43% [DEBUG] mod_opus.c:750 Opus encoder stats: Frames[0] Bytes encoded[0] Encoded length ms[0] Average encoded bitrate bps[0]
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:175 sofia/internal/1000@13.235.45.114 Standard DESTROY
2026-05-07 07:26:37.468577 90.43% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1000@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:26:40.268582 91.87% [WARNING] sofia_reg.c:3210 Can't find user [800@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="800" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:44.568457 92.83% [WARNING] sofia_reg.c:3210 Can't find user [816@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="816" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:48.208603 93.80% [WARNING] sofia_reg.c:3210 Can't find user [831@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="831" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:49.108568 94.07% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/1603@13.235.45.114 [c71c8be1-9af3-4386-94cc-7b7ec308cd64]
2026-05-07 07:26:49.108568 94.07% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1603@13.235.45.114) Running State Change CS_NEW (Cur 1 Tot 11801)
2026-05-07 07:26:49.108568 94.07% [INFO] sofia.c:10460 sofia/internal/1603@13.235.45.114 receiving invite from 199.127.61.12:61628 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 244202151-1074296583-1352874989
2026-05-07 07:26:49.108568 94.07% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:26:49.108568 94.07% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/1603@13.235.45.114) State NEW
2026-05-07 07:26:49.108568 94.07% [DEBUG] sofia.c:2419 detaching session c71c8be1-9af3-4386-94cc-7b7ec308cd64
2026-05-07 07:26:49.348531 94.07% [DEBUG] sofia.c:2532 Re-attaching to session c71c8be1-9af3-4386-94cc-7b7ec308cd64
2026-05-07 07:26:49.368526 94.07% [INFO] sofia.c:10460 sofia/internal/1603@13.235.45.114 receiving invite from 199.127.61.12:61628 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 244202151-1074296583-1352874989
2026-05-07 07:26:49.368526 94.07% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:26:49.368526 94.07% [WARNING] sofia_reg.c:3210 Can't find user [1603@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1603" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:49.368526 94.07% [NOTICE] sofia.c:2417 Hangup sofia/internal/1603@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:26:49.388551 94.07% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1603@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 11801)
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/1603@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/1603@13.235.45.114) State HANGUP
2026-05-07 07:26:49.388551 94.07% [DEBUG] mod_sofia.c:469 Channel sofia/internal/1603@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:59 sofia/internal/1603@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/1603@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/1603@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1603@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 11801)
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/1603@13.235.45.114) State REPORTING
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:168 sofia/internal/1603@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/1603@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/1603@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_session.c:1744 Session 11801 (sofia/internal/1603@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:26:49.388551 94.07% [NOTICE] switch_core_session.c:1762 Session 11801 (sofia/internal/1603@13.235.45.114) Ended
2026-05-07 07:26:49.388551 94.07% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/1603@13.235.45.114 [CS_DESTROY]
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/1603@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 11801)
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1603@13.235.45.114) State DESTROY
2026-05-07 07:26:49.388551 94.07% [DEBUG] mod_sofia.c:380 sofia/internal/1603@13.235.45.114 SOFIA DESTROY
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:175 sofia/internal/1603@13.235.45.114 Standard DESTROY
2026-05-07 07:26:49.388551 94.07% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1603@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:26:52.348632 94.77% [WARNING] sofia_reg.c:3210 Can't find user [832@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="832" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:56.488569 95.73% [WARNING] sofia_reg.c:3210 Can't find user [833@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="833" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:58.268544 96.23% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/1603@13.235.45.114 [84e77679-e41d-4f46-9c0d-fad8cc3e6d18]
2026-05-07 07:26:58.268544 96.23% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1603@13.235.45.114) Running State Change CS_NEW (Cur 1 Tot 11802)
2026-05-07 07:26:58.268544 96.23% [INFO] sofia.c:10460 sofia/internal/1603@13.235.45.114 receiving invite from 199.127.61.12:65121 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 2004252661-672573151-2008109879
2026-05-07 07:26:58.268544 96.23% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:26:58.268544 96.23% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/1603@13.235.45.114) State NEW
2026-05-07 07:26:58.268544 96.23% [DEBUG] sofia.c:2419 detaching session 84e77679-e41d-4f46-9c0d-fad8cc3e6d18
2026-05-07 07:26:58.548557 96.23% [DEBUG] sofia.c:2532 Re-attaching to session 84e77679-e41d-4f46-9c0d-fad8cc3e6d18
2026-05-07 07:26:58.548557 96.23% [INFO] sofia.c:10460 sofia/internal/1603@13.235.45.114 receiving invite from 199.127.61.12:65121 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 2004252661-672573151-2008109879
2026-05-07 07:26:58.548557 96.23% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:26:58.548557 96.23% [WARNING] sofia_reg.c:3210 Can't find user [1603@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1603" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:26:58.548557 96.23% [NOTICE] sofia.c:2417 Hangup sofia/internal/1603@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:26:58.568544 96.23% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1603@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 11802)
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/1603@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/1603@13.235.45.114) State HANGUP
2026-05-07 07:26:58.568544 96.23% [DEBUG] mod_sofia.c:469 Channel sofia/internal/1603@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:59 sofia/internal/1603@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/1603@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/1603@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1603@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 11802)
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/1603@13.235.45.114) State REPORTING
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:168 sofia/internal/1603@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/1603@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/1603@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_session.c:1744 Session 11802 (sofia/internal/1603@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:26:58.568544 96.23% [NOTICE] switch_core_session.c:1762 Session 11802 (sofia/internal/1603@13.235.45.114) Ended
2026-05-07 07:26:58.568544 96.23% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/1603@13.235.45.114 [CS_DESTROY]
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/1603@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 11802)
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1603@13.235.45.114) State DESTROY
2026-05-07 07:26:58.568544 96.23% [DEBUG] mod_sofia.c:380 sofia/internal/1603@13.235.45.114 SOFIA DESTROY
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:175 sofia/internal/1603@13.235.45.114 Standard DESTROY
2026-05-07 07:26:58.568544 96.23% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1603@13.235.45.114) State DESTROY going to sleep
2026-05-07 07:27:00.388554 96.77% [WARNING] sofia_reg.c:3210 Can't find user [834@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="834" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:27:04.268617 97.77% [WARNING] sofia_reg.c:3210 Can't find user [835@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="835" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:27:06.848457 98.73% [WARNING] sofia_reg.c:3210 Can't find user [836@172.31.38.106] from 5.39.101.60
You must define a domain called '172.31.38.106' in your directory and add a user with the id="836" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:27:06.988529 98.73% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/1603@13.235.45.114 [bbc1551a-814f-49e1-923b-a9f7ae8c728b]
2026-05-07 07:27:06.988529 98.73% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1603@13.235.45.114) Running State Change CS_NEW (Cur 1 Tot 11803)
2026-05-07 07:27:06.988529 98.73% [INFO] sofia.c:10460 sofia/internal/1603@13.235.45.114 receiving invite from 199.127.61.12:50945 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 42023491-1753857095-591993190
2026-05-07 07:27:06.988529 98.73% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:27:06.988529 98.73% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/1603@13.235.45.114) State NEW
2026-05-07 07:27:06.988529 98.73% [DEBUG] sofia.c:2419 detaching session bbc1551a-814f-49e1-923b-a9f7ae8c728b
2026-05-07 07:27:07.228537 98.73% [DEBUG] sofia.c:2532 Re-attaching to session bbc1551a-814f-49e1-923b-a9f7ae8c728b
2026-05-07 07:27:07.248553 98.73% [INFO] sofia.c:10460 sofia/internal/1603@13.235.45.114 receiving invite from 199.127.61.12:50945 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: 42023491-1753857095-591993190
2026-05-07 07:27:07.248553 98.73% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 199.127.61.12:0.
2026-05-07 07:27:07.248553 98.73% [WARNING] sofia_reg.c:3210 Can't find user [1603@172.31.38.106] from 199.127.61.12
You must define a domain called '172.31.38.106' in your directory and add a user with the id="1603" attribute
and you must configure your device to use the proper domain in its authentication credentials.
2026-05-07 07:27:07.248553 98.73% [NOTICE] sofia.c:2417 Hangup sofia/internal/1603@13.235.45.114 [CS_NEW] [CALL_REJECTED]
2026-05-07 07:27:07.268561 98.73% [DEBUG] sofia.c:1527 Channel is already hungup.
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1603@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 11803)
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/1603@13.235.45.114) Callstate Change DOWN -> HANGUP
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/1603@13.235.45.114) State HANGUP
2026-05-07 07:27:07.268561 98.73% [DEBUG] mod_sofia.c:469 Channel sofia/internal/1603@13.235.45.114 hanging up, cause: CALL_REJECTED
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:59 sofia/internal/1603@13.235.45.114 Standard HANGUP, cause: CALL_REJECTED
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/1603@13.235.45.114) State HANGUP going to sleep
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/1603@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1603@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 11803)
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/1603@13.235.45.114) State REPORTING
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:168 sofia/internal/1603@13.235.45.114 Standard REPORTING, cause: CALL_REJECTED
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/1603@13.235.45.114) State REPORTING going to sleep
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/1603@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_session.c:1744 Session 11803 (sofia/internal/1603@13.235.45.114) Locked, Waiting on external entities
2026-05-07 07:27:07.268561 98.73% [NOTICE] switch_core_session.c:1762 Session 11803 (sofia/internal/1603@13.235.45.114) Ended
2026-05-07 07:27:07.268561 98.73% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/1603@13.235.45.114 [CS_DESTROY]
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/1603@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 11803)
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1603@13.235.45.114) State DESTROY
2026-05-07 07:27:07.268561 98.73% [DEBUG] mod_sofia.c:380 sofia/internal/1603@13.235.45.114 SOFIA DESTROY
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:175 sofia/internal/1603@13.235.45.114 Standard DESTROY
2026-05-07 07:27:07.268561 98.73% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1603@13.235.45.114) State DESTROY going to sleep
freeswitch@ip-172-31-38-106> 