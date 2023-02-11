<template>
    <form @submit.prevent="create_user">
        <div class="form-inputs">
            <div v-if="password_not_matching">
                <h4 style="color: red; text-align: center">Passwords Do Not Match!</h4>
            </div>
            <div class="form-input">
                <label for="username">Create Username:</label>
                <br/>
                <input type="text" name="username" v-model="username"/>
            </div>
            <div class="form-input">
                <label for="password">Create Password:</label>
                <br/>
                <input type="password" name="password" v-model="password"/>
            </div>
            <div class="form-input">
                <label for="confirm_password">Re-Enter Password:</label>
                <br/>
                <input type="password" name="confirm_password" v-model="confirm_password"/>
            </div>
            <div class="form-input">
                <input type="submit" value="Sign Up"/>
            </div>
        </div>
    </form>
</template>

<script>

export default {
    name: 'SignupPage',
    data() {
        return {
            username: '',
            password: '',
            confirm_password: '',
            password_not_matching: false,
        }
    },
    methods: {
        create_user(){
            if (this.confirm_password !== this.password){
                this.password_not_matching = true
            } else {
                const body_msg = JSON.stringify({username: this.username, password: this.password})
                fetch('http://localhost:8000/create', {
                    method: 'POST',
                    headers: {
                        "Content-type": "application/json",
                    }, 
                    body: body_msg,
                }).then(data => {
                        data.json().then(
                            data => {
                                this.$cookies.set('token', data['token'])
                                this.$router.push('/').then(() => { this.$router.go() })
                            }
                        )
                })
            }
        }
    }
}

</script>
