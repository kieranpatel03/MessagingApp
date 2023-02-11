<template>
    <h1 class="person-name">{{ message_to_name }}</h1>
    <div class="message_list">
        <div>
            <div v-for="message in current_messages" :key="message.id" style="margin: 20px;">
                <div :class="message.user_sent == this.message_from_id ? ['right', 'message_block'] : ['left', 'message_block']">
                    <p class="content" style="font-size: 10px;">{{ message.date_sent }}</p>
                    <h6 class="content" style="text-align: left">{{ message.message }}</h6>
                </div>
            </div>
            <div class="send-div">
                <textarea class='send-message' v-model='message_typing' placeholder="Send Message"></textarea>
                <input type="button" class="button-message" @click="add_msg"/>
            </div>
        </div>
    </div>
</template>

<script>

export default {
    name: 'MessageList',
    data() {
        return {
            current_messages: {},
            message_to_name: '',
            message_typing: '',
            message_to_id: 0,
            message_from_id: 0,
        }
    },
    methods: {
        update_msgs(){
            fetch(`http://127.0.0.1:8000?user_id=${this.$route.params.id}`, {
        method: 'GET',
        headers: {
          "Authorization": this.$cookies.get('token')
      }}).then(response => response.json()).then(this.unwrap_data)
        },
        unwrap_data(data){
            this.current_messages = data['message_list'];
            this.message_to_name = data['message_to_name'];
            this.message_to_id = data['message_to_id']
            this.message_from_id = data['message_from_id']
        },
        add_msg(){
            const body_msg = JSON.stringify({user_to: this.message_to_id, user_sent: this.message_from_id, message : this.message_typing})  
            fetch(`http://127.0.0.1:8000/insert`, {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                    "Authorization": this.$cookies.get('token'),
                }, 
                body: body_msg,
            }).then(this.message_typing = '').then(this.update_msgs).catch(function(error) {
                console.log('Request failed', error);
            });
        }
    },
    created() {
        this.update_msgs()
    }
}

</script>

<style>

.send-div {
    width: 90%;
    display: flex;
    position: fixed;
}

.send-message {
    width: 90%;
}

.button-message {
    background: url("../assets/send_img.png") no-repeat;  
    background-size: 100% 100%;
    width: 4%;
    height: 50px;
}

.person-name {
    text-align: center;
}

.message_block {
    position: relative;
    background: #ffffff;
    font-family: Arial;
    font-size: 20px;
    text-align: center;
    width: 40%;
    border-radius: 10px;
    padding: 0px;
    border: #030303 solid 1px;
}

.left:after {
    content: '';
    position: absolute;
    display: block;
    width: 0;
    border-style: solid;
    border-width: 0 0 11px 13px;
    border-color: transparent transparent #ffffff transparent;
    top: 70%;
    left: -13px;
    margin-top: -5.5px;
}
.left:before {
    content: '';
    position: absolute;
    width: 0;
    border-style: solid;
    border-width: 0 0 12px 14px;
    border-color: transparent transparent #030303 transparent;
    top: 70%;
    left: -15px;
    margin-top: -5.5px;
    display: block;
}


.right:after {
    content: '';
    position: absolute;
    display: block;
    width: 0;
    border-style: solid;
    border-width: 11px 0 0 13px;
    border-color: transparent transparent transparent #ffffff;
    top: 70%;
    right: -13px;
    margin-top: -5.5px;
}
.right:before {
    content: '';
    position: absolute;
    width: 0;
    border-style: solid;
    border-width: 12px 0 0 14px;
    border-color: transparent transparent transparent #030303;
    top: 70%;
    right: -15px;
    margin-top: -5.5px;
    display: block;
}

.left {
    margin: 0 auto 0 0;
}

.right {
    margin: 0 0 0 auto;
}

.content {
    margin: 10px;
}

.message_list {
    width: 90%;
    margin: 10px auto;
    overflow-y: scroll; 
    height:400px;
    display:flex; 
    flex-direction:column-reverse;
}

</style>