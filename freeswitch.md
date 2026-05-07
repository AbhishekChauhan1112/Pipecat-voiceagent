root@ip-172-31-38-106:/home/ubuntu# # See the existing pipecat dialplan
cat /usr/local/freeswitch/conf/dialplan/default/00_pipecat.xml

# Confirm context mismatch — internal profile sends to 'public' but dialplan is in 'default'
grep -i "context\|user_context" /usr/local/freeswitch/conf/sip_profiles/internal.xml

# See what's in the public dialplan (where Linphone calls actually land)
cat /usr/local/freeswitch/conf/dialplan/public/00_inbound_did.xml

# Check directory for Linphone user (to see user_context)
ls /usr/local/freeswitch/conf/directory/default/
cat /usr/local/freeswitch/conf/directory/default/*.xml | grep -A5 -i "1000\|user_context"
<include>
  <extension name="pipecat_agent" continue="false">
    <condition field="destination_number" expression="^7007$">
      <action application="lua" data="pipecat.lua"/>
    </condition>
  </extension>
</include>
    <param name="context" value="public"/>
<include>
  <extension name="public_did">
    <condition field="destination_number" expression="^(5551212)$">
      <!--
          If you're hosting multiple domains you will want to set the
          target_domain on these calls so they hit the proper domain after you
          transfer the caller into the default context.

          $${domain} is the default domain set from vars.xml but you can set it
          to any domain you have setup in your user directory.

      -->
      <action application="set" data="domain_name=$${domain}"/>
      <!-- This example maps the DID 5551212 to ring 1000 in the default context -->
      <action application="transfer" data="1000 XML default"/>
    </condition>
  </extension>
</include>
1000.xml  1002.xml  1004.xml  1006.xml  1008.xml  1010.xml  1012.xml  1014.xml  1016.xml  1018.xml  brian.xml    example.com.xml
1001.xml  1003.xml  1005.xml  1007.xml  1009.xml  1011.xml  1013.xml  1015.xml  1017.xml  1019.xml  default.xml  skinny-example.xml
  <user id="1000">
    <params>
      <param name="password" value="$${default_password}"/>
      <param name="vm-password" value="1000"/>
    </params>
    <variables>
      <variable name="toll_allow" value="domestic,international,local"/>
      <variable name="accountcode" value="1000"/>
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1000"/>
      <variable name="effective_caller_id_number" value="1000"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
    </variables>
  </user>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1001"/>
      <variable name="effective_caller_id_number" value="1001"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1002"/>
      <variable name="effective_caller_id_number" value="1002"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1003"/>
      <variable name="effective_caller_id_number" value="1003"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1004"/>
      <variable name="effective_caller_id_number" value="1004"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1005"/>
      <variable name="effective_caller_id_number" value="1005"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1006"/>
      <variable name="effective_caller_id_number" value="1006"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1007"/>
      <variable name="effective_caller_id_number" value="1007"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1008"/>
      <variable name="effective_caller_id_number" value="1008"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1009"/>
      <variable name="effective_caller_id_number" value="1009"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1010"/>
      <variable name="effective_caller_id_number" value="1010"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1011"/>
      <variable name="effective_caller_id_number" value="1011"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1012"/>
      <variable name="effective_caller_id_number" value="1012"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1013"/>
      <variable name="effective_caller_id_number" value="1013"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1014"/>
      <variable name="effective_caller_id_number" value="1014"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1015"/>
      <variable name="effective_caller_id_number" value="1015"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1016"/>
      <variable name="effective_caller_id_number" value="1016"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1017"/>
      <variable name="effective_caller_id_number" value="1017"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1018"/>
      <variable name="effective_caller_id_number" value="1018"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Extension 1019"/>
      <variable name="effective_caller_id_number" value="1019"/>
      <variable name="outbound_caller_id_name" value="$${outbound_caller_name}"/>
      <variable name="outbound_caller_id_number" value="$${outbound_caller_id}"/>
      <variable name="callgroup" value="techsupport"/>
--
      <variable name="user_context" value="default"/>
      <variable name="effective_caller_id_name" value="Brian West"/>
      <variable name="effective_caller_id_number" value="1000"/>
      <!-- Don't write a CDR if this is false valid values are: true, false, a_leg and b_leg -->
      <variable name="process_cdr" value="true"/>
      <!-- rtp_secure_media will offer mandatory SRTP on invite AES_CM_128_HMAC_SHA1_32, AES_CM_128_HMAC_SHA1_80 or true-->
      <variable name="rtp_secure_media" value="true"/>
      <!-- limit the max number of outgoing calls for this user -->
--
      <!--<variable name="presence_id" value="1000@$${domain}"/>-->

      <!-- set these to take advantage of a dialplan localized to this user -->
      <!--<variable name="numbering_plan" value="US"/>-->
      <!--<variable name="default_area_code" value="434"/>-->
      <!--<variable name="default_gateway" value="asterlink.com"/>-->
--
        this user a user_context and we don't authenticate this user they will be put in context 'public'.

        This isn't a security issue as the endpoint would be put into the same context 'public' as the 
        sofia profile that starts on 5080 by default. If you're paranoid just remove this file and 
        remove the external profile also.

root@ip-172-31-38-106:/home/ubuntu# 

=============================================================================

