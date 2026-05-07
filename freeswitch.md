root@ip-172-31-38-106:/var/lib# tail -f /usr/local/freeswitch/log/freeswitch.log
4b9868aa-34d5-4ff5-9a6f-52a5ee804a4b 2026-05-07 09:16:53.508600 94.27% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/1000@13.235.45.114 [CS_DESTROY]
4b9868aa-34d5-4ff5-9a6f-52a5ee804a4b 2026-05-07 09:16:53.508600 94.27% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/1000@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 12367)
4b9868aa-34d5-4ff5-9a6f-52a5ee804a4b 2026-05-07 09:16:53.508600 94.27% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1000@13.235.45.114) State DESTROY
4b9868aa-34d5-4ff5-9a6f-52a5ee804a4b 2026-05-07 09:16:53.508600 94.27% [DEBUG] mod_sofia.c:380 sofia/internal/1000@13.235.45.114 SOFIA DESTROY
4b9868aa-34d5-4ff5-9a6f-52a5ee804a4b 2026-05-07 09:16:53.508600 94.27% [DEBUG] mod_opus.c:735 Opus decoder stats: Frames[0] PLC[0] FEC[0]
4b9868aa-34d5-4ff5-9a6f-52a5ee804a4b 2026-05-07 09:16:53.508600 94.27% [DEBUG] mod_opus.c:750 Opus encoder stats: Frames[0] Bytes encoded[0] Encoded length ms[0] Average encoded bitrate bps[0]
4b9868aa-34d5-4ff5-9a6f-52a5ee804a4b 2026-05-07 09:16:53.508600 94.27% [DEBUG] mod_opus.c:735 Opus decoder stats: Frames[0] PLC[0] FEC[0]
4b9868aa-34d5-4ff5-9a6f-52a5ee804a4b 2026-05-07 09:16:53.508600 94.27% [DEBUG] mod_opus.c:750 Opus encoder stats: Frames[0] Bytes encoded[0] Encoded length ms[0] Average encoded bitrate bps[0]
4b9868aa-34d5-4ff5-9a6f-52a5ee804a4b 2026-05-07 09:16:53.508600 94.27% [DEBUG] switch_core_state_machine.c:175 sofia/internal/1000@13.235.45.114 Standard DESTROY
4b9868aa-34d5-4ff5-9a6f-52a5ee804a4b 2026-05-07 09:16:53.508600 94.27% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1000@13.235.45.114) State DESTROY going to sleep
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.748602 95.50% [NOTICE] switch_channel.c:1142 New Channel sofia/internal/1000@13.235.45.114 [8398b0ce-8012-4f1e-b466-92022bf4471c]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.748602 95.50% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_NEW (Cur 1 Tot 12368)
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.748602 95.50% [INFO] sofia.c:10460 sofia/internal/1000@13.235.45.114 receiving invite from 152.59.120.238:27588 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: iTQqBNMQ4r
2026-05-07 09:30:41.748602 95.50% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 152.59.120.238:0.
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.768550 95.50% [DEBUG] switch_core_state_machine.c:600 (sofia/internal/1000@13.235.45.114) State NEW
2026-05-07 09:30:41.768550 95.50% [DEBUG] sofia.c:2419 detaching session 8398b0ce-8012-4f1e-b466-92022bf4471c
2026-05-07 09:30:41.848526 95.50% [DEBUG] sofia.c:2532 Re-attaching to session 8398b0ce-8012-4f1e-b466-92022bf4471c
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [INFO] sofia.c:10460 sofia/internal/1000@13.235.45.114 receiving invite from 152.59.120.238:27588 version: 1.10.12-release git a88d069 2024-08-02 21:02:27Z 64bit call-id: iTQqBNMQ4r
2026-05-07 09:30:41.868552 95.50% [DEBUG] sofia.c:10554 verifying acl "domains" for ip/port 152.59.120.238:0.
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] sofia.c:7493 Channel sofia/internal/1000@13.235.45.114 entering state [received][100]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] sofia.c:7503 Remote SDP:
8398b0ce-8012-4f1e-b466-92022bf4471c v=0
8398b0ce-8012-4f1e-b466-92022bf4471c o=1000 1052 1252 IN IP4 152.59.120.238
8398b0ce-8012-4f1e-b466-92022bf4471c s=Talk
8398b0ce-8012-4f1e-b466-92022bf4471c c=IN IP4 152.59.120.238
8398b0ce-8012-4f1e-b466-92022bf4471c t=0 0
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtcp-xr:rcvr-rtt=all:10000 stat-summary=loss,dup,jitt,TTL voip-metrics
8398b0ce-8012-4f1e-b466-92022bf4471c a=record:off
8398b0ce-8012-4f1e-b466-92022bf4471c m=audio 14300 RTP/AVP 96 97 98 0 8 18 101 99 100
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:96 opus/48000/2
8398b0ce-8012-4f1e-b466-92022bf4471c a=fmtp:96 useinbandfec=1
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:97 speex/16000
8398b0ce-8012-4f1e-b466-92022bf4471c a=fmtp:97 vbr=on
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:98 speex/8000
8398b0ce-8012-4f1e-b466-92022bf4471c a=fmtp:98 vbr=on
8398b0ce-8012-4f1e-b466-92022bf4471c a=fmtp:18 annexb=yes
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:101 telephone-event/48000
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:99 telephone-event/16000
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:100 telephone-event/8000
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtcp:43245
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtcp-fb:* trr-int 1000
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtcp-fb:* ccm tmmbr
8398b0ce-8012-4f1e-b466-92022bf4471c 
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] sofia.c:7906 (sofia/internal/1000@13.235.45.114) State Change CS_NEW -> CS_INIT
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_INIT (Cur 1 Tot 12368)
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:624 (sofia/internal/1000@13.235.45.114) State INIT
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] mod_sofia.c:97 sofia/internal/1000@13.235.45.114 SOFIA INIT
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:40 sofia/internal/1000@13.235.45.114 Standard INIT
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:48 (sofia/internal/1000@13.235.45.114) State Change CS_INIT -> CS_ROUTING
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:624 (sofia/internal/1000@13.235.45.114) State INIT going to sleep
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_ROUTING (Cur 1 Tot 12368)
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_channel.c:2399 (sofia/internal/1000@13.235.45.114) Callstate Change DOWN -> RINGING
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:640 (sofia/internal/1000@13.235.45.114) State ROUTING
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] mod_sofia.c:158 sofia/internal/1000@13.235.45.114 SOFIA ROUTING
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:230 sofia/internal/1000@13.235.45.114 Standard ROUTING
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [INFO] mod_dialplan_xml.c:639 Processing 1000 <1000>->7007 in context default
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->unloop] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [unloop] ${unroll_loops}(true) =~ /^true$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [unloop] ${sip_looped_call}() =~ /^true$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->tod_example] continue=true
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Date/Time Match (PASS) [tod_example] break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Action set(open=true)
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->holiday_example] continue=true
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Date/TimeMatch (FAIL) [holiday_example] break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->global-intercept] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [global-intercept] destination_number(7007) =~ /^886$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->group-intercept] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [group-intercept] destination_number(7007) =~ /^\*8$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->intercept-ext] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [intercept-ext] destination_number(7007) =~ /^\*\*(\d+)$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->redial] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [redial] destination_number(7007) =~ /^(redial|870)$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->global] continue=true
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [global] ${call_debug}(false) =~ /^true$/ break=never
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [global] ${default_password}(Test1234) =~ /^1234$/ break=never
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [global] ${rtp_has_crypto}() =~ /^(AEAD_AES_256_GCM_8|AEAD_AES_128_GCM_8|AES_CM_256_HMAC_SHA1_80|AES_CM_192_HMAC_SHA1_80|AES_CM_128_HMAC_SHA1_80|AES_CM_256_HMAC_SHA1_32|AES_CM_192_HMAC_SHA1_32|AES_CM_128_HMAC_SHA1_32|AES_CM_128_NULL_AUTH)$/ break=never
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [global] ${endpoint_disposition}(DELAYED NEGOTIATION) =~ /^(DELAYED NEGOTIATION)/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [global] ${switch_r_sdp}(v=0
8398b0ce-8012-4f1e-b466-92022bf4471c o=1000 1052 1252 IN IP4 152.59.120.238
8398b0ce-8012-4f1e-b466-92022bf4471c s=Talk
8398b0ce-8012-4f1e-b466-92022bf4471c c=IN IP4 152.59.120.238
8398b0ce-8012-4f1e-b466-92022bf4471c t=0 0
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtcp-xr:rcvr-rtt=all:10000 stat-summary=loss,dup,jitt,TTL voip-metrics
8398b0ce-8012-4f1e-b466-92022bf4471c a=record:off
8398b0ce-8012-4f1e-b466-92022bf4471c m=audio 14300 RTP/AVP 96 97 98 0 8 18 101 99 100
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:96 opus/48000/2
8398b0ce-8012-4f1e-b466-92022bf4471c a=fmtp:96 useinbandfec=1
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:97 speex/16000
8398b0ce-8012-4f1e-b466-92022bf4471c a=fmtp:97 vbr=on
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:98 speex/8000
8398b0ce-8012-4f1e-b466-92022bf4471c a=fmtp:98 vbr=on
8398b0ce-8012-4f1e-b466-92022bf4471c a=fmtp:18 annexb=yes
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:101 telephone-event/48000
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:99 telephone-event/16000
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:100 telephone-event/8000
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtcp:43245
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtcp-fb:* trr-int 1000
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtcp-fb:* ccm tmmbr
8398b0ce-8012-4f1e-b466-92022bf4471c ) =~ /(AES_CM_128_HMAC_SHA1_32|AES_CM_128_HMAC_SHA1_80)/ break=never
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Absolute Condition [global]
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Action hash(insert/${domain_name}-spymap/${caller_id_number}/${uuid})
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Action hash(insert/${domain_name}-last_dial/${caller_id_number}/${destination_number})
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Action hash(insert/${domain_name}-last_dial/global/${uuid})
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Action export(RFC2822_DATE=${strftime(%a, %d %b %Y %T %z)})
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->snom-demo-2] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [snom-demo-2] destination_number(7007) =~ /^9001$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->snom-demo-1] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [snom-demo-1] destination_number(7007) =~ /^9000$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->eavesdrop] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [eavesdrop] destination_number(7007) =~ /^88(\d{4})$|^\*0(.*)$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->eavesdrop] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [eavesdrop] destination_number(7007) =~ /^779$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->call_return] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [call_return] destination_number(7007) =~ /^\*69$|^869$|^lcr$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->del-group] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [del-group] destination_number(7007) =~ /^80(\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->add-group] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [add-group] destination_number(7007) =~ /^81(\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->call-group-simo] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [call-group-simo] destination_number(7007) =~ /^82(\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->call-group-order] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [call-group-order] destination_number(7007) =~ /^83(\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->extension-intercom] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [extension-intercom] destination_number(7007) =~ /^8(10[01][0-9])$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->Local_Extension] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [Local_Extension] destination_number(7007) =~ /^(10[01][0-9])$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->Local_Extension_Skinny] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [Local_Extension_Skinny] destination_number(7007) =~ /^(11[01][0-9])$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->group_dial_sales] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [group_dial_sales] destination_number(7007) =~ /^2000$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->group_dial_support] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [group_dial_support] destination_number(7007) =~ /^2001$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->group_dial_billing] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [group_dial_billing] destination_number(7007) =~ /^2002$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->operator] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [operator] destination_number(7007) =~ /^(operator|0)$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->vmain] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [vmain] destination_number(7007) =~ /^vmain$|^4000$|^\*98$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->sip_uri] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [sip_uri] destination_number(7007) =~ /^sip:(.*)$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->nb_conferences] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [nb_conferences] destination_number(7007) =~ /^(30\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->wb_conferences] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [wb_conferences] destination_number(7007) =~ /^(31\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->uwb_conferences] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [uwb_conferences] destination_number(7007) =~ /^(32\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->cdquality_conferences] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [cdquality_conferences] destination_number(7007) =~ /^(33\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->cdquality_stereo_conferences] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [cdquality_stereo_conferences] destination_number(7007) =~ /^(35\d{2}).*?-screen$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->conference-canvases] continue=true
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [conference-canvases] destination_number(7007) =~ /(35\d{2})-canvas-(\d+)/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->conf mod] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [conf mod] destination_number(7007) =~ /^6070-moderator$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->cdquality_conferences] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [cdquality_conferences] destination_number(7007) =~ /^(35\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->cdquality_conferences_720] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [cdquality_conferences_720] destination_number(7007) =~ /^(36\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->cdquality_conferences_480] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [cdquality_conferences_480] destination_number(7007) =~ /^(37\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->cdquality_conferences_320] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [cdquality_conferences_320] destination_number(7007) =~ /^(38\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->freeswitch_public_conf_via_sip] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [freeswitch_public_conf_via_sip] destination_number(7007) =~ /^9(888|8888|1616|3232)$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->mad_boss_intercom] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [mad_boss_intercom] destination_number(7007) =~ /^0911$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->mad_boss_intercom] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [mad_boss_intercom] destination_number(7007) =~ /^0912$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->mad_boss] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [mad_boss] destination_number(7007) =~ /^0913$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ivr_demo] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ivr_demo] destination_number(7007) =~ /^5000$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->dynamic_conference] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [dynamic_conference] destination_number(7007) =~ /^5001$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->rtp_multicast_page] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [rtp_multicast_page] destination_number(7007) =~ /^pagegroup$|^7243$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->park] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [park] destination_number(7007) =~ /^5900$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->unpark] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [unpark] destination_number(7007) =~ /^5901$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->valet_park] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [valet_park] destination_number(7007) =~ /^(6000)$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->valet_park] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [valet_park] destination_number(7007) =~ /^((?!6000)60\d{2})$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->park] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [park] source(mod_sofia) =~ /mod_sofia/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [park] destination_number(7007) =~ /park\+(\d+)/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->unpark] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [unpark] source(mod_sofia) =~ /mod_sofia/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [unpark] destination_number(7007) =~ /^parking$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->park] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [park] source(mod_sofia) =~ /mod_sofia/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [park] destination_number(7007) =~ /callpark/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->unpark] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [unpark] source(mod_sofia) =~ /mod_sofia/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [unpark] destination_number(7007) =~ /pickup/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->wait] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [wait] destination_number(7007) =~ /^wait$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->fax_receive] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [fax_receive] destination_number(7007) =~ /^9178$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->fax_transmit] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [fax_transmit] destination_number(7007) =~ /^9179$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ringback_180] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ringback_180] destination_number(7007) =~ /^9180$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ringback_183_uk_ring] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ringback_183_uk_ring] destination_number(7007) =~ /^9181$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ringback_183_music_ring] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ringback_183_music_ring] destination_number(7007) =~ /^9182$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ringback_post_answer_uk_ring] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ringback_post_answer_uk_ring] destination_number(7007) =~ /^9183$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ringback_post_answer_music] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ringback_post_answer_music] destination_number(7007) =~ /^9184$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->ClueCon] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [ClueCon] destination_number(7007) =~ /^9191$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->show_info] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [show_info] destination_number(7007) =~ /^9192$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->video_record] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [video_record] destination_number(7007) =~ /^9193$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->video_playback] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [video_playback] destination_number(7007) =~ /^9194$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->delay_echo] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [delay_echo] destination_number(7007) =~ /^9195$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->echo] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [echo] destination_number(7007) =~ /^9196$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->milliwatt] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [milliwatt] destination_number(7007) =~ /^9197$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->tone_stream] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [tone_stream] destination_number(7007) =~ /^9198$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->hold_music] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [hold_music] destination_number(7007) =~ /^9664$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->laugh break] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [laugh break] destination_number(7007) =~ /^9386$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->101] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (FAIL) [101] destination_number(7007) =~ /^101$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 parsing [default->pipecat_agent] continue=false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Regex (PASS) [pipecat_agent] destination_number(7007) =~ /^7007$/ break=on-false
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Action answer()
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Action sleep(500)
8398b0ce-8012-4f1e-b466-92022bf4471c Dialplan: sofia/internal/1000@13.235.45.114 Action lua(pipecat.lua)
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:281 (sofia/internal/1000@13.235.45.114) State Change CS_ROUTING -> CS_EXECUTE
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:640 (sofia/internal/1000@13.235.45.114) State ROUTING going to sleep
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_EXECUTE (Cur 1 Tot 12368)
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:647 (sofia/internal/1000@13.235.45.114) State EXECUTE
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] mod_sofia.c:213 sofia/internal/1000@13.235.45.114 SOFIA EXECUTE
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_state_machine.c:323 sofia/internal/1000@13.235.45.114 Standard EXECUTE
8398b0ce-8012-4f1e-b466-92022bf4471c EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 set(open=true)
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] mod_dptools.c:1671 SET sofia/internal/1000@13.235.45.114 [open]=[true]
8398b0ce-8012-4f1e-b466-92022bf4471c EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 hash(insert/172.31.38.106-spymap/1000/8398b0ce-8012-4f1e-b466-92022bf4471c)
8398b0ce-8012-4f1e-b466-92022bf4471c EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 hash(insert/172.31.38.106-last_dial/1000/7007)
8398b0ce-8012-4f1e-b466-92022bf4471c EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 hash(insert/172.31.38.106-last_dial/global/8398b0ce-8012-4f1e-b466-92022bf4471c)
8398b0ce-8012-4f1e-b466-92022bf4471c EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 export(RFC2822_DATE=Thu, 07 May 2026 09:30:41 +0000)
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_channel.c:1334 EXPORT (export_vars) [RFC2822_DATE]=[Thu, 07 May 2026 09:30:41 +0000]
8398b0ce-8012-4f1e-b466-92022bf4471c EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 answer()
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [opus:96:48000:20:0:1]/[opus:116:48000:20:0:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5588 Audio Codec Compare [opus:116:48000:20:0:1] ++++ is saved as a match
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [opus:96:48000:20:0:1]/[PCMU:0:8000:20:64000:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [opus:96:48000:20:0:1]/[PCMA:8:8000:20:64000:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:97:16000:20:0:1]/[opus:116:48000:20:0:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:97:16000:20:0:1]/[PCMU:0:8000:20:64000:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:97:16000:20:0:1]/[PCMA:8:8000:20:64000:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:98:8000:20:0:1]/[opus:116:48000:20:0:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:98:8000:20:0:1]/[PCMU:0:8000:20:64000:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [speex:98:8000:20:0:1]/[PCMA:8:8000:20:64000:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMU:0:8000:20:64000:1]/[opus:116:48000:20:0:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMU:0:8000:20:64000:1]/[PCMU:0:8000:20:64000:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5588 Audio Codec Compare [PCMU:0:8000:20:64000:1] ++++ is saved as a match
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMU:0:8000:20:64000:1]/[PCMA:8:8000:20:64000:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMA:8:8000:20:64000:1]/[opus:116:48000:20:0:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMA:8:8000:20:64000:1]/[PCMU:0:8000:20:64000:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [PCMA:8:8000:20:64000:1]/[PCMA:8:8000:20:64000:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5588 Audio Codec Compare [PCMA:8:8000:20:64000:1] ++++ is saved as a match
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [G729:18:8000:20:8000:1]/[opus:116:48000:20:0:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [G729:18:8000:20:8000:1]/[PCMU:0:8000:20:64000:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5526 Audio Codec Compare [G729:18:8000:20:8000:1]/[PCMA:8:8000:20:64000:1]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5438 Set telephone-event payload to 101@48000
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] mod_opus.c:629 Opus encoder: set bitrate to local settings [72000bps]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] mod_opus.c:629 Opus encoder: set bitrate to local settings [72000bps]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:3731 Set Codec sofia/internal/1000@13.235.45.114 opus/48000 20 ms 960 samples 0 bits 1 channels
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_codec.c:111 sofia/internal/1000@13.235.45.114 Original read codec set to opus:116
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5798 Set telephone-event payload to 101@48000
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:5856 sofia/internal/1000@13.235.45.114 Set 2833 dtmf send payload to 101 recv payload to 101
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:8660 AUDIO RTP [sofia/internal/1000@13.235.45.114] 172.31.38.106 port 18030 -> 152.59.120.238 port 14300 codec: 96 ms: 20
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_rtp.c:4566 Starting timer [soft] 960 bytes per 20ms
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:8881 Activating RTCP PORT 43245
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_rtp.c:4898 RTCP send rate is: 1000 and packet rate is: 20000 Remote Port: 43245
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_rtp.c:2692 Setting RTCP remote addr to 152.59.120.238:43245 2
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:8973 sofia/internal/1000@13.235.45.114 Set 2833 dtmf send payload to 101
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:8980 sofia/internal/1000@13.235.45.114 Set 2833 dtmf receive payload to 101
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:9003 sofia/internal/1000@13.235.45.114 Set rtp dtmf delay to 40
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [NOTICE] sofia_media.c:90 Pre-Answer sofia/internal/1000@13.235.45.114!
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_channel.c:3585 (sofia/internal/1000@13.235.45.114) Callstate Change RINGING -> EARLY
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_core_media.c:8642 Audio params are unchanged for sofia/internal/1000@13.235.45.114.
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] mod_sofia.c:914 Local SDP sofia/internal/1000@13.235.45.114:
8398b0ce-8012-4f1e-b466-92022bf4471c v=0
8398b0ce-8012-4f1e-b466-92022bf4471c o=FreeSWITCH 1778128211 1778128212 IN IP4 13.235.45.114
8398b0ce-8012-4f1e-b466-92022bf4471c s=FreeSWITCH
8398b0ce-8012-4f1e-b466-92022bf4471c c=IN IP4 13.235.45.114
8398b0ce-8012-4f1e-b466-92022bf4471c t=0 0
8398b0ce-8012-4f1e-b466-92022bf4471c m=audio 18030 RTP/AVP 96 101
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:96 opus/48000/2
8398b0ce-8012-4f1e-b466-92022bf4471c a=fmtp:96 useinbandfec=1
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtpmap:101 telephone-event/48000
8398b0ce-8012-4f1e-b466-92022bf4471c a=fmtp:101 0-15
8398b0ce-8012-4f1e-b466-92022bf4471c a=ptime:20
8398b0ce-8012-4f1e-b466-92022bf4471c a=sendrecv
8398b0ce-8012-4f1e-b466-92022bf4471c a=rtcp:18031 IN IP4 13.235.45.114
8398b0ce-8012-4f1e-b466-92022bf4471c 
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [NOTICE] mod_dptools.c:1406 Channel [sofia/internal/1000@13.235.45.114] has been answered
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] switch_channel.c:3912 (sofia/internal/1000@13.235.45.114) Callstate Change EARLY -> ACTIVE
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:41.868552 95.50% [DEBUG] sofia.c:7493 Channel sofia/internal/1000@13.235.45.114 entering state [completed][200]
8398b0ce-8012-4f1e-b466-92022bf4471c EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 sleep(500)
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:42.368468 95.50% [DEBUG] sofia.c:7493 Channel sofia/internal/1000@13.235.45.114 entering state [ready][200]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:42.368468 95.50% [DEBUG] switch_rtp.c:7128 Correct audio RTCP ip/port confirmed.
8398b0ce-8012-4f1e-b466-92022bf4471c EXECUTE [depth=0] sofia/internal/1000@13.235.45.114 lua(pipecat.lua)
2026-05-07 09:30:42.388536 95.50% [INFO] switch_cpp.cpp:1466 === PIPECAT AGENT STARTED uuid=8398b0ce-8012-4f1e-b466-92022bf4471c ===
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:42.748598 95.47% [DEBUG] switch_rtp.c:1934 rtcp_stats_init: audio ssrc[3813205223] base_seq[0]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:42.748598 95.47% [DEBUG] switch_rtp.c:7698 Correct audio ip/port confirmed.
2026-05-07 09:30:42.888668 95.47% [INFO] switch_cpp.cpp:1466 Sending: uuid_audio_stream 8398b0ce-8012-4f1e-b466-92022bf4471c start ws://127.0.0.1:8765 stereo 16000
2026-05-07 09:30:42.888668 95.47% [DEBUG] mod_audio_stream.c:151 mod_audio_stream cmd: 8398b0ce-8012-4f1e-b466-92022bf4471c start ws://127.0.0.1:8765 stereo 16000
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:42.888668 95.47% [DEBUG] mod_audio_stream.c:82 calling stream_session_init.
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:42.888668 95.47% [DEBUG] audio_streamer_glue.cpp:485 (8398b0ce-8012-4f1e-b466-92022bf4471c) resampling from 48000 to 16000
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:42.888668 95.47% [DEBUG] audio_streamer_glue.cpp:496 (8398b0ce-8012-4f1e-b466-92022bf4471c) stream_data_init
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:42.888668 95.47% [DEBUG] mod_audio_stream.c:88 adding bug.
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:42.888668 95.47% [DEBUG] switch_core_media_bug.c:976 Attaching BUG to sofia/internal/1000@13.235.45.114
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:42.888668 95.47% [DEBUG] mod_audio_stream.c:92 setting bug private data.
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:42.888668 95.47% [DEBUG] mod_audio_stream.c:95 exiting start_capture.
2026-05-07 09:30:42.888668 95.47% [INFO] switch_cpp.cpp:1466 Result: +OK Success

8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:43.088552 95.47% [INFO] audio_streamer_glue.cpp:281 connection closed
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:30:43.268558 95.47% [DEBUG] switch_core_io.c:448 Setting BUG Codec opus:116
2026-05-07 09:30:43.268558 95.47% [DEBUG] mod_opus.c:629 Opus encoder: set bitrate to local settings [72000bps]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [NOTICE] sofia.c:1065 Hangup sofia/internal/1000@13.235.45.114 [CS_EXECUTE] [NORMAL_CLEARING]
2026-05-07 09:31:44.328579 99.13% [DEBUG] mod_audio_stream.c:151 mod_audio_stream cmd: 8398b0ce-8012-4f1e-b466-92022bf4471c stop
2026-05-07 09:31:44.328579 99.13% [ERR] mod_audio_stream.c:233 Error locating session 8398b0ce-8012-4f1e-b466-92022bf4471c
2026-05-07 09:31:44.328579 99.13% [INFO] switch_cpp.cpp:1466 === PIPECAT AGENT ENDED ===
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_cpp.cpp:1210 sofia/internal/1000@13.235.45.114 destroy/unlink session from object
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_session.c:2979 sofia/internal/1000@13.235.45.114 skip receive message [APPLICATION_EXEC_COMPLETE] (channel is hungup already)
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:647 (sofia/internal/1000@13.235.45.114) State EXECUTE going to sleep
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_HANGUP (Cur 1 Tot 12368)
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [INFO] mod_audio_stream.c:34 Got SWITCH_ABC_TYPE_CLOSE.
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] audio_streamer_glue.cpp:889 (8398b0ce-8012-4f1e-b466-92022bf4471c) stream_session_cleanup
2026-05-07 09:31:44.328579 99.13% [DEBUG] audio_streamer_glue.cpp:41 disconnecting...
2026-05-07 09:31:44.328579 99.13% [INFO] audio_streamer_glue.cpp:502 8398b0ce-8012-4f1e-b466-92022bf4471c destroy_tech_pvt
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [INFO] audio_streamer_glue.cpp:921 (8398b0ce-8012-4f1e-b466-92022bf4471c) stream_session_cleanup: connection closed
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_media_bug.c:1326 Removing BUG from sofia/internal/1000@13.235.45.114
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:844 (sofia/internal/1000@13.235.45.114) Callstate Change ACTIVE -> HANGUP
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/1000@13.235.45.114) State HANGUP
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] mod_sofia.c:469 Channel sofia/internal/1000@13.235.45.114 hanging up, cause: NORMAL_CLEARING
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:59 sofia/internal/1000@13.235.45.114 Standard HANGUP, cause: NORMAL_CLEARING
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:846 (sofia/internal/1000@13.235.45.114) State HANGUP going to sleep
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:616 (sofia/internal/1000@13.235.45.114) State Change CS_HANGUP -> CS_REPORTING
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:581 (sofia/internal/1000@13.235.45.114) Running State Change CS_REPORTING (Cur 1 Tot 12368)
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/1000@13.235.45.114) State REPORTING
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:168 sofia/internal/1000@13.235.45.114 Standard REPORTING, cause: NORMAL_CLEARING
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:932 (sofia/internal/1000@13.235.45.114) State REPORTING going to sleep
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:607 (sofia/internal/1000@13.235.45.114) State Change CS_REPORTING -> CS_DESTROY
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_session.c:1744 Session 12368 (sofia/internal/1000@13.235.45.114) Locked, Waiting on external entities
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [NOTICE] switch_core_session.c:1762 Session 12368 (sofia/internal/1000@13.235.45.114) Ended
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [NOTICE] switch_core_session.c:1766 Close Channel sofia/internal/1000@13.235.45.114 [CS_DESTROY]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:735 (sofia/internal/1000@13.235.45.114) Running State Change CS_DESTROY (Cur 0 Tot 12368)
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1000@13.235.45.114) State DESTROY
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] mod_sofia.c:380 sofia/internal/1000@13.235.45.114 SOFIA DESTROY
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] mod_opus.c:735 Opus decoder stats: Frames[0] PLC[0] FEC[0]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] mod_opus.c:750 Opus encoder stats: Frames[0] Bytes encoded[0] Encoded length ms[0] Average encoded bitrate bps[0]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] mod_opus.c:735 Opus decoder stats: Frames[0] PLC[0] FEC[0]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] mod_opus.c:750 Opus encoder stats: Frames[0] Bytes encoded[0] Encoded length ms[0] Average encoded bitrate bps[0]
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:175 sofia/internal/1000@13.235.45.114 Standard DESTROY
8398b0ce-8012-4f1e-b466-92022bf4471c 2026-05-07 09:31:44.328579 99.13% [DEBUG] switch_core_state_machine.c:745 (sofia/internal/1000@13.235.45.114) State DESTROY going to sleep
