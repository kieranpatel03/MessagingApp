<template>
     <form @submit.prevent="form_submit">
        <div class="msg_sender">
            <div v-if="user_not_exists">
                <h4 style="color: red; text-align: center">That User Does Not Exist!</h4>
            </div>
            <div class="form-input">
                <label for="user_id">Enter User ID:</label>
                <br/>
                <input type="text" name="user_id" v-model="user_id"/>
            </div>
            <div class="form-input">
                <label for="message">Enter Message:</label>
                <br/>
                <textarea style="width: 100%;" type="text" name="message" v-model="message"/>
            </div>
            <div class="form-input send-or-cancel">
                <input type="submit" value="Send"/>
                <button @click="$emit('removeMsgInput')">Cancel</button>
            </div>
        </div>
    </form>
</template>

<script>

export default {
    name: 'SendMessage',
    data() {
        return {
            user_not_exists: false,
            user_id: '',
            message: '',
        }
    },
    methods: {
        form_submit(){
            const body_msg = JSON.stringify({user_to: this.user_id, message: this.message})
            fetch('http://127.0.0.1:8000/insert', {
                method: "POST",
                headers: {
                    "Content-type": "application/json",
                    "Authorization": this.$cookies.get('token'),
                },
                body: body_msg,
            })
            this.$emit("removeMsgInput")
            this.$emit("reload")
        }
    }
}

</script>

<style>

.send-or-cancel{
    display: flex;
    justify-content: space-around;
}

.msg_sender {
    border: solid;
    background-color: #7FFFD4;
    position: absolute;
    left: 40%;
    width: 20%;
}



</style>