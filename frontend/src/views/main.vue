<template>
  <div v-if="$cookies.get('token')">
    <div v-if="sending_msg">
      <SendMessage @remove-msg-input="sending_msg=false" @reload="get_data"/>
    </div>
    <div class="new_msg">
      <div class="new_msg_button" @click="sending_msg=true">+</div>
    </div>
    <div v-for="message in messages" :key="message.user_id" class='message_box'>
      <router-link :to="{path: '/messages/' + message.user_id}" style="text-decoration: none; color: black;">
        <div class='user_and_notif'>
          <h1 class='message_user'>{{ message.user_name }}</h1>
          <h2 v-if="message.number_unread > 0" class='notif_alert'>{{ message.notifs }}</h2>
        </div>
        <p class='last_message_in_chat'>{{ message.last_message }}</p>
      </router-link>
    </div>
  </div>
  <div v-else>
    <h1 style="text-align:center; margin: 250px;">Log In To View Your Messages!</h1>
  </div>
</template>
  
  
<script>

import SendMessage from '@/components/send_message.vue';

export default {
  name: 'MainApp',
  data() {
    return {
        messages: {},
        sending_msg: false,
    }
  },
  methods: {
    get_data(){
      if (this.$cookies.get('token')){
        fetch(`http://127.0.0.1:8000/select`, {
          method: 'GET',
          headers: {
            "Authorization": this.$cookies.get('token'),
        }}).then(
          response => response.json()
        ).then(
          data => this.messages = data
        ).catch(
          //pass
        )
      }
    }
  },
  created() {
    this.get_data()
  },
  components: {
    SendMessage,
  }
}
</script>

<style>

.new_msg {
  margin: 10px auto;
  width: 30%;
  height: 100px;
}

.new_msg_button {
  float: right;
  border: solid;
  font-size: 50px;
  margin: 20px;
  padding: 0px 15px;
  border-radius: 10px;
  background-color: #FFFFFF;
}

.message_box {
    border: solid;
    border-radius: 10px;
    margin: 10px auto;
    width: 30%;
    height: 100px;
    background: #FFFFFF;
}

.message_user {
    margin: 10px 20px;
    font-family: sans-serif;
}

.notif_alert {
    margin: 10px 20px;
    font-family: sans-serif;
    color: #AAFF00;
}

.last_message_in_chat {
    margin: 0px 20px;
}

.user_and_notif {
    display: flex;
    justify-content: space-between;
}

</style>
